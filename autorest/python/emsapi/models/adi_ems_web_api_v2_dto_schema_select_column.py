# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoSchemaSelectColumn(Model):
    """Represents a column of data that can be selected in a data source query.

    :param field_id: The unique string identifier of the field to select in a
     query
    :type field_id: str
    :param aggregate: An optional aggregate operation to perform on the
     column. Omission of this property results in no aggregate
     operation being performed. Possible values include: 'none', 'avg',
     'count', 'max', 'min', 'stdev', 'sum', 'var'
    :type aggregate: str or ~emsapi.models.enum
    :param format: Value formatting that should be performed on this field's
     value before returning.
     This will override the query's display value. Possible values include:
     'none', 'display'
    :type format: str or ~emsapi.models.enum
    """

    _validation = {
        'field_id': {'required': True},
    }

    _attribute_map = {
        'field_id': {'key': 'fieldId', 'type': 'str'},
        'aggregate': {'key': 'aggregate', 'type': 'str'},
        'format': {'key': 'format', 'type': 'str'},
    }

    def __init__(self, field_id, aggregate=None, format=None):
        super(AdiEmsWebApiV2DtoSchemaSelectColumn, self).__init__()
        self.field_id = field_id
        self.aggregate = aggregate
        self.format = format
