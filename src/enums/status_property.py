from enum import Enum

class StatusProperty(Enum):
    """
    This class is used to limit the property status options that the user has.
    """
    PRE_VENTA = 3
    EN_VENTA = 4
    VENDIDO = 5