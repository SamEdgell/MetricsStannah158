from enum import Enum, unique
from Enums.enum_utils import EnumUtils


@unique
class ADCECU1(EnumUtils, Enum):
    """
    Enum class containing all the ADC channels for ECU1.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each ADC channel for ECU1.
    """
    ADC_CHANNEL_1                = 0
    ADC_CHANNEL_2                = 1
    ADC_CHANNEL_3                = 2
    ADC_CHANNEL_4                = 3
    ADC_CHANNEL_5                = 4
    ADC_CHANNEL_6                = 5
    ADC_CHANNEL_7                = 6
    ADC_CHANNEL_8                = 7
    ADC_CHANNEL_9                = 8
    ADC_CHANNEL_10               = 9


@unique
class ADCECU2(EnumUtils, Enum):
    """
    Enum class containing all the ADC channels for ECU2.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each ADC channel for ECU2.
    """
    ADC_CHANNEL_1                = 0
    ADC_CHANNEL_2                = 1
    ADC_CHANNEL_3                = 2
    ADC_CHANNEL_4                = 3
    ADC_CHANNEL_5                = 4
    ADC_CHANNEL_6                = 5
    ADC_CHANNEL_7                = 6
    ADC_CHANNEL_8                = 7
    ADC_CHANNEL_9                = 8
    ADC_CHANNEL_10               = 9