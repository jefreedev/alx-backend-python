#!/usr/bin/env python3
""" Unittest client module.
"""
import unittest

from unittest import mock
from urllib import response
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """ Tests for github org client.
    """
    @parameterized.expand([
        ("google"),
        ("abc")
        ])
    @patch("client.get_json")
    def test_org(self, data, mock):
        """ Tests for org.
        """
        api_url = "https://api.github.com/orgs/{}".format(data)
        tmp = GithubOrgClient(data)
        tmp.org()
        mock.assert_called_once_with(api_url)

    @parameterized.expand([
        ("rand_url", {"repo_url": "http://some_url.com"})
        ])
    def test_public_repos_url(self, name, result):
        """ Tests for public repo urls.
        """
        with patch("client.GithubOrgClient.org",
                   Property)
