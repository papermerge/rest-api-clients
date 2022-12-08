# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from papermerge_restapi_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from papermerge_restapi_client import schemas  # noqa: F401

from . import path

# query params


class ArchiveTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        min_length = 1
        enum_value_to_name = {
            "targz": "TARGZ",
            "zip": "ZIP",
        }
    
    @schemas.classproperty
    def TARGZ(cls):
        return cls("targz")
    
    @schemas.classproperty
    def ZIP(cls):
        return cls("zip")


class FileNameSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 32
        min_length = 1


class FormatSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "json": "JSON",
            "vnd.api+json": "VND_APIJSON",
        }
    
    @schemas.classproperty
    def JSON(cls):
        return cls("json")
    
    @schemas.classproperty
    def VND_APIJSON(cls):
        return cls("vnd.api+json")


class IncludeVersionSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        min_length = 1
        enum_value_to_name = {
            "only_original": "ORIGINAL",
            "only_last": "LAST",
        }
    
    @schemas.classproperty
    def ORIGINAL(cls):
        return cls("only_original")
    
    @schemas.classproperty
    def LAST(cls):
        return cls("only_last")


class NodeIdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.UUIDSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, uuid.UUID, ]], typing.List[typing.Union[MetaOapg.items, str, uuid.UUID, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'NodeIdsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'node_ids': typing.Union[NodeIdsSchema, list, tuple, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'archive_type': typing.Union[ArchiveTypeSchema, str, ],
        'file_name': typing.Union[FileNameSchema, str, ],
        'format': typing.Union[FormatSchema, str, ],
        'include_version': typing.Union[IncludeVersionSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_archive_type = api_client.QueryParameter(
    name="archive_type",
    style=api_client.ParameterStyle.FORM,
    schema=ArchiveTypeSchema,
    explode=True,
)
request_query_file_name = api_client.QueryParameter(
    name="file_name",
    style=api_client.ParameterStyle.FORM,
    schema=FileNameSchema,
    explode=True,
)
request_query_format = api_client.QueryParameter(
    name="format",
    style=api_client.ParameterStyle.FORM,
    schema=FormatSchema,
    explode=True,
)
request_query_include_version = api_client.QueryParameter(
    name="include_version",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeVersionSchema,
    explode=True,
)
request_query_node_ids = api_client.QueryParameter(
    name="node_ids",
    style=api_client.ParameterStyle.FORM,
    schema=NodeIdsSchema,
    required=True,
    explode=True,
)
_auth = [
    'Token Authentication',
]
SchemaFor200ResponseBodyApplicationPdf = schemas.BinarySchema
SchemaFor200ResponseBodyApplicationZip = schemas.BinarySchema
SchemaFor200ResponseBodyApplicationXGtar = schemas.BinarySchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationPdf,
        SchemaFor200ResponseBodyApplicationZip,
        SchemaFor200ResponseBodyApplicationXGtar,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/pdf': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationPdf),
        'application/zip': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationZip),
        'application/x-gtar': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationXGtar),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/pdf',
    'application/zip',
    'application/x-gtar',
)


class BaseApi(api_client.Api):

    def _nodes_download_oapg(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_archive_type,
            request_query_file_name,
            request_query_format,
            request_query_include_version,
            request_query_node_ids,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class NodesDownload(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def nodes_download(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._nodes_download_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def get(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._nodes_download_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


