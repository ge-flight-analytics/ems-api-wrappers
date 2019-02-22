# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoWeatherMetarMetarQuery(Model):
    """Defines the options that can be used to query for METAR reports.

    :param airport_id: Optional airport ID for an airport returned by the
     Assets APIs. If set then ICAO code should not be set
    :type airport_id: int
    :param airport_icao: Optional airport ICAO code. If set then airportId
     should not be set
    :type airport_icao: str
    :param observation_range_from: Optional date range from filter. If set all
     METARs issued after this value will be returned
    :type observation_range_from: datetime
    :param observation_range_to: Optional date range to filter. If set all
     METARs issued before this value will be returned
    :type observation_range_to: datetime
    :param visibility_minimum: Optional value indicating the minimum observed
     visibility in miles
    :type visibility_minimum: float
    :param visibility_maximum: Optional value indicating the maximum observed
     visibility in miles
    :type visibility_maximum: float
    :param ceiling_minimum: Optional value indicating the minimum observed
     ceiling in feet
    :type ceiling_minimum: float
    :param ceiling_maximum: Optional value indicating the maximum observed
     ceiling in feet
    :type ceiling_maximum: float
    :param max_results: The maximum number of results to return. If set to 0
     all results will be returned. This defaults to 200
    :type max_results: int
    """

    _attribute_map = {
        'airport_id': {'key': 'airportId', 'type': 'int'},
        'airport_icao': {'key': 'airportIcao', 'type': 'str'},
        'observation_range_from': {'key': 'observationRangeFrom', 'type': 'iso-8601'},
        'observation_range_to': {'key': 'observationRangeTo', 'type': 'iso-8601'},
        'visibility_minimum': {'key': 'visibilityMinimum', 'type': 'float'},
        'visibility_maximum': {'key': 'visibilityMaximum', 'type': 'float'},
        'ceiling_minimum': {'key': 'ceilingMinimum', 'type': 'float'},
        'ceiling_maximum': {'key': 'ceilingMaximum', 'type': 'float'},
        'max_results': {'key': 'maxResults', 'type': 'int'},
    }

    def __init__(self, airport_id=None, airport_icao=None, observation_range_from=None, observation_range_to=None, visibility_minimum=None, visibility_maximum=None, ceiling_minimum=None, ceiling_maximum=None, max_results=None):
        super(AdiEmsWebApiV2DtoWeatherMetarMetarQuery, self).__init__()
        self.airport_id = airport_id
        self.airport_icao = airport_icao
        self.observation_range_from = observation_range_from
        self.observation_range_to = observation_range_to
        self.visibility_minimum = visibility_minimum
        self.visibility_maximum = visibility_maximum
        self.ceiling_minimum = ceiling_minimum
        self.ceiling_maximum = ceiling_maximum
        self.max_results = max_results
