# Standard library imports.
import asyncio
import multiprocessing
import qasync
import sys

# Third party imports.
from PySide6.QtWidgets import QApplication

# Local application imports.
from UI.ui_base import UIBase
from UI.ui_splash_screen import SplashScreen


class MainProgram(UIBase):
    """
    Main application class for Metrics.
    Inherits from UIBase to provide the main window and core UI setup, and manages all asynchronous tasks required by the application.
    Coordinates the main window, background async tasks, and application shutdown.
    """

    def __init__(self, application, event_loop, splash):
        """
        Initialises the main application.

        Args:
            application:    The main Qt application instance.
            event_loop:     The asyncio event loop integrated with Qt, used to schedule async tasks alongside GUI events.
            splash:         The splash screen instance displayed during startup.
        """
        super().__init__(event_loop, splash) # Initialises UIBase with splash screen and event loop references.
        self.application = application
        self.application.setQuitOnLastWindowClosed(False) # Prevent the app from quitting automatically when the last window is closed.
        self.application.lastWindowClosed.connect(self.quietExit) # Connect the lastWindowClosed signal to a safe shutdown handler.
        self.event_loop = event_loop
        self.main_task = None # Reference to the main async task manager for later cancellation and cleanup.
        self.running_event = asyncio.Event() # Event flag to control the running state of async tasks.
        self.running_event.set() # Set the event to indicate tasks should run.


    async def manageTasks(self):
        """
        The main async task manager. Gathers and runs all background tasks concurrently. This means the tasks are ran on one CPU core, and they take turns running (only one can run at a time), switching whenever one is waiting.
        This method starts all required background async tasks and waits for them to complete. On cancellation, it ensures a clean shutdown.
        """
        task_list = [self.TASK_MessageProcessing()] # List of background async tasks to run, currently only one task.
        try:
            await asyncio.gather(*task_list) # Run all tasks concurrently and wait for completion.
        except asyncio.CancelledError:
            print("Tasks Cancelled")
        finally:
            await self.shutdown() # Ensure proper cleanup and shutdown.


    async def TASK_MessageProcessing(self):
        """
        Worker async task that processes messages from the UI communications handler. This coroutine waits for the UI communications handler (`ui_comms`) to be initialised,
        then continuously retrieves and processes messages from its async queue while the application is running. Handles exceptions gracefully and supports cooperative cancellation.
        """
        # Wait for ui_comms to be initialised before starting this task.
        while not hasattr(self, 'ui_comms') or self.ui_comms is None:
            await asyncio.sleep(0.1)
        print("Message Processing Started")
        try:
            # Continue processing messages as long as the running event flag is set (i.e., until shutdown is requested).
            while self.running_event.is_set():
                try:
                    # Wait for the next message from the queue.
                    message = await self.ui_comms.message_queue.get()
                    self.ui_comms.handleMessage(message) # Process the message.
                    self.ui_comms.message_queue.task_done() # Mark the message as processed.
                except Exception as e:
                    print(f"E1: {__file__}: {e}")
                    await asyncio.sleep(0.01)
        except asyncio.CancelledError:
            print("Message Processing Stopped")


    def quietExit(self):
        """
        Initiates a safe application shutdown when the last window is closed. The GUI disappears immediately, but background tasks and cleanup continue until shutdown is complete.
        """
        print("Exiting Application")
        self.hide() # Hide the main window immediately.
        # Directly cancel the main task to start the shutdown process.
        if self.main_task and not self.main_task.done():
            self.main_task.cancel()


    async def shutdown(self):
        """
        The final cleanup stage of the application.
        """
        try:
            # First, stop any non-async threads that are running.
            if self.ui_comms.serial_port_handler:
                self.ui_comms.serial_port_handler.stop() # Stop the serial port polling thread.

            # Clearing event signal causes all async tasks to terminate.
            self.running_event.clear()

            # Request cancellation for all tasks that are still running.
            tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
            for task in tasks:
                task.cancel()

            try:
                # Wait for all tasks to finish, with a timeout to avoid hanging.
                await asyncio.wait_for(asyncio.gather(*tasks, return_exceptions=True), timeout=5.0)
            except asyncio.TimeoutError:
                print("Timeout waiting for tasks to cancel")

        except Exception as e:
            print(f"E2: {__file__}: {e}")
        finally:
            # Finally, stop the event loop and exit the application.
            self.application.quit() # This posts a quit event for the Qt event loop.
            self.event_loop.stop()


if __name__ == "__main__":
    """
    'Metrics' generally refers to measurable data or quantitative measurements that help evaluate, compare, or track performance, progress, or quality.
    In a software context, metrics can be used to assess code performance, user interactions, and system behaviours, among other things.
    """
    """
    When a script using multiprocessing is frozen into an executable, starting a new process on Windows re-launches the main executable.
    freeze_support() must be called immediately here. It allows the child process to run its target code instead of re-initializing the entire application,
    which would otherwise create a new window.
    """
    multiprocessing.freeze_support()

    print(f"-------------------")
    print(f"Application Started")
    print(f"-------------------")

    try:
        # Create the main Qt application instance, required for all Qt GUI applications.
        application = QApplication(sys.argv)

        """
        Set the application style to "Fusion" for consistent styling. This must be done right after creating the QApplication instance.
        Failure to do this resulted in style-related issues on some platforms for my QTableWidgets and QTextBrowsers.
        This tells the application to use this consistent, style-sheet friendly engine for drawing all its widgets, "Fusion" correctly
        interprets and applies properties correctly because it gives precedence to user defined styles over any default platform styles.
        """
        application.setStyle("Fusion")

        # Ensure the splash screen is displayed immediately.
        splash = SplashScreen()
        splash.show()
        application.processEvents()

        """
        This approach uses qasync to integrate Python's asyncio event loop with Qt's event loop.
        It is recommended for applications that require both a responsive GUI and asynchronous I/O.
        qasync ensures that both Qt GUI events and asyncio tasks are handled smoothly together.
        """
        event_loop = qasync.QEventLoop(application)
        asyncio.set_event_loop(event_loop)

        # Create and display the main application window, passing in the application instance, event loop, and splash screen.
        program = MainProgram(application, event_loop, splash)
        program.show()

        # Close the splash screen now that the main window is ready and visible.
        splash.close()

        # Start the main asynchronous task manager and keep a reference for controlled shutdown.
        program.main_task = event_loop.create_task(program.manageTasks())

        # Start the integrated Qt/asyncio event loop, keeping the application running and responsive to both GUI and async events.
        event_loop.run_forever()

    except asyncio.CancelledError:
        # This is expected on a clean shutdown.
        pass
    except Exception as e:
        print(f"E3: {__file__}: {e}")
    finally:
        print(f"-------------------")
        print(f"Application Stopped")
        print(f"-------------------")
        sys.exit(0)