# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b36
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


class Page(
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
            def type() -> typing.Type['PageTypeEnum']:
                return PageTypeEnum
            id = schemas.UUIDSchema
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        id = schemas.UUIDSchema
                        number = schemas.IntSchema
                        text = schemas.StrSchema
                        
                        
                        class lang(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 8
                        svg_url = schemas.StrSchema
                        jpg_url = schemas.StrSchema
                        __annotations__ = {
                            "id": id,
                            "number": number,
                            "text": text,
                            "lang": lang,
                            "svg_url": svg_url,
                            "jpg_url": jpg_url,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["lang"]) -> MetaOapg.properties.lang: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["svg_url"]) -> MetaOapg.properties.svg_url: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["jpg_url"]) -> MetaOapg.properties.jpg_url: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "number", "text", "lang", "svg_url", "jpg_url", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> typing.Union[MetaOapg.properties.number, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union[MetaOapg.properties.text, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["lang"]) -> typing.Union[MetaOapg.properties.lang, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["svg_url"]) -> typing.Union[MetaOapg.properties.svg_url, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["jpg_url"]) -> typing.Union[MetaOapg.properties.jpg_url, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "number", "text", "lang", "svg_url", "jpg_url", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
                    number: typing.Union[MetaOapg.properties.number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    text: typing.Union[MetaOapg.properties.text, str, schemas.Unset] = schemas.unset,
                    lang: typing.Union[MetaOapg.properties.lang, str, schemas.Unset] = schemas.unset,
                    svg_url: typing.Union[MetaOapg.properties.svg_url, str, schemas.Unset] = schemas.unset,
                    jpg_url: typing.Union[MetaOapg.properties.jpg_url, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *args,
                        id=id,
                        number=number,
                        text=text,
                        lang=lang,
                        svg_url=svg_url,
                        jpg_url=jpg_url,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class relationships(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                    
                        @staticmethod
                        def document_version() -> typing.Type['Reltoone']:
                            return Reltoone
                        __annotations__ = {
                            "document_version": document_version,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["document_version"]) -> 'Reltoone': ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["document_version", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["document_version"]) -> typing.Union['Reltoone', schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["document_version", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    document_version: typing.Union['Reltoone', schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'relationships':
                    return super().__new__(
                        cls,
                        *args,
                        document_version=document_version,
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
    
    type: 'PageTypeEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'PageTypeEnum': ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'PageTypeEnum': ...
    
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
        type: 'PageTypeEnum',
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        relationships: typing.Union[MetaOapg.properties.relationships, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'Page':
        return super().__new__(
            cls,
            *args,
            type=type,
            id=id,
            attributes=attributes,
            relationships=relationships,
            _configuration=_configuration,
        )

from papermerge_restapi_client.model.page_type_enum import PageTypeEnum
from papermerge_restapi_client.model.reltoone import Reltoone
