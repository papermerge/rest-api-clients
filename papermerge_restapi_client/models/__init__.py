# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from papermerge_restapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from papermerge_restapi_client.model.archive_type_enum import ArchiveTypeEnum
from papermerge_restapi_client.model.auth_token import AuthToken
from papermerge_restapi_client.model.custom_user_preference import CustomUserPreference
from papermerge_restapi_client.model.datum import Datum
from papermerge_restapi_client.model.document_details import DocumentDetails
from papermerge_restapi_client.model.document_version import DocumentVersion
from papermerge_restapi_client.model.document_version_ocr_text import DocumentVersionOcrText
from papermerge_restapi_client.model.documents_merge import DocumentsMerge
from papermerge_restapi_client.model.error import Error
from papermerge_restapi_client.model.errors import Errors
from papermerge_restapi_client.model.failure import Failure
from papermerge_restapi_client.model.folder import Folder
from papermerge_restapi_client.model.group import Group
from papermerge_restapi_client.model.id import Id
from papermerge_restapi_client.model.inbox_count import InboxCount
from papermerge_restapi_client.model.include_version_enum import IncludeVersionEnum
from papermerge_restapi_client.model.jsonapi import Jsonapi
from papermerge_restapi_client.model.link import Link
from papermerge_restapi_client.model.linkage import Linkage
from papermerge_restapi_client.model.links import Links
from papermerge_restapi_client.model.meta import Meta
from papermerge_restapi_client.model.node import Node
from papermerge_restapi_client.model.node_id import NodeID
from papermerge_restapi_client.model.node_move import NodeMove
from papermerge_restapi_client.model.node_tags import NodeTags
from papermerge_restapi_client.model.node_type_enum import NodeTypeEnum
from papermerge_restapi_client.model.nodes_download import NodesDownload
from papermerge_restapi_client.model.ocr import Ocr
from papermerge_restapi_client.model.onlymeta import Onlymeta
from papermerge_restapi_client.model.page import Page
from papermerge_restapi_client.model.page_reorder import PageReorder
from papermerge_restapi_client.model.page_rotate import PageRotate
from papermerge_restapi_client.model.pageref import Pageref
from papermerge_restapi_client.model.pages_move_to_document import PagesMoveToDocument
from papermerge_restapi_client.model.pages_move_to_folder import PagesMoveToFolder
from papermerge_restapi_client.model.pages_reorder import PagesReorder
from papermerge_restapi_client.model.pages_rotate import PagesRotate
from papermerge_restapi_client.model.paginated_custom_user_preference_list import PaginatedCustomUserPreferenceList
from papermerge_restapi_client.model.paginated_document_details_list import PaginatedDocumentDetailsList
from papermerge_restapi_client.model.paginated_folder_list import PaginatedFolderList
from papermerge_restapi_client.model.paginated_group_list import PaginatedGroupList
from papermerge_restapi_client.model.paginated_node_list import PaginatedNodeList
from papermerge_restapi_client.model.paginated_tag_list import PaginatedTagList
from papermerge_restapi_client.model.paginated_token_list import PaginatedTokenList
from papermerge_restapi_client.model.paginated_user_list import PaginatedUserList
from papermerge_restapi_client.model.pagination import Pagination
from papermerge_restapi_client.model.password import Password
from papermerge_restapi_client.model.patched_custom_user_preference import PatchedCustomUserPreference
from papermerge_restapi_client.model.patched_document_details import PatchedDocumentDetails
from papermerge_restapi_client.model.patched_folder import PatchedFolder
from papermerge_restapi_client.model.patched_group import PatchedGroup
from papermerge_restapi_client.model.patched_node import PatchedNode
from papermerge_restapi_client.model.patched_node_tags import PatchedNodeTags
from papermerge_restapi_client.model.patched_tag import PatchedTag
from papermerge_restapi_client.model.patched_user import PatchedUser
from papermerge_restapi_client.model.permission import Permission
from papermerge_restapi_client.model.relationship_links import RelationshipLinks
from papermerge_restapi_client.model.relationship_to_many import RelationshipToMany
from papermerge_restapi_client.model.relationship_to_one import RelationshipToOne
from papermerge_restapi_client.model.reltomany import Reltomany
from papermerge_restapi_client.model.reltoone import Reltoone
from papermerge_restapi_client.model.resource import Resource
from papermerge_restapi_client.model.resource_identifier_object import ResourceIdentifierObject
from papermerge_restapi_client.model.search_result import SearchResult
from papermerge_restapi_client.model.tag import Tag
from papermerge_restapi_client.model.token import Token
from papermerge_restapi_client.model.type import Type
from papermerge_restapi_client.model.user import User
from papermerge_restapi_client.model.version import Version
