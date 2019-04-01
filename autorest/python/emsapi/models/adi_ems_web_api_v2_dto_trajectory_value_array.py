# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoTrajectoryValueArray(Model):
    """Encapsulates the data returned when requesting trajectory values through
    the API.

    :param values: The points in the generated trajectory.
    :type values: list[~emsapi.models.AdiEmsWebApiV2DtoTrajectoryValue]
    """

    _attribute_map = {
        'values': {'key': 'values', 'type': '[AdiEmsWebApiV2DtoTrajectoryValue]'},
    }

    def __init__(self, values=None):
        super(AdiEmsWebApiV2DtoTrajectoryValueArray, self).__init__()
        self.values = values
