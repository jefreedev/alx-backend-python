#!/usr/bin/env python3
""" Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Inherits from unittest.TestCase.
    """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Tests if a method returns what it should.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Ensure that an error is raised on a bad input.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map.path)


class TestGetJson(unittest.TestCase):
    """ Tests if JSON returns data in expected format.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, url, payload):
        """ Confirms if a method returns what it should.
        """
        class Mocked(Mock):
            """ Inherits props from class Moch.
            """

            def json(self):
                """ Returns a payload.
                """
                return payload

        with patch("requests.get") as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """ Tests for memoize.
    """
    def test_memoize(self):
        """ Tests fro memoization.
        """
        class TestClass:
            """ Tests class.
            """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mocked:
            i = TestClass()
            i.a_property
            mocked.assetCalledOnce()
