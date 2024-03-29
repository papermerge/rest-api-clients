# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.9
    Generated by: https://openapi-generator.tech
"""

from papermerge_restapi_client.paths.api_document_versions_id_download_.get import DocumentVersionsDownloadRetrieve
from papermerge_restapi_client.paths.api_document_versions_id_.get import DocumentVersionsRetrieve


class DocumentVersionsApi(
    DocumentVersionsDownloadRetrieve,
    DocumentVersionsRetrieve,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
