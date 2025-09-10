class EnumUtils:
    """
    Utility class providing common helper methods for working with Enum classes.

    This class includes methods to:
    - Check if a name or value exists in the enum.
    - Retrieve an enum member by its value.
    - Retrieve the name of an enum member by its value.

    These utilities make enum checks and lookups more convenient and consistent.
    """

    @classmethod
    def doesNameExist(cls, name):
        """
        Checks if the name exists in the enum.

        Args:
            cls:    The class to check.
            name:   The name to check.
        """
        return name in cls._member_map_


    @classmethod
    def doesValueExist(cls, value):
        """
        Checks if the value exists in the enum.

        Args:
            cls:    The class to check.
            value:  The value to check.
        """
        return value in cls._value2member_map_


    @classmethod
    def getMember(cls, value):
        """
        Gets the enum member based on the value.

        Args:
            cls:    The class to check.
            value:  The value to check.
        """
        return cls._value2member_map_.get(value)


    @classmethod
    def getName(cls, value):
        """
        Gets the enum member name based on the value.

        Args:
            cls:    The class to check.
            value:  The value to check.
        """
        member = cls._value2member_map_.get(value)
        return member.name if member else None