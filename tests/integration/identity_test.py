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

def test_me_logout(me_endpoint_sws_client):
    response = me_endpoint_sws_client.identity().logout(refresh_token="serato")
    
    assert response.status_code != 404
    assert response.status_code != 500

def test_user_logout(user_endpoint_sws_client):
    response = user_endpoint_sws_client.identity().logout(refresh_token="serato")
    
    assert response.status_code != 404
    assert response.status_code != 500

def test_token_refresh(me_endpoint_sws_client):
    response = me_endpoint_sws_client.identity().token_refresh(refresh_token="serato")
    
    assert response.status_code != 404
    assert response.status_code != 500 

def test_token_exchange(me_endpoint_sws_client):
    response = me_endpoint_sws_client.identity().token_exchange(
        grant_type="grant_type",
        code="code",
        redirect_uri="redirect_uri"
    )
    
    assert response.status_code != 404
    assert response.status_code != 500    

def test_get_users(user_endpoint_sws_client):
    response = user_endpoint_sws_client.identity().get_users(email_address="test@serato.com")
    
    assert response.status_code != 404
    assert response.status_code != 500  

def test_get_me(me_endpoint_sws_client):
    response = me_endpoint_sws_client.identity().get_user()
    
    assert response.status_code != 404
    assert response.status_code != 500  

def test_get_me(user_endpoint_sws_client):
    response = user_endpoint_sws_client.identity().get_user()
    
    assert response.status_code != 404
    assert response.status_code != 500  

def test_delete_me(me_endpoint_sws_client):
    response = me_endpoint_sws_client.identity().delete_user()
    
    assert response.status_code != 404
    assert response.status_code != 500  

def test_reset_password(me_endpoint_sws_client):
    response = me_endpoint_sws_client.identity().reset_password(
        email_address="test@serato.com"
    )
    
    assert response.status_code != 404
    assert response.status_code != 500 

def test_me_verify_email_address(me_endpoint_sws_client):
    response = me_endpoint_sws_client.identity().verify_email_address(
        email_address="test@serato.com", 
        redirect_uri="https://serato.com"
    )
    
    assert response.status_code != 404
    assert response.status_code != 500 

def test_me_verify_email_address(user_endpoint_sws_client):
    response = user_endpoint_sws_client.identity().verify_email_address(
        email_address="test@serato.com", 
        redirect_uri="https://serato.com"
    )
    
    assert response.status_code != 404
    assert response.status_code != 500 

def test_post_user_gaclientid(user_endpoint_sws_client):
    response = user_endpoint_sws_client.identity().post_user_gaclientid(
        ga_client_id="ga_client_id"
    )
    
    assert response.status_code != 404
    assert response.status_code != 500