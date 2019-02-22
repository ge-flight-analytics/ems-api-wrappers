# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoSchemaAsyncQueryData(Model):
    """Represents the tabular results of a data source query obtained from an
    async query.

    :param rows: An array of JSON string arrays, where each entry is a row in
     the results set
    :type rows: list[str]
    :param has_more_rows: Whether the query has one or more rows in its result
     set at an index greater than the last row returned
    :type has_more_rows: bool
    """

    _validation = {
        'rows': {'required': True},
        'has_more_rows': {'required': True},
    }

    _attribute_map = {
        'rows': {'key': 'rows', 'type': '[str]'},
        'has_more_rows': {'key': 'hasMoreRows', 'type': 'bool'},
    }

    def __init__(self, rows, has_more_rows):
        super(AdiEmsWebApiV2DtoSchemaAsyncQueryData, self).__init__()
        self.rows = rows
        self.has_more_rows = has_more_rows
