from datetime import datetime 

import pytest
import requests_mock

from sws_py_sdk.sws_client import SwsClient


APP_ID = 'myClientAppId'
GET_LICENSES_API = '/api/v1/me/licenses'
NEW_ACCESS_TOKEN_VALUE = 'New.Access.Token.Value'

INVALID_ACCESS_TOKEN_ERRORS = [
        {
            'httpStatus': 403,
            'code': 2001,
            'errorText': 'Invalid Access token'
        },
            #   Access token has expired
        {
            'httpStatus': 401,
            'code': 2002,
            'errorText': 'Expired Access token'
        }
    ]
MOCK_TOKEN_REFRESH_RESPONSE_BODY =  {
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

MOCK_GET_LICENSES_RESPONSE_BODY = {
  "items": [
    {
      "id": "SDJ-1047936-0034-7100-4717",
      "activation_limit": 2,
      "activations": [
        {
          "app": {
            "id": "dj",
            "version": "1.9.4"
          },
          "machine": {
            "hardware_id": "P6ZA66QPQI85~NCCYW33555RF54N4HO",
            "canonical_hardware_id": "P6ZA66QPQI85",
            "name": "BigDaves-MBP"
          }
        }
      ],
      "license_type": {
        "id": 34,
        "name": "Serato DJ - Subscription",
        "term": "subscription",
        "rlm_schema": {
          "name": "serato_dj",
          "version": "1.0",
          "options": "S"
        }
      },
      "valid_to_with_grace_period":"2016-02-12T12:29:22Z",
      "expires_in_days": 10,
      "valid_to": "2016-02-12T12:29:22Z",
      "subscription_status": "Active"
    },
    {
      "id": "SDJ-1047936-0036-7100-4717",
      "activation_limit": 2,
      "activations": [
        {
          "app": {
            "id": "dj",
            "version": "1.9.4"
          },
          "machine": {
            "hardware_id": "P6ZA66QPQI85~NCCYW33555RF54N4HO",
            "canonical_hardware_id": "P6ZA66QPQI85",
            "name": "BigDaves-MBP"
          }
        }
      ],
      "license_type": {
        "id": 36,
        "name": "DVS - Subscription",
        "term": "subscription",
        "rlm_schema": {
          "name": "serato_dvs_pack",
          "version": "1.0",
          "options": "S"
        }
      },
      "expires_in_days": 22,
      "valid_to": "2016-02-12T12:29:22Z"
    },
    {
      "id": "2319511-1220-3457-8505",
      "activation_limit": 1,
      "license_type": {
        "id": 20,
        "name": "Pitch 'n Time LE 3",
        "term": "permanent"
      },
      "ilok": {
        "token": "9137-0339-6584-8878-6501-3520-9308-47",
        "user_id": "ilok_user_id@example.com",
        "url": "http://www.ilok.com/lc/r?c=9137-0339-6584-8878-6501-3520-9308-47&u=ilok_user_id%2B100%40example.com"
      },
      "valid_to": "2016-02-12T12:29:22Z",
      "subscription_status": "Active"
    }
  ]
}

TOKEN_REFRESH_URL = '/api/v1/me/tokens/refresh'
GET_LICENSES_API = '/api/v1/users/1000/licenses'
SERVICE_URI = {
    "id": "http://192.168.4.7",
    "license": "http://192.168.4.6"
}
""" Some SWS Client tests, these largely concern the clients ability to manage tokens
"""


def test_invalid_access_token_will_refresh_and_retry(requests_mock):
    # Build up mock requests and responses
    # 1: Request getLicenses -> get error response
    # 2: request token refresh -> get new access token

    sws_client = SwsClient(app_id=APP_ID, secret='myclientapppassword', service_uri=SERVICE_URI, user_id=1000)
    # Set refresh token
    sws_client.refresh_token = MOCK_TOKEN_REFRESH_RESPONSE_BODY['tokens']['access']['token']
    # Set handler for access token update
    sws_client.access_token_updated_handler = handle_access_token_update
    
    # Build up mock requests
    get_licenses_url = SERVICE_URI['license'] + GET_LICENSES_API
    requests_mock.register_uri('GET', get_licenses_url, json=MOCK_GET_LICENSES_RESPONSE_BODY, status_code=403)
    token_refresh_url = SERVICE_URI['id'] + TOKEN_REFRESH_URL
    requests_mock.register_uri('POST', token_refresh_url, json=MOCK_TOKEN_REFRESH_RESPONSE_BODY)
    requests_mock.register_uri('GET', get_licenses_url, json=MOCK_GET_LICENSES_RESPONSE_BODY, status_code=200)
    response = sws_client.license().get_licenses()
    assert response.status_code == 200
    data = response.json()
    assert data == MOCK_GET_LICENSES_RESPONSE_BODY

def handle_access_token_update(token, expires):

    assert token == MOCK_TOKEN_REFRESH_RESPONSE_BODY['tokens']['access']['token']
    assert expires == datetime.utcfromtimestamp(MOCK_TOKEN_REFRESH_RESPONSE_BODY['tokens']['access']['expires_at'])