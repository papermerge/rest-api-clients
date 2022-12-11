# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b34
    Generated by: https://openapi-generator.tech
"""

from papermerge_restapi_client.paths.api_groups_.post import GroupsCreate
from papermerge_restapi_client.paths.api_groups_id_.delete import GroupsDestroy
from papermerge_restapi_client.paths.api_groups_.get import GroupsList
from papermerge_restapi_client.paths.api_groups_id_.patch import GroupsPartialUpdate
from papermerge_restapi_client.paths.api_groups_id_.get import GroupsRetrieve


class GroupsApi(
    GroupsCreate,
    GroupsDestroy,
    GroupsList,
    GroupsPartialUpdate,
    GroupsRetrieve,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
