from sws_py_sdk.service import Service
from sws_py_sdk.identity import Identity
from sws_py_sdk.sws import Sws

TOKEN_REFRESH_URL = '/api/v1/tokens/refresh'

MOCK_RESPONSE_BODY =  {
    "user": {
        "id": 12345,
        "email_address": "example@example.com",
        "first_name": "Billy",
        "last_name": "Bob",
        "date_created": "2016-11-05T08:15:30Z",
        "locale": "en_US.UTF-8"
    },
    "tokens": {
        "access": {
            "token": "NgCXRKdjsLksdKKJjslPQmxMzYjw",
            "expires_at": 1489142529,
            "scopes": {
                "license.serato.io": ["user-license", "user-license-admin"]
            },
            "type": "Bearer"
        },
        "refresh": {
            "token": "NgAagAAYqJQjdkEkjkjSkkseKSKaweplOeklUm_SHo",
            "expires_at": 1489174529,
            "type": "Bearer"
        }
    }
}

SERVICE_URI = {
    "id": "http://192.168.4.6",
    "license": "http://192.168.4.7"
}
app_id = "MyClientId"
# 'http://' + SERVICE_URI['id'] + TOKEN_REFRESH_URL
# http:// 192.168.4.7 /api/v1/me/tokens/refresh
def test_token_refresh_returns_tokens(requests_mock):
    sws = Sws(app_id=app_id, secret='myclientapppassword', service_uri=SERVICE_URI)
    url = SERVICE_URI['id'] + TOKEN_REFRESH_URL
    requests_mock.register_uri('POST', url, json=MOCK_RESPONSE_BODY)
    response = sws.identity().token_refresh(refresh_token='totally_refresh_refresh_token')
    assert response.status_code is 200
    json_response = response.json()
    assert json_response['user']['id'] == 12345
    assert json_response['tokens']['access']['token'] == "NgCXRKdjsLksdKKJjslPQmxMzYjw"
    assert json_response['tokens']['refresh']['token'] == "NgAagAAYqJQjdkEkjkjSkkseKSKaweplOeklUm_SHo"


def test_cdn_auth_header(requests_mock):
    """Tests that the test stack CDN authentication header is added to requests, if credentials are given"""
    sws = Sws(app_id=app_id, secret='myclientapppassword', service_uri=SERVICE_URI, cdn_auth_id='test_id',
              cdn_auth_secret='test_secret')
    url = SERVICE_URI['id'] + TOKEN_REFRESH_URL
    requests_mock.register_uri('POST', url, json=MOCK_RESPONSE_BODY,
                               request_headers={'x-serato-cdn-auth': 'dGVzdF9pZDp0ZXN0X3NlY3JldA=='})

    # Any API call (validating the request headers)
    sws.identity().token_refresh(refresh_token='totally_refresh_refresh_token')
