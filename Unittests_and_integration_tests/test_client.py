#!/usr/bin/env python3
""" Unit Testing for GithubOrgClient """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: unittest.mock.patch):
        """Test that GithubOrgClient.org returns the correct organization."""
        test_class = GithubOrgClient(org_name)
        test_class.org()

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


if __name__ == '__main__':
    unittest.main()