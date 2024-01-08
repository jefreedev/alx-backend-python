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
                   PropertyMock(return_value=result)):
            res = GithubOrgClient(name).public_repos_url
            self.assertEqual(res, result.get("repo_url"))

    @patch("client.get_json")
    def test_public_repos(self, mocked_method):
        """ Tests for public Github repos urls.
        """
        payload = [{"name": "Google"}, {"name": "TT"}]
        mocked_method.return_value = payload

        with patch("client.GithubOrgClient.public_repos_url",
                   new_callable=PropertyMock) as mocked_public:
            mocked_public.return_value = "world"
            res = GithubOrgClient("test").public_repos()

            self.assertEqual(res, ["Google", "TT"])

            mocked_public.assert_called_once()
            mocked_method.assert_called_once()
