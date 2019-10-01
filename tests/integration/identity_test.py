""" The purpose of this test file is to perform basic integration tests 

    The scope of these tests only includes checking that non-404 responses can be attained.
    Testing that endpoints actually work to spec is the responsibility of the API and Client.
"""

import pytest

# from sws_py_sdk import ecom, sws_client
from base_test import me_endpoint_sws_client, user_endpoint_sws_client

def test_login(me_endpoint_sws_client):
    error_response = me_endpoint_sws_client.identity().login(email_address="test.user@serato.com", password="Auckland009")

    assert me_endpoint_sws_client.identity().last_request.data != None
    assert me_endpoint_sws_client.identity().last_request.data['email_address'] == "test.user@serato.com"
    assert me_endpoint_sws_client.identity().last_request.data['password'] == "Auckland009"
    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500
