""" The purpose of this test file is to perform basic integration tests

    The scope of these tests only includes checking that non-404 responses can be attained.
    Testing that endpoints actually work to spec is the responsibility of the API and Client.
"""

import pytest
import datetime

# from sws_py_sdk import ecom, sws_client
from base_test import me_endpoint_sws_client, user_endpoint_sws_client

def test_get_me_subscriptions(me_endpoint_sws_client):
    response = me_endpoint_sws_client.ecom().get_subscriptions()
    assert response.status_code != 404
    assert response.status_code != 500

def test_get_user_subscriptions(user_endpoint_sws_client):
    response = user_endpoint_sws_client.ecom().get_subscriptions()
    assert response.status_code != 404
    assert response.status_code != 500


def test_get_me_subscriptions_with_sub_id(me_endpoint_sws_client):
    response = me_endpoint_sws_client.ecom().get_subscriptions("notasubscriptionid")
    assert response.status_code != 404
    assert response.status_code != 500


def test_get_user_subscriptions_with_sub_id(user_endpoint_sws_client):
    response = user_endpoint_sws_client.ecom().get_subscriptions("notasubscriptionid")
    assert response.status_code != 404
    assert response.status_code != 500


def test_update_me_subscription(me_endpoint_sws_client):
    subscription_id="subId"
    number_of_billing_cycle = 400
    payment_method_token = "tokenlookin"
    response = me_endpoint_sws_client.ecom().update_subscription(
        subscription_id=subscription_id,
        number_of_billing_cycle=number_of_billing_cycle,
        payment_method_token=payment_method_token
    )
    assert response.status_code != 404
    assert response.status_code != 500


def test_update_user_subscription(user_endpoint_sws_client):
    subscription_id = "bdcbd840933411e9b3ef1239f8b24ea2"
    number_of_billing_cycle = 4
    payment_method_token = "j8d7cx"
    response = user_endpoint_sws_client.ecom().update_subscription(
        subscription_id=subscription_id,
        number_of_billing_cycle=number_of_billing_cycle,
        payment_method_token=payment_method_token
    )
    assert response.status_code != 404
    assert response.status_code != 500

def test_delete_me_subscription(me_endpoint_sws_client):
    subscription_id = "subid"
    response = me_endpoint_sws_client.ecom().delete_subscription(subscription_id=subscription_id)

    assert response.status_code != 404
    assert response.status_code != 500

def test_delete_user_subscription(user_endpoint_sws_client):
    subscription_id = "subid"
    response = user_endpoint_sws_client.ecom().delete_subscription(subscription_id=subscription_id)

    assert response.status_code != 404
    assert response.status_code != 500

def test_get_me_orders(me_endpoint_sws_client):
    response = me_endpoint_sws_client.ecom().get_orders()

    assert response.status_code != 404
    assert response.status_code != 500


def test_get_user_orders(user_endpoint_sws_client):
    response = user_endpoint_sws_client.ecom().get_orders()

    assert response.status_code != 404
    assert response.status_code != 500

def test_get_me_invoice(me_endpoint_sws_client):
    order_id = 1000
    invoice_id = 2000
    response = me_endpoint_sws_client.ecom().get_invoice(order_id=order_id, invoice_id=invoice_id)

    assert response.status_code != 500


def test_get_user_invoice(user_endpoint_sws_client):
    order_id = 1000
    invoice_id = 2000
    response = user_endpoint_sws_client.ecom().get_invoice(order_id=order_id, invoice_id=invoice_id)

    assert response.status_code != 500

def test_get_me_payment_methods(me_endpoint_sws_client):
    response = me_endpoint_sws_client.ecom().get_payment_methods()

    assert response.status_code != 404
    assert response.status_code != 405
    assert response.status_code != 500


def test_get_user_payment_methods(user_endpoint_sws_client):
    response = user_endpoint_sws_client.ecom().get_payment_methods()

    assert response.status_code != 404
    assert response.status_code != 500

def test_update_me_payment_method(me_endpoint_sws_client):
    payment_token = "Uvuvwevwe"
    nonce = "Uvuvwevwe_Onyetenyevwe_Ugwembubwem_Ossas"
    device_data = "Uvuvwevwes Macbook Pro"
    billing_address_id = "Uv"

    response = me_endpoint_sws_client.ecom().update_payment_methods(
        payment_token=payment_token,
        nonce=nonce,
        device_data=device_data,
        billing_address_id=billing_address_id
    )
    assert response.status_code != 404
    assert response.status_code != 500


def test_update_user_payment_method(user_endpoint_sws_client):
    payment_token = "Uvuvwevwe"
    nonce = "Uvuvwevwe_Onyetenyevwe_Ugwembubwem_Ossas"
    device_data = "Uvuvwevwes Macbook Pro"
    billing_address_id = "Uv"

    response = user_endpoint_sws_client.ecom().update_payment_methods(
        payment_token=payment_token,
        nonce=nonce,
        device_data=device_data,
        billing_address_id=billing_address_id
    )
    assert response.status_code != 404
    assert response.status_code != 500


def test_delete_me_payment_method(me_endpoint_sws_client):
    payment_method_token = "Uvuvwevwe"
    response = me_endpoint_sws_client.ecom().delete_payment_method(payment_method_token=payment_method_token)

    assert response.status_code != 404
    assert response.status_code != 500

def test_delete_user_payment_method(user_endpoint_sws_client):
    payment_method_token = "Uvuvwevwe"
    response = user_endpoint_sws_client.ecom().delete_payment_method(payment_method_token=payment_method_token)

    assert response.status_code != 404
    assert response.status_code != 500

def test_add_me_plan_change_request(me_endpoint_sws_client):

    subscription_id = "Uvuvwevwe"
    catalog_product_id = 105
    response = me_endpoint_sws_client.ecom().add_plan_change_request(
        subscription_id=subscription_id,
        catalog_product_id=catalog_product_id
    )
    assert response.status_code != 404
    assert response.status_code != 500

def test_add_user_payment_method(user_endpoint_sws_client):
    nonce = "Uvuvwevwe_Onyetenyevwe_Ugwembubwem_Ossas"
    device_data = "Uvuvwevwes Macbook Pro"
    billing_address_id = "uv"
    response = user_endpoint_sws_client.ecom().add_payment_method(
        nonce=nonce,
        device_data=device_data,
        billing_address_id=billing_address_id
    )
    assert response.status_code != 500
    assert response.status_code != 404

def test_add_me_payment_method(me_endpoint_sws_client):
    nonce = "Uvuvwevwe_Onyetenyevwe_Ugwembubwem_Ossas"
    device_data = "Uvuvwevwes Macbook Pro"
    billing_address_id = "uv"
    response = me_endpoint_sws_client.ecom().add_payment_method(
        nonce=nonce,
        device_data=device_data,
        billing_address_id=billing_address_id
    )
    assert response.status_code != 500
    assert response.status_code != 404

def test_update_user_plan_change(user_endpoint_sws_client):
    subscription_id = "subsid"
    plan_change_id = "1000"
    response = user_endpoint_sws_client.ecom().update_plan_change(
        subscription_id=subscription_id,
        plan_change_id=plan_change_id
    )
    assert response.status_code != 500
    assert response.status_code != 404


def test_update_me_plan_change(me_endpoint_sws_client):
    subscription_id = "subsid"
    plan_change_id = "1000"
    response = me_endpoint_sws_client.ecom().update_plan_change(
        subscription_id=subscription_id,
        plan_change_id=plan_change_id
    )
    assert response.status_code != 500
    assert response.status_code != 404

def test_send_braintree_webhook(me_endpoint_sws_client):
    notification_kind = "subscription_charged_successfully"
    subscription_id = "fp4f36"
    response = me_endpoint_sws_client.ecom().send_braintree_webhook(
        notification_kind=notification_kind,
        subscription_id=subscription_id
    )
    assert response.status_code != 500
    assert response.status_code != 404

def test_create_promotion(me_endpoint_sws_client):
    currentDateTime = datetime.datetime.now()
    name = "promotion name"
    description = "promotion description"
    starts_at = str(currentDateTime)
    ends_at = str(currentDateTime + datetime.timedelta(days=10))
    coupon_based = True
    enabled = True

    response = me_endpoint_sws_client.ecom().create_promotion(
        name=name,
        description=description,
        starts_at=starts_at,
        ends_at=ends_at,
        coupon_based=coupon_based,
        enabled=enabled
    )

    assert response.status_code != 500
    assert response.status_code != 404

def test_create_promotion_coupons(me_endpoint_sws_client):
    promotion_id=7045
    usage_limit=10
    usage_limit_per_user=1
    expires_at=str(datetime.datetime.now() + datetime.timedelta(days=10))

    response = me_endpoint_sws_client.ecom().create_promotion_coupons(
        promotion_id=promotion_id,
        usage_limit=usage_limit,
        usage_limit_per_user=usage_limit_per_user,
        expires_at=expires_at
    )
    
    assert response.status_code != 500
    assert response.status_code != 404

def test_create_promotion_rule(me_endpoint_sws_client):
    promotion_id=7063
    product_type_id=138
    discount_percentage=10
    discount_fixed_amount=20
    pre_condition_product_id=95
    braintree_discount_id="some_discount_id"
    subscription_promotion_expires=3

    response = me_endpoint_sws_client.ecom().create_promotion_rule(
        promotion_id=promotion_id,
        product_type_id=product_type_id,
        discount_percentage=discount_percentage,
        discount_fixed_amount=discount_fixed_amount,
        pre_condition_product_id=pre_condition_product_id,
        braintree_discount_id=braintree_discount_id,
        subscription_promotion_expires=subscription_promotion_expires
    )
    
    assert response.status_code != 500
    assert response.status_code != 404

def test_delete_promotion(me_endpoint_sws_client):
    promotion_id = "7063"
    response = me_endpoint_sws_client.ecom().delete_promotion(promotion_id=promotion_id)

    assert response.status_code != 404
    assert response.status_code != 500

def test_delete_promotion_coupon(me_endpoint_sws_client):
    promotion_id = "7033"
    coupon_code = "COUPONCODE"
    response = me_endpoint_sws_client.ecom().delete_promotion_coupon(promotion_id=promotion_id, coupon_code=coupon_code)
    
    assert response.status_code != 404
    assert response.status_code != 500

def test_create_voucher(me_endpoint_sws_client):
    voucher_type_id=104
    batch_id="BATCH_ID"
    response = me_endpoint_sws_client.ecom().create_voucher(voucher_type_id=voucher_type_id, batch_id=batch_id)
    assert response.status_code != 404
    assert response.status_code != 500

def test_redeem_voucher(me_endpoint_sws_client):
    voucher_id = "VOUCHER-CODE"
    response = me_endpoint_sws_client.ecom().redeem_voucher(voucher_id=voucher_id)
    
    assert response.status_code != 404
    assert response.status_code != 500