""" The purpose of this test file is to perform basic integration tests 

    The scope of these tests only includes checking that non-404 responses can be attained.
    Testing that endpoints actually work to spec is the responsibility of the API and Client.
"""

import pytest
import json

# from sws_py_sdk import ecom, sws_client
from base_test import me_endpoint_sws_client, user_endpoint_sws_client

def test_login(me_endpoint_sws_client):
    response = me_endpoint_sws_client.identity().login(email_address="test.user@serato.com", password="Auckland009")

    assert me_endpoint_sws_client.identity().last_request.data != None
    json_result = json.loads(me_endpoint_sws_client.identity().last_request.data)
    assert json_result['email_address'] == "test.user@serato.com"
    assert json_result['password'] == "Auckland009"
    assert response.status_code != 404
    assert response.status_code != 500


def test_create_user(me_endpoint_sws_client):
    response = me_endpoint_sws_client.identity().post_users(
        email_address="test.useruser@serato.com",
        password="test_password"
    )

    assert response.status_code != 404
    assert response.status_code != 500


def test_me_groups(me_endpoint_sws_client):
    response = me_endpoint_sws_client.identity().post_groups(
        group_name="serato"
    )

    assert response.status_code != 404
    assert response.status_code != 500


def test_user_groups(user_endpoint_sws_client):
    response = user_endpoint_sws_client.identity().post_groups(
        group_name="serato"
    )

    assert response.status_code != 404
    assert response.status_code != 500
