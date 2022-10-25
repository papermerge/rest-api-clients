# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import papermerge_restapi_client
from papermerge_restapi_client.paths.api_folders_id_ import delete  # noqa: E501
from papermerge_restapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiFoldersId(ApiTestMixin, unittest.TestCase):
    """
    ApiFoldersId unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
