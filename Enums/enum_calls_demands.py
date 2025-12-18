# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class CallSource(EnumUtils, Enum):
    """
    Enum class containing all the call sources.
    """
    NO_CALL_SOURCE  = 0
    LOCAL           = 1
    REMOTE          = 2
    SOFTWARE        = 3
    CALIBRATION     = 4
    CREEP_TO_CHARGE = 5


@unique
class CallType(EnumUtils, Enum):
    """
    Enum class containing all the call types.
    """
    NO_CALL_TYPE                            = 0x00

    # Carriage movement only
    CARRIAGE_LEFT                           = 0x01
    CARRIAGE_RIGHT                          = 0x02
    CARRIAGE_UP                             = 0x03       # Not used externally - converted to left or right
    CARRIAGE_DOWN                           = 0x04       # Not used externally - converted to left or right

    # EMC (Main drive)
    EMC_CARRIAGE                            = 0x05
    EMC_CARRIAGE_AND_CHAIR_FOLD             = 0x06
    EMC_CARRIAGE_AND_FOOTREST               = 0x07
    EMC_CARRIAGE_CHAIR_FOLD_AND_FOOTREST    = 0x08

    # Footrest movement only
    FOOTREST_FOLD                           = 0x10
    FOOTREST_UNFOLD                         = 0x11

    # Swivel movement only
    SWIVEL_OUT_LEFT                         = 0x20
    SWIVEL_OUT_RIGHT                        = 0x21
    SWIVEL_IN                               = 0x22
    SWIVEL_IN_A                             = 0x23       # Only used as a call input, is swapped to SWIVEL_IN when read
    SWIVEL_TO_LEFT                          = 0x24
    SWIVEL_TO_RIGHT                         = 0x25

    # Chair fold movement only
    CHAIR_FOLD                              = 0x30
    CHAIR_UNFOLD                            = 0x31
    CHAIR_PARTIAL_FOLD                      = 0x32

    # Standard call - may result in any powered drive motion, based on demand sequencing
    CALL_LEFT                               = 0x0A
    CALL_RIGHT                              = 0x0B
    CALL_UP                                 = 0x0C        # Not used externally - converted to left or right
    CALL_DOWN                               = 0x0D        # Not used externally - converted to left or right

    # Creep to charge
    CREEP_TO_CHARGE_LEFT                    = 0x0E
    CREEP_TO_CHARGE_RIGHT                   = 0x0F

    # EMC (Excluding main drive)
    EMC_CHAIR_FOLD                          = 0xA1
    EMC_SWIVEL                              = 0xA2
    EMC_FOOTREST                            = 0xA3
    EMC_CHAIR_FOLD_AND_FOOTREST             = 0xA4


@unique
class DiagnosticCall(EnumUtils, Enum):
    """
    Enum class containing all the diagnostic software call types.
    """
    NO_CALL                 = 0
    LOCAL_LEFT              = 1
    LOCAL_RIGHT             = 2
    REMOTE_UP               = 3
    REMOTE_DOWN             = 4


@unique
class DemandStates(EnumUtils, Enum):
    """
    Enum class containing all the demand states.
    """
    IDLE                                = 0
    CAL_CHAIRFOLD                       = 1
    CAL_DRIVE                           = 2
    CAL_FOOTREST                        = 3
    CAL_SWIVEL                          = 4
    CARRIAGE_DRIVE                      = 5
    CHAIR_FOLD                          = 6
    CHAIR_PARTIAL_UNFOLD                = 7
    CHAIR_UNFOLD                        = 8
    DELAY                               = 9
    FOLD_FOOTREST                       = 10
    FULL_FOLD                           = 11
    MOVE_TO_BOARDING                    = 12
    APPROACHING_TARGET                  = 13
    MOVE_TO_POINT                       = 14
    MOVING_AND_FOLDING_CHAIR            = 15
    PARTIAL_UNFOLDING                   = 16
    START_LOCAL_NON_SYNC_FOLD           = 17
    START_UNLOADED                      = 18
    SWIVEL_IN                           = 19
    SWIVEL_OUT                          = 20
    UNFOLD_FOOTREST                     = 21
    UNFOLDING                           = 22
    UNPACK                              = 23
    WAIT_FOR_CALL_REMOVAL               = 24
    MOVE_TO_PARKING                     = 25
    MOVE_TO_POINT_PARTIALLY_UNFOLDED    = 26
    CONTINUE_ATOMIC_MOVEMENT            = 27


@unique
class BreakReasons(EnumUtils, Enum):
    """
    Enum class containing all break reasons.
    """
    NO_BREAK                                    = 0
    CALL_REMOVED                                = 1
    FAULT_PRESENT                               = 2
    MAIN_FUSE_BLOWN                             = 3
    ULTIMATE_PRESSED                            = 4
    OSG_ACTIVATED                               = 5
    DIR_CHAIN_NOT_ENERGISED                     = 6
    # Everything below here is raised as a recoverable fault (reject reasons)
    REJECT_DIR_SAFETY_CHAIN_OPEN                = 7
    REJECT_BATTERY_VOLTAGE_INSUFFICIENT_RAIL    = 8
    REJECT_BATTERY_VOLTAGE_INSUFFICIENT_ALL     = 9
    REJECT_BISTABLE_DISABLES_MOVEMENT           = 10
    REJECT_KEY_REMOVED                          = 11
    REJECT_SEAT_NOT_LOADED                      = 12
    REJECT_SEATBELT_NOT_ENGAGED                 = 13
    REJECT_SWIVEL_NOT_CENTRED                   = 14
    REJECT_SWIVEL_NOT_LOCKED                    = 15
    REJECT_DRIVE_NOT_CALIBRATED                 = 16
    REJECT_SEAT_LOADED                          = 17
    REJECT_SEATBELT_ENGAGED                     = 18


@unique
class ChairDemands(EnumUtils, Enum):
    """
    Enum class containing the Chair demands.
    """
    NO_DEMAND            = 0
    FOLD                 = 1
    FULL_UNFOLD          = 2
    PARTIAL_UNFOLD       = 3
    CAL_RUN_TO_FOLD      = 4
    CAL_RUN_TO_UNFOLD    = 5


@unique
class FootrestDemands(EnumUtils, Enum):
    """
    Enum class containing the Footrest demands.
    """
    NO_DEMAND            = 0
    FOLD                 = 1
    UNFOLD               = 2
    CAL_RUN_TO_FOLD      = 3
    CAL_RUN_TO_UNFOLD    = 4


@unique
class MainDemands(EnumUtils, Enum):
    """
    Enum class containing the Main demands.
    """
    NO_DEMAND            = 0
    LEFT_TO_RAIL_POINT   = 1
    RIGHT_TO_RAIL_POINT  = 2
    LEFT_TO_BOARD_POINT  = 3
    RIGHT_TO_BOARD_POINT = 4
    DRIVE_LEFT           = 5
    DRIVE_RIGHT          = 6
    CAL_DRIVE_LEFT       = 7
    CAL_DRIVE_RIGHT      = 8
    CREEP_TO_CHARGE_L    = 9
    CREEP_TO_CHARGE_R    = 10


@unique
class SwivelDemands(EnumUtils, Enum):
    """
    Enum class containing the Swivel demands.
    """
    NO_DEMAND            = 0
    SWIVEL_OUT_LEFT      = 1
    SWIVEL_OUT_RIGHT     = 2
    SWIVEL_IN            = 3
    CAL_SWIVEL_TO_LEFT   = 4
    CAL_SWIVEL_TO_RIGHT  = 5