# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoEmsProfileProfileResultsEventRecord(Model):
    """Encapsulates information about an event result stored in the database.

    :param record_number: The unique id of the event in the database
    :type record_number: int
    :param event_type: The unique id of the event definition that generated
     this event
    :type event_type: int
    :param phase_of_flight: The phase of flight where the event occurred (a
     value from the EMS POF list)
    :type phase_of_flight: int
    :param severity: The event severity (a value from the EMS Severity list)
    :type severity: int
    :param status: The status of the event (a value from the EMS Status list).
     Typically this is defaulted to
     0 for new events, but in some data-merge scenarios we need to import a
     non-default value
     from a remote system
    :type status: int
    :param false_positive: The false positive value for the event (a value
     from the EMS False Positive list).
     Typically this is defaulted to 0 for new events, but in some data-merge
     scenarios we
     need to import a non-default value from a remote system
    :type false_positive: int
    :param start_time: The starting offset for the event
    :type start_time: float
    :param end_time: The ending offset for the event
    :type end_time: float
    :param global_measurements: The global event measurements (defined for all
     events)
    :type global_measurements:
     list[~emsapi.models.AdiEmsWebApiV2DtoEmsProfileProfileResultValue]
    :param global_timepoints: The global event timepoints (defined for all
     events)
    :type global_timepoints:
     list[~emsapi.models.AdiEmsWebApiV2DtoEmsProfileProfileResultValue]
    :param local_measurements: The event-specific measurements (different for
     each event type)
    :type local_measurements:
     list[~emsapi.models.AdiEmsWebApiV2DtoEmsProfileProfileResultValue]
    :param local_timepoints: The event-specific timepoints (different for each
     event type)
    :type local_timepoints:
     list[~emsapi.models.AdiEmsWebApiV2DtoEmsProfileProfileResultValue]
    :param comments: The event comments. Usually this is empty, but it's
     required for some data-merge
     scenarios.
    :type comments:
     list[~emsapi.models.AdiEmsWebApiV2DtoEmsProfileProfileResultComment]
    """

    _validation = {
        'record_number': {'required': True},
        'event_type': {'required': True},
        'phase_of_flight': {'required': True},
        'severity': {'required': True},
        'status': {'required': True},
        'false_positive': {'required': True},
        'start_time': {'required': True},
        'end_time': {'required': True},
        'global_measurements': {'required': True},
        'global_timepoints': {'required': True},
        'local_measurements': {'required': True},
        'local_timepoints': {'required': True},
        'comments': {'required': True},
    }

    _attribute_map = {
        'record_number': {'key': 'recordNumber', 'type': 'int'},
        'event_type': {'key': 'eventType', 'type': 'int'},
        'phase_of_flight': {'key': 'phaseOfFlight', 'type': 'int'},
        'severity': {'key': 'severity', 'type': 'int'},
        'status': {'key': 'status', 'type': 'int'},
        'false_positive': {'key': 'falsePositive', 'type': 'int'},
        'start_time': {'key': 'startTime', 'type': 'float'},
        'end_time': {'key': 'endTime', 'type': 'float'},
        'global_measurements': {'key': 'globalMeasurements', 'type': '[AdiEmsWebApiV2DtoEmsProfileProfileResultValue]'},
        'global_timepoints': {'key': 'globalTimepoints', 'type': '[AdiEmsWebApiV2DtoEmsProfileProfileResultValue]'},
        'local_measurements': {'key': 'localMeasurements', 'type': '[AdiEmsWebApiV2DtoEmsProfileProfileResultValue]'},
        'local_timepoints': {'key': 'localTimepoints', 'type': '[AdiEmsWebApiV2DtoEmsProfileProfileResultValue]'},
        'comments': {'key': 'comments', 'type': '[AdiEmsWebApiV2DtoEmsProfileProfileResultComment]'},
    }

    def __init__(self, record_number, event_type, phase_of_flight, severity, status, false_positive, start_time, end_time, global_measurements, global_timepoints, local_measurements, local_timepoints, comments):
        super(AdiEmsWebApiV2DtoEmsProfileProfileResultsEventRecord, self).__init__()
        self.record_number = record_number
        self.event_type = event_type
        self.phase_of_flight = phase_of_flight
        self.severity = severity
        self.status = status
        self.false_positive = false_positive
        self.start_time = start_time
        self.end_time = end_time
        self.global_measurements = global_measurements
        self.global_timepoints = global_timepoints
        self.local_measurements = local_measurements
        self.local_timepoints = local_timepoints
        self.comments = comments
