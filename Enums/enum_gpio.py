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
    INPUT_ID_4             = 3
    INPUT_ID_5             = 4
    INPUT_ID_6             = 5
    INPUT_ID_7             = 6
    INPUT_ID_8             = 7
    INPUT_ID_9             = 8
    INPUT_ID_10            = 9
    INPUT_ID_11            = 10
    INPUT_ID_12            = 11
    INPUT_ID_13            = 12
    INPUT_ID_14            = 13
    INPUT_ID_15            = 14
    INPUT_ID_16            = 15


@unique
class InputsECU2(EnumUtils, Enum):
    """
    Enum class containing all the inputs for ECU2.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each input for ECU2.
    """
    INPUT_ID_1             = 0
    INPUT_ID_2             = 1
    INPUT_ID_3             = 2
    INPUT_ID_4             = 3
    INPUT_ID_5             = 4
    INPUT_ID_6             = 5
    INPUT_ID_7             = 6
    INPUT_ID_8             = 7
    INPUT_ID_9             = 8
    INPUT_ID_10            = 9
    INPUT_ID_11            = 10
    INPUT_ID_12            = 11
    INPUT_ID_13            = 12
    INPUT_ID_14            = 13
    INPUT_ID_15            = 14
    INPUT_ID_16            = 15


@unique
class OutputsECU1(EnumUtils, Enum):
    """
    Enum class containing all the outputs for ECU1.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each output for ECU1.
    """
    OUTPUT_ID_1            = 0
    OUTPUT_ID_2            = 1
    OUTPUT_ID_3            = 2
    OUTPUT_ID_4            = 3
    OUTPUT_ID_5            = 4
    OUTPUT_ID_6            = 5
    OUTPUT_ID_7            = 6
    OUTPUT_ID_8            = 7


@unique
class OutputsECU2(EnumUtils, Enum):
    """
    Enum class containing all the outputs for ECU2.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each output for ECU2.
    """
    OUTPUT_ID_1            = 0
    OUTPUT_ID_2            = 1
    OUTPUT_ID_3            = 2
    OUTPUT_ID_4            = 3
    OUTPUT_ID_5            = 4
    OUTPUT_ID_6            = 5
    OUTPUT_ID_7            = 6
    OUTPUT_ID_8            = 7


@unique
class LogicState(EnumUtils, Enum):
    """
    Enum class containing logic state details.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing logic states.
    """
    LOGIC_0                = 0
    LOGIC_1                = 1