# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b26
    Generated by: https://openapi-generator.tech
"""

from papermerge_restapi_client.paths.api_auth_login_.post import AuthLoginCreate
from papermerge_restapi_client.paths.api_auth_logout_.post import AuthLogoutCreate
from papermerge_restapi_client.paths.api_auth_logoutall_.post import AuthLogoutallCreate


class AuthApi(
    AuthLoginCreate,
    AuthLogoutCreate,
    AuthLogoutallCreate,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
