# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b12
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

from papermerge-restapi-client import schemas  # noqa: F401


class SearchResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A `Serializer` is a model-less serializer class with additional
support for JSON:API spec features.

As in JSON:API specification a type is always required you need to
make sure that you define `resource_name` in your `Meta` class
when deriving from this class.

Included Mixins:

* A mixin class to enable sparse fieldsets is included
* A mixin class to enable validation of included resources is included
    """


    class MetaOapg:
        required = {
            "highlight",
            "node_type",
            "breadcrumb",
            "user_id",
            "id",
            "title",
        }
        
        class properties:
            id = schemas.UUIDSchema
            title = schemas.StrSchema
            highlight = schemas.StrSchema
            
            
            class breadcrumb(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'breadcrumb':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def node_type() -> typing.Type['NodeTypeEnum']:
                return NodeTypeEnum
            user_id = schemas.UUIDSchema
            text = schemas.StrSchema
            items = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "title": title,
                "highlight": highlight,
                "breadcrumb": breadcrumb,
                "node_type": node_type,
                "user_id": user_id,
                "text": text,
                "items": items,
            }
    
    highlight: MetaOapg.properties.highlight
    node_type: 'NodeTypeEnum'
    breadcrumb: MetaOapg.properties.breadcrumb
    user_id: MetaOapg.properties.user_id
    id: MetaOapg.properties.id
    title: MetaOapg.properties.title
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["highlight"]) -> MetaOapg.properties.highlight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["breadcrumb"]) -> MetaOapg.properties.breadcrumb: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["node_type"]) -> 'NodeTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "title", "highlight", "breadcrumb", "node_type", "user_id", "text", "items", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["highlight"]) -> MetaOapg.properties.highlight: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["breadcrumb"]) -> MetaOapg.properties.breadcrumb: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["node_type"]) -> 'NodeTypeEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union[MetaOapg.properties.text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> typing.Union[MetaOapg.properties.items, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "title", "highlight", "breadcrumb", "node_type", "user_id", "text", "items", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        highlight: typing.Union[MetaOapg.properties.highlight, str, ],
        node_type: 'NodeTypeEnum',
        breadcrumb: typing.Union[MetaOapg.properties.breadcrumb, list, tuple, ],
        user_id: typing.Union[MetaOapg.properties.user_id, str, uuid.UUID, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        text: typing.Union[MetaOapg.properties.text, str, schemas.Unset] = schemas.unset,
        items: typing.Union[MetaOapg.properties.items, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SearchResult':
        return super().__new__(
            cls,
            *args,
            highlight=highlight,
            node_type=node_type,
            breadcrumb=breadcrumb,
            user_id=user_id,
            id=id,
            title=title,
            text=text,
            items=items,
            _configuration=_configuration,
            **kwargs,
        )

from papermerge-restapi-client.model.node_type_enum import NodeTypeEnum
