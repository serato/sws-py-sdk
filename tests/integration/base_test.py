""" This base file exists to define fixtures and configuration that can be used for integration tests.
"""
import pytest

APP_ID = 'myClientAppId'
SERVICE_URI= {
    "id": "http://192.168.4.14:8585",
    "license": "http://192.168.4.14:8686",
    "ecom": "http://192.168.4.14:8787"
}

@pytest.fixture
def me_endpoint_sws_client():
    from sws_py_sdk.sws_client import SwsClient

    return SwsClient(app_id=APP_ID, secret='myclientapppassword', service_uri=SERVICE_URI)


@pytest.fixture
def user_endpoint_sws_client():
    from sws_py_sdk.sws_client import SwsClient

    return SwsClient(app_id=APP_ID, secret='myclientapppassword', service_uri=SERVICE_URI, user_id=100000)
