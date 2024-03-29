# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.9
    Generated by: https://openapi-generator.tech
"""

from papermerge_restapi_client.paths.api_folders_.post import FoldersCreate
from papermerge_restapi_client.paths.api_folders_id_.delete import FoldersDestroy
from papermerge_restapi_client.paths.api_folders_.get import FoldersList
from papermerge_restapi_client.paths.api_folders_id_.patch import FoldersPartialUpdate
from papermerge_restapi_client.paths.api_folders_id_.get import FoldersRetrieve


class FoldersApi(
    FoldersCreate,
    FoldersDestroy,
    FoldersList,
    FoldersPartialUpdate,
    FoldersRetrieve,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
