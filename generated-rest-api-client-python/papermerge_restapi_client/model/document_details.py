# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b34
    Generated by: https://openapi-generator.tech
"""

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


class DocumentDetails(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
        
            @staticmethod
            def type() -> typing.Type['DocumentDetailsTypeEnum']:
                return DocumentDetailsTypeEnum
            id = schemas.UUIDSchema
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "title",
                    }
                    
                    class properties:
                        id = schemas.UUIDSchema
                        
                        
                        class title(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 200
                        
                        
                        class lang(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 8
                        ocr = schemas.BoolSchema
                        
                        
                        class ocr_status(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                enum_value_to_name = {
                                    "unknown": "UNKNOWN",
                                    "received": "RECEIVED",
                                    "started": "STARTED",
                                    "succeeded": "SUCCEEDED",
                                    "failed": "FAILED",
                                }
                            
                            @schemas.classproperty
                            def UNKNOWN(cls):
                                return cls("unknown")
                            
                            @schemas.classproperty
                            def RECEIVED(cls):
                                return cls("received")
                            
                            @schemas.classproperty
                            def STARTED(cls):
                                return cls("started")
                            
                            @schemas.classproperty
                            def SUCCEEDED(cls):
                                return cls("succeeded")
                            
                            @schemas.classproperty
                            def FAILED(cls):
                                return cls("failed")
                        
                        
                        class versions(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['DocumentVersion']:
                                    return DocumentVersion
                        
                            def __new__(
                                cls,
                                arg: typing.Union[typing.Tuple['DocumentVersion'], typing.List['DocumentVersion']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'versions':
                                return super().__new__(
                                    cls,
                                    arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'DocumentVersion':
                                return super().__getitem__(i)
                        created_at = schemas.DateTimeSchema
                        updated_at = schemas.DateTimeSchema
                        __annotations__ = {
                            "id": id,
                            "title": title,
                            "lang": lang,
                            "ocr": ocr,
                            "ocr_status": ocr_status,
                            "versions": versions,
                            "created_at": created_at,
                            "updated_at": updated_at,
                        }
                
                title: MetaOapg.properties.title
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["lang"]) -> MetaOapg.properties.lang: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["ocr"]) -> MetaOapg.properties.ocr: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["ocr_status"]) -> MetaOapg.properties.ocr_status: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["versions"]) -> MetaOapg.properties.versions: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "title", "lang", "ocr", "ocr_status", "versions", "created_at", "updated_at", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["lang"]) -> typing.Union[MetaOapg.properties.lang, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["ocr"]) -> typing.Union[MetaOapg.properties.ocr, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["ocr_status"]) -> typing.Union[MetaOapg.properties.ocr_status, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["versions"]) -> typing.Union[MetaOapg.properties.versions, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "title", "lang", "ocr", "ocr_status", "versions", "created_at", "updated_at", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    title: typing.Union[MetaOapg.properties.title, str, ],
                    id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
                    lang: typing.Union[MetaOapg.properties.lang, str, schemas.Unset] = schemas.unset,
                    ocr: typing.Union[MetaOapg.properties.ocr, bool, schemas.Unset] = schemas.unset,
                    ocr_status: typing.Union[MetaOapg.properties.ocr_status, str, schemas.Unset] = schemas.unset,
                    versions: typing.Union[MetaOapg.properties.versions, list, tuple, schemas.Unset] = schemas.unset,
                    created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
                    updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *args,
                        title=title,
                        id=id,
                        lang=lang,
                        ocr=ocr,
                        ocr_status=ocr_status,
                        versions=versions,
                        created_at=created_at,
                        updated_at=updated_at,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class relationships(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                    
                        @staticmethod
                        def parent() -> typing.Type['Reltoone']:
                            return Reltoone
                        __annotations__ = {
                            "parent": parent,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["parent"]) -> 'Reltoone': ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["parent", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> typing.Union['Reltoone', schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["parent", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    parent: typing.Union['Reltoone', schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'relationships':
                    return super().__new__(
                        cls,
                        *args,
                        parent=parent,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "type": type,
                "id": id,
                "attributes": attributes,
                "relationships": relationships,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    type: 'DocumentDetailsTypeEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'DocumentDetailsTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationships"]) -> MetaOapg.properties.relationships: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type"], typing_extensions.Literal["id"], typing_extensions.Literal["attributes"], typing_extensions.Literal["relationships"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'DocumentDetailsTypeEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> typing.Union[MetaOapg.properties.attributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationships"]) -> typing.Union[MetaOapg.properties.relationships, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type"], typing_extensions.Literal["id"], typing_extensions.Literal["attributes"], typing_extensions.Literal["relationships"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: 'DocumentDetailsTypeEnum',
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        relationships: typing.Union[MetaOapg.properties.relationships, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DocumentDetails':
        return super().__new__(
            cls,
            *args,
            type=type,
            id=id,
            attributes=attributes,
            relationships=relationships,
            _configuration=_configuration,
        )

from papermerge_restapi_client.model.document_details_type_enum import DocumentDetailsTypeEnum
from papermerge_restapi_client.model.document_version import DocumentVersion
from papermerge_restapi_client.model.reltoone import Reltoone
