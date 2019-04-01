# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class TransferOperations(object):
    """TransferOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def start_async(
            self, ems_system_id, request, custom_headers=None, raw=False, **operation_config):
        """Starts a new upload.

        :param ems_system_id: The ID of the EMS system on which to start a new
         upload.
        :type ems_system_id: int
        :param request: Information about the upload to start.
        :type request: ~emsapi.models.AdiEmsWebApiV2DtoUploadUploadRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.start_async.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(request, 'AdiEmsWebApiV2DtoUploadUploadRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 401, 500, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdiEmsWebApiV2DtoUploadUploadParameters', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 500:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    start_async.metadata = {'url': '/v2/ems-systems/{emsSystemId}/uploads'}

    def chunk_async(
            self, ems_system_id, transfer_id, first, last, custom_headers=None, raw=False, **operation_config):
        """Uploads a chunk of a file. This will fail if any chunks have been
        skipped in the specified file.

        The practical limit for a single chunk is less than 4MB or so,
        dependent on the web server's configuration.
        If you receive 500 responses, try smaller chunk sizes.

        :param ems_system_id: The ID of the EMS system to which the client is
         uploading.
        :type ems_system_id: int
        :param transfer_id: The ID of the upload, returned originally by the
         upload start call.
        :type transfer_id: str
        :param first: The byte index of the first byte that will be uploaded.
        :type first: long
        :param last: The byte index of the last byte that will be uploaded.
        :type last: long
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.chunk_async.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int'),
            'transferId': self._serialize.url("transfer_id", transfer_id, 'str'),
            'first': self._serialize.url("first", first, 'long'),
            'last': self._serialize.url("last", last, 'long')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 401, 404, 500, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdiEmsWebApiV2DtoUploadUploadResult', response)
        if response.status_code == 400:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 404:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 500:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    chunk_async.metadata = {'url': '/v2/ems-systems/{emsSystemId}/uploads/{transferId}/{first}/{last}'}

    def status(
            self, ems_system_id, transfer_id, custom_headers=None, raw=False, **operation_config):
        """Gets the status of an upload in progress.

        :param ems_system_id: The ID of the EMS system to which the client is
         uploading.
        :type ems_system_id: int
        :param transfer_id: The ID of the upload, returned originally by the
         upload start call.
        :type transfer_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.status.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int'),
            'transferId': self._serialize.url("transfer_id", transfer_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 401, 404, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdiEmsWebApiV2DtoUploadUploadStatus', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 404:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    status.metadata = {'url': '/v2/ems-systems/{emsSystemId}/uploads/{transferId}'}

    def finish_async(
            self, ems_system_id, transfer_id, custom_headers=None, raw=False, **operation_config):
        """Completes an existing upload in progress.

        <p>This will examine everything that's been transferred to make sure
        that it is intact, then
        give a status report in response.</p>
        <p>The use of this call is not required unless the file is being
        streamed (i.e. there was no
        totalSize passed in the beginning of the file). In that case, this call
        is necessary to
        tell the server that all data are received.</p>.

        :param ems_system_id: The ID of the EMS system to which the client is
         uploading.
        :type ems_system_id: int
        :param transfer_id: The ID of the upload, returned originally by the
         upload start call.
        :type transfer_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.finish_async.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int'),
            'transferId': self._serialize.url("transfer_id", transfer_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 401, 404, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdiEmsWebApiV2DtoUploadUploadResult', response)
        if response.status_code == 400:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 404:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    finish_async.metadata = {'url': '/v2/ems-systems/{emsSystemId}/uploads/{transferId}/finish'}

    def cancel_async(
            self, ems_system_id, transfer_id, custom_headers=None, raw=False, **operation_config):
        """Cancels an existing upload in progress.

        If successful, this call will delete the file in progress and set the
        associated database record to canceled.

        :param ems_system_id: The ID of the EMS system to which the client is
         uploading.
        :type ems_system_id: int
        :param transfer_id: The ID of the upload, returned originally by the
         upload start call.
        :type transfer_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.cancel_async.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int'),
            'transferId': self._serialize.url("transfer_id", transfer_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 401, 404, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdiEmsWebApiV2DtoUploadUploadResult', response)
        if response.status_code == 400:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 404:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    cancel_async.metadata = {'url': '/v2/ems-systems/{emsSystemId}/uploads/{transferId}/cancel'}

    def get_uploads(
            self, max_entries=None, custom_headers=None, raw=False, **operation_config):
        """Get a list of upload records from the server.

        For administrative users, this will return a list of all uploads;
        otherwise only the uploads associated
        to the current user will be returned.

        :param max_entries: The maximum number of entries to return; this is
         capped at 50, and
         50 will be used if it's not specified.
        :type max_entries: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_uploads.metadata['url']

        # Construct parameters
        query_parameters = {}
        if max_entries is not None:
            query_parameters['maxEntries'] = self._serialize.query("max_entries", max_entries, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 401, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[AdiEmsWebApiV2DtoUploadUploadRecord]', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_uploads.metadata = {'url': '/v2/uploads'}

    def get_upload_processing_status(
            self, ems_system_id, transfer_id, custom_headers=None, raw=False, **operation_config):
        """Gets the EMS processing status for a single upload.

        When using this route, make sure to use EMS system and upload IDs that
        match. Results for IDs that do not
        exist will still return valid results, but will indicate that the
        uploading processing is incomplete,
        which, while true, may be misleading.

        :param ems_system_id: The ID of the EMS server to query for the
         specified uploads.
        :type ems_system_id: int
        :param transfer_id: The ID of the upload for which to return status
         information.
        :type transfer_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_upload_processing_status.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int'),
            'transferId': self._serialize.url("transfer_id", transfer_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 401, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdiEmsWebApiV2DtoUploadUploadProcessingStatus', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_upload_processing_status.metadata = {'url': '/v2/ems-systems/{emsSystemId}/uploads/processing-status/{transferId}'}

    def get_upload_processing_status_multiple(
            self, ems_system_id, ids, custom_headers=None, raw=False, **operation_config):
        """Gets the EMS processing status for a set of uploads.

        When using this route, make sure to use EMS system and upload IDs that
        match. Results for IDs that do not
        exist will still return valid results, but will indicate that the
        uploading processing is incomplete,
        which, while true, may be misleading.

        :param ems_system_id: The ID of the EMS server to query for the
         specified uploads.
        :type ems_system_id: int
        :param ids: The list of IDs of the upload for which to return status
         information.
        :type ids: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_upload_processing_status_multiple.metadata['url']
        path_format_arguments = {
            'emsSystemId': self._serialize.url("ems_system_id", ems_system_id, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(ids, '[str]')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 401, 503]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('{AdiEmsWebApiV2DtoUploadUploadProcessingStatus}', response)
        if response.status_code == 400:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 401:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)
        if response.status_code == 503:
            deserialized = self._deserialize('AdiEmsWebApiModelError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_upload_processing_status_multiple.metadata = {'url': '/v2/ems-systems/{emsSystemId}/uploads/processing-status'}
