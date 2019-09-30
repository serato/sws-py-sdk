""" The purpose of this test file is to perform basic integration tests 

    The scope of these tests only includes checking that non-404 responses can be attained.
    Testing that endpoints actually work to spec is the responsibility of the API and Client.
"""

import pytest

# from sws_py_sdk import ecom, sws_client
from base_test import me_endpoint_sws_client, user_endpoint_sws_client

def test_get_me_subscriptions(me_endpoint_sws_client):
    error_response = me_endpoint_sws_client.ecom().get_subscriptions()
    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500

def test_get_user_subscriptions(user_endpoint_sws_client):
    error_response = user_endpoint_sws_client.ecom().get_subscriptions()
    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500


def test_get_me_subscriptions_with_sub_id(me_endpoint_sws_client):
    error_response = me_endpoint_sws_client.ecom().get_subscriptions("notasubscriptionid")
    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500


def test_get_user_subscriptions_with_sub_id(user_endpoint_sws_client):
    error_response = user_endpoint_sws_client.ecom().get_subscriptions("notasubscriptionid")
    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500


def test_update_me_subscription(me_endpoint_sws_client):
    subscription_id="subId"
    number_of_billing_cycle = 400
    payment_method_token = "tokenlookin"
    error_response = me_endpoint_sws_client.ecom().update_subscription(
        subscription_id=subscription_id,
        number_of_billing_cycle=number_of_billing_cycle,
        payment_method_token=payment_method_token
    )
    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500


def test_update_user_subscription(user_endpoint_sws_client):
    subscription_id = "bdcbd840933411e9b3ef1239f8b24ea2"
    number_of_billing_cycle = 4
    payment_method_token = "j8d7cx"
    error_response = user_endpoint_sws_client.ecom().update_subscription(
        subscription_id=subscription_id,
        number_of_billing_cycle=number_of_billing_cycle,
        payment_method_token=payment_method_token
    )
    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500

def test_delete_me_subscription(me_endpoint_sws_client):
    subscription_id = "subid"
    error_response = me_endpoint_sws_client.ecom().delete_subscription(subscription_id=subscription_id)

    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500

def test_delete_user_subscription(user_endpoint_sws_client):
    subscription_id = "subid"
    error_response = user_endpoint_sws_client.ecom().delete_subscription(subscription_id=subscription_id)

    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500

def test_get_me_orders(me_endpoint_sws_client):
    order_id = 1000
    error_response = me_endpoint_sws_client.ecom().get_orders(order_id)

    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500


def test_get_me_orders(user_endpoint_sws_client):
    order_id = 1000
    error_response = user_endpoint_sws_client.ecom().get_orders(order_id)

    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500

def test_get_me_invoices(me_endpoint_sws_client):
    order_id = 1000
    error_response = me_endpoint_sws_client.ecom().get_invoices(order_id)

    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500


def test_get_user_invoices(user_endpoint_sws_client):
    order_id = 1000
    error_response = user_endpoint_sws_client.ecom().get_invoices(order_id)

    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500


def test_get_me_payment_methods(me_endpoint_sws_client):
    error_response = me_endpoint_sws_client.ecom().get_payment_methods()

    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500


def test_get_user_payment_methods(user_endpoint_sws_client):
    error_response = user_endpoint_sws_client.ecom().get_payment_methods()

    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500

def test_update_me_payment_method(me_endpoint_sws_client):
    payment_token = "Uvuvwevwe"
    nonce = "Uvuvwevwe_Onyetenyevwe_Ugwembubwem_Ossas"
    device_data = "Uvuvwevwes Macbook Pro"
    billing_address_id = "Uv"

    error_response = me_endpoint_sws_client.ecom().update_payment_methods(
        payment_token=payment_token,
        nonce=nonce,
        device_data=device_data,
        billing_address_id=billing_address_id
    )
    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500


def test_update_user_payment_method(user_endpoint_sws_client):
    payment_token = "Uvuvwevwe"
    nonce = "Uvuvwevwe_Onyetenyevwe_Ugwembubwem_Ossas"
    device_data = "Uvuvwevwes Macbook Pro"
    billing_address_id = "Uv"

    error_response = user_endpoint_sws_client.ecom().update_payment_methods(
        payment_token=payment_token,
        nonce=nonce,
        device_data=device_data,
        billing_address_id=billing_address_id
    )
    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500


def test_delete_me_payment_method(me_endpoint_sws_client):
    payment_method_token = "Uvuvwevwe"
    error_response = me_endpoint_sws_client.ecom().delete_payment_method(payment_method_token=payment_method_token)
    
    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500

def test_delete_user_payment_method(user_endpoint_sws_client):
    payment_method_token = "Uvuvwevwe"
    error_response = user_endpoint_sws_client.ecom().delete_payment_method(payment_method_token=payment_method_token)
    
    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500

def test_add_me_plan_change_request(me_endpoint_sws_client):

    subscription_id = "Uvuvwevwe"
    catalog_product_id = 105
    error_response = me_endpoint_sws_client.ecom().add_plan_change_request(
        subscription_id=subscription_id,
        catalog_product_id=catalog_product_id
    )
    assert error_response.response.status_code != 404
    assert error_response.response.status_code != 500

def test_add_user_payment_method(user_endpoint_sws_client):
    nonce = "Uvuvwevwe_Onyetenyevwe_Ugwembubwem_Ossas"
    device_data = "Uvuvwevwes Macbook Pro"
    billing_address_id = "uv"
    error_response = user_endpoint_sws_client.ecom().add_payment_method(
        nonce=nonce,
        device_data=device_data,
        billing_address_id=billing_address_id
    )
    assert error_response.response.status_code != 500
    assert error_response.response.status_code != 404

def test_add_me_payment_method(me_endpoint_sws_client):
    nonce = "Uvuvwevwe_Onyetenyevwe_Ugwembubwem_Ossas"
    device_data = "Uvuvwevwes Macbook Pro"
    billing_address_id = "uv"
    error_response = me_endpoint_sws_client.ecom().add_payment_method(
        nonce=nonce,
        device_data=device_data,
        billing_address_id=billing_address_id
    )
    assert error_response.response.status_code != 500
    assert error_response.response.status_code != 404

def test_update_user_plan_change(user_endpoint_sws_client):
    subscription_id = "subsid"
    plan_change_id = "1000"
    error_response = user_endpoint_sws_client.ecom().update_plan_change(
        subscription_id=subscription_id,
        plan_change_id=plan_change_id
    )
    assert error_response.response.status_code != 500
    assert error_response.response.status_code != 404


def test_update_me_plan_change(me_endpoint_sws_client):
    subscription_id = "subsid"
    plan_change_id = "1000"
    error_response = me_endpoint_sws_client.ecom().update_plan_change(
        subscription_id=subscription_id,
        plan_change_id=plan_change_id
    )
    assert error_response.response.status_code != 500
    assert error_response.response.status_code != 404
