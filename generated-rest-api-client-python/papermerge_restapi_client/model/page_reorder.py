# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b20
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


class PageReorder(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "old_number",
            "id",
            "new_number",
        }
        
        class properties:
            id = schemas.UUIDSchema
            old_number = schemas.IntSchema
            new_number = schemas.IntSchema
            __annotations__ = {
                "id": id,
                "old_number": old_number,
                "new_number": new_number,
            }
    
    old_number: MetaOapg.properties.old_number
    id: MetaOapg.properties.id
    new_number: MetaOapg.properties.new_number
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["old_number"]) -> MetaOapg.properties.old_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["new_number"]) -> MetaOapg.properties.new_number: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "old_number", "new_number", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["old_number"]) -> MetaOapg.properties.old_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["new_number"]) -> MetaOapg.properties.new_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "old_number", "new_number", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        old_number: typing.Union[MetaOapg.properties.old_number, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        new_number: typing.Union[MetaOapg.properties.new_number, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PageReorder':
        return super().__new__(
            cls,
            *args,
            old_number=old_number,
            id=id,
            new_number=new_number,
            _configuration=_configuration,
            **kwargs,
        )
