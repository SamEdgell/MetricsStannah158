# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class ADCX04(EnumUtils, Enum):
    """
    Enum class containing all the ADC channels for X04.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each ADC channel for ECU1.
    """
    ADC_CARRIAGE_BUS_VFB                = 0
    ADC_CARRIAGE_LH_FET_VFB             = 1
    ADC_CARRIAGE_RH_FET_VFB             = 2
    ADC_CARRIAGE_IFB                    = 3
    ADC_FOOTREST_BUS_VFB                = 4
    ADC_FOOTREST_LH_FET_VFB             = 5
    ADC_FOOTREST_RH_FET_VFB             = 6
    ADC_FOOTREST_IFB                    = 7
    ADC_ANA_BAT_2S_SENSE                = 8
    ADC_ANA_BAT_1S_SENSE                = 9
    ADC_ANA_VIN_SENSE                   = 10
    ADC_ANA_LFR_MON                     = 11
    ADC_ANA_RFR_MON                     = 12


@unique
class ADCX01(EnumUtils, Enum):
    """
    Enum class containing all the ADC channels for X01.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each ADC channel for ECU2.
    """
    ADC_SEATLOAD_MON                    = 0
    ADC_FOLD_RH_FET_VFB                 = 1
    ADC_FOLD_LH_FET_VFB                 = 2
    ADC_FOLD_IFB                        = 3
    ADC_FOLD_BUS_VBF                    = 4
    ADC_SWIVEL_IFB                      = 5
    ADC_SWIVEL_RH_FET_VFB               = 6
    ADC_SWIVEL_LH_FET_VFB               = 7
    ADC_SWIVEL_BUS_VBF                  = 8