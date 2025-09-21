# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class MetricSubcodes(EnumUtils, Enum):
    """
    Enum class to define the metric subcodes.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants.
    The enum values are used as indices for the METRIC_SUBCODE_MAPPER dictionary.
    """
    METRIC_INVALID                          = 0x0000