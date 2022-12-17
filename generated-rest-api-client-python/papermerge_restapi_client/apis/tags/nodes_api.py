# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.1
    Generated by: https://openapi-generator.tech
"""

from papermerge_restapi_client.paths.api_nodes_id_tags_.patch import NodeAppendTags
from papermerge_restapi_client.paths.api_nodes_id_tags_.post import NodeAssignTags
from papermerge_restapi_client.paths.api_nodes_id_tags_.delete import NodeDissociateTags
from papermerge_restapi_client.paths.api_nodes_id_.get import NodeRetrieve
from papermerge_restapi_client.paths.api_nodes_.post import NodesCreate
from papermerge_restapi_client.paths.api_nodes_id_.delete import NodesDestroy
from papermerge_restapi_client.paths.api_nodes_download_.get import NodesDownload
from papermerge_restapi_client.paths.api_nodes_inboxcount_.get import NodesInboxcountRetrieve
from papermerge_restapi_client.paths.api_nodes_.get import NodesList
from papermerge_restapi_client.paths.api_nodes_move_.post import NodesMoveCreate
from papermerge_restapi_client.paths.api_nodes_id_.patch import NodesPartialUpdate


class NodesApi(
    NodeAppendTags,
    NodeAssignTags,
    NodeDissociateTags,
    NodeRetrieve,
    NodesCreate,
    NodesDestroy,
    NodesDownload,
    NodesInboxcountRetrieve,
    NodesList,
    NodesMoveCreate,
    NodesPartialUpdate,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
