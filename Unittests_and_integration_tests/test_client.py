#!/usr/bin/env python3
""" Unit Testing for GithubOrgClient """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct organization."""
        expected_response = {"login": org_name}
        mock_get_json.return_value = expected_response

        client = GithubOrgClient(org_name)

        self.assertEqual(client.org(), expected_response)

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


if __name__ == '__main__':
    unittest.main()