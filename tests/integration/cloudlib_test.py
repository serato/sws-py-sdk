""" The purpose of this test file is to perform basic integration tests

    The scope of these tests only includes checking that non-404 responses can be attained.
    Testing that endpoints actually work to spec is the responsibility of the API and Client.
"""

import pytest
import datetime

# from sws_py_sdk import cloudlib, sws_client
from base_test import me_endpoint_sws_client, user_endpoint_sws_client

def me_create_file_upload(me_endpoint_sws_client):
    response = me_endpoint_sws_client.cloudlib().me_create_file_upload(md5_hash='mockhash', mime_type='mockmime', size=123, name=None)
    assert response.status_code != 404
    assert response.status_code != 500

def test_user_create_file_upload(user_endpoint_sws_client):
    response = user_endpoint_sws_client.cloudlib().user_create_file_upload(md5_hash='mockhash', mime_type='mockmime', size=123, name=None)
    assert response.status_code != 404
    assert response.status_code != 500

def test_me_get_file(user_endpoint_sws_client):
    response = user_endpoint_sws_client.cloudlib().me_get_file(name=None)
    assert response.status_code != 500

def test_user_get_file(user_endpoint_sws_client):
    response = user_endpoint_sws_client.cloudlib().user_get_file(name=None)
    assert response.status_code != 500
