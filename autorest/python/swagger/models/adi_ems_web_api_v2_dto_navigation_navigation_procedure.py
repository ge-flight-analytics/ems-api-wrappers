# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoNavigationNavigationProcedure(Model):
    """Various pieces of information associated with a procedure.

    :param id: The unique identiifer for this procedure.
    :type id: int
    :param cycle_date: A text value representing the cycle date of the
     procedure.
    :type cycle_date: str
    :param emergency_safe_altitude: The emergency safe altitude of the
     procedure.
    :type emergency_safe_altitude: float
    :param string: A text identifier of the procedure.
    :type string: str
    :param transitional_altitude: The transition altitude of the procedure.
    :type transitional_altitude: float
    :param transitional_level: The transition level of the procedure.
    :type transitional_level: float
    :param type: The type of the procedure.
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'cycle_date': {'key': 'cycleDate', 'type': 'str'},
        'emergency_safe_altitude': {'key': 'emergencySafeAltitude', 'type': 'float'},
        'string': {'key': 'string', 'type': 'str'},
        'transitional_altitude': {'key': 'transitionalAltitude', 'type': 'float'},
        'transitional_level': {'key': 'transitionalLevel', 'type': 'float'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, id=None, cycle_date=None, emergency_safe_altitude=None, string=None, transitional_altitude=None, transitional_level=None, type=None):
        super(AdiEmsWebApiV2DtoNavigationNavigationProcedure, self).__init__()
        self.id = id
        self.cycle_date = cycle_date
        self.emergency_safe_altitude = emergency_safe_altitude
        self.string = string
        self.transitional_altitude = transitional_altitude
        self.transitional_level = transitional_level
        self.type = type
