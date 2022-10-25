# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import papermerge_restapi_client
from papermerge_restapi_client.paths.api_users_id_ import patch  # noqa: E501
from papermerge_restapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiUsersId(ApiTestMixin, unittest.TestCase):
    """
    ApiUsersId unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = patch.ApiForpatch(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
