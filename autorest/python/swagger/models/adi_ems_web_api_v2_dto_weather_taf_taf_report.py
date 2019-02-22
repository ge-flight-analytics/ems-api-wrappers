# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoWeatherTafTafReport(Model):
    """Represents an individual TAF report.

    :param parse_errors: Error messages delimited by newlines if there were
     non-critical issues parsing the raw TAF string
    :type parse_errors: str
    :param issued: The time point that this TAF report was issued
    :type issued: datetime
    :param airport: The airport that issued the TAF report
    :type airport: str
    :param valid_from: The starting time point that this TAF report is valid
    :type valid_from: datetime
    :param valid_to: The ending time point that this TAF report is valid
    :type valid_to: datetime
    :param predictions: A list of forecast predictions in the TAF
    :type predictions:
     list[~swagger.models.AdiEmsWebApiV2DtoWeatherTafPrediction]
    :param header_text: The header text for the TAF
    :type header_text: str
    :param flight_match_type: The time and place relative to a specific flight
     that this forecast data would match to. Possible values include: 'none',
     'takeoffAtDispatch', 'landingAtDispatch', 'alternateAtDispatch',
     'landingAtTakeoff', 'alternateAtTakeoff', 'alternateAtLanding'
    :type flight_match_type: str or ~swagger.models.enum
    :param matched_prediction: The forecast data that matches to a specific
     flight
    :type matched_prediction:
     ~swagger.models.AdiEmsWebApiV2DtoWeatherTafPrediction
    """

    _validation = {
        'issued': {'required': True},
        'airport': {'required': True},
        'valid_from': {'required': True},
        'valid_to': {'required': True},
        'header_text': {'required': True},
    }

    _attribute_map = {
        'parse_errors': {'key': 'parseErrors', 'type': 'str'},
        'issued': {'key': 'issued', 'type': 'iso-8601'},
        'airport': {'key': 'airport', 'type': 'str'},
        'valid_from': {'key': 'validFrom', 'type': 'iso-8601'},
        'valid_to': {'key': 'validTo', 'type': 'iso-8601'},
        'predictions': {'key': 'predictions', 'type': '[AdiEmsWebApiV2DtoWeatherTafPrediction]'},
        'header_text': {'key': 'headerText', 'type': 'str'},
        'flight_match_type': {'key': 'flightMatchType', 'type': 'str'},
        'matched_prediction': {'key': 'matchedPrediction', 'type': 'AdiEmsWebApiV2DtoWeatherTafPrediction'},
    }

    def __init__(self, issued, airport, valid_from, valid_to, header_text, parse_errors=None, predictions=None, flight_match_type=None, matched_prediction=None):
        super(AdiEmsWebApiV2DtoWeatherTafTafReport, self).__init__()
        self.parse_errors = parse_errors
        self.issued = issued
        self.airport = airport
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.predictions = predictions
        self.header_text = header_text
        self.flight_match_type = flight_match_type
        self.matched_prediction = matched_prediction
