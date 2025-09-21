from enum import Enum, unique
from Enums.enum_utils import EnumUtils


@unique
class InputsECU1(EnumUtils, Enum):
    """
    Enum class containing all the inputs for ECU1.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each input for ECU1.
    """
    INPUT_ID_1             = 0
    INPUT_ID_2             = 1
    INPUT_ID_3             = 2


@unique
class InputsECU2(EnumUtils, Enum):
    """
    Enum class containing all the inputs for ECU2.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each input for ECU2.
    """
    INPUT_ID_1             = 0
    INPUT_ID_2             = 1
    INPUT_ID_3             = 2


@unique
class OutputsECU1(EnumUtils, Enum):
    """
    Enum class containing all the outputs for ECU1.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each output for ECU1.
    """
    OUTPUT_ID_1            = 0
    OUTPUT_ID_2            = 1
    OUTPUT_ID_3            = 2


@unique
class OutputsECU2(EnumUtils, Enum):
    """
    Enum class containing all the outputs for ECU2.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each output for ECU2.
    """
    OUTPUT_ID_1            = 0
    OUTPUT_ID_2            = 1
    OUTPUT_ID_3            = 2


@unique
class LogicState(EnumUtils, Enum):
    """
    Enum class containing logic state details.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing logic states.
    """
    LOGIC_0                = 0
    LOGIC_1                = 1