# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b12
    Generated by: https://openapi-generator.tech
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "papermerge-restapi-client"
VERSION = "1.0.4"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.15",
  "certifi",
  "python-dateutil",
  "frozendict >= 2.0.3",
  "typing_extensions",
]

setup(
    name=NAME,
    version=VERSION,
    description="Papermerge REST API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Papermerge REST API"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    Document management system designed for digital archives  # noqa: E501
    """
)
