""" The purpose of this test file is to perform basic integration tests 

    The scope of these tests only includes checking that non-404 responses can be attained.
    Testing that endpoints actually work to spec is the responsibility of the API and Client.
"""

from base_test import me_endpoint_sws_client as me_client, user_endpoint_sws_client as user_client


def test_get_me_licenses(me_client):
    response = me_client.license().get_licenses()
    assert response.status_code != 404
    assert response.status_code != 500


def test_get_user_licenses(user_client):
    response = user_client.license().get_licenses()
    assert response.status_code != 404
    assert response.status_code != 500


def test_create_me_license_authorization(me_client):
    action = 'activate'
    app_name = 'serato_studio'
    app_version = '1.0.0'
    host_machine_id = 'ABC123123'
    host_machine_name = 'My Machine'
    license_id = '420'
    system_time = '2019-10-10T17:01:33+13:00'
    response = me_client.license().create_license_authorization(action=action,
                                                                app_name=app_name,
                                                                app_version=app_version,
                                                                host_machine_id=host_machine_id,
                                                                host_machine_name=host_machine_name,
                                                                license_id=license_id,
                                                                system_time=system_time)

    assert response.status_code != 404
    assert response.status_code != 500


def test_create_user_license_authorization(user_client):
    action = 'activate'
    app_name = 'serato_studio'
    app_version = '1.0.0'
    host_machine_id = 'ABC123123'
    host_machine_name = 'My Machine'
    license_id = '420'
    system_time = '2019-10-10T17:01:33+13:00'
    response = user_client.license().create_license_authorization(action=action,
                                                                  app_name=app_name,
                                                                  app_version=app_version,
                                                                  host_machine_id=host_machine_id,
                                                                  host_machine_name=host_machine_name,
                                                                  license_id=license_id,
                                                                  system_time=system_time)
    assert response.status_code != 404
    assert response.status_code != 500


def test_update_me_license_authorization(me_client):
    authorization_id = 420
    authorization_status_code = 111
    response = me_client.license().update_license_authorization(authorization_id, authorization_status_code)
    assert response.status_code != 404
    assert response.status_code != 500


def test_update_user_license_authorization(user_client):
    authorization_id = 420
    authorization_status_code = 111
    response = user_client.license().update_license_authorization(authorization_id, authorization_status_code)
    assert response.status_code != 404
    assert response.status_code != 500


def test_get_me_products(me_client):
    response = me_client.license().get_products()
    assert response.status_code != 404
    assert response.status_code != 500


def test_get_user_products(user_client):
    response = user_client.license().get_products()
    assert response.status_code != 404
    assert response.status_code != 500


def test_add_me_product(me_client):
    product_type_id = 420
    response = me_client.license().add_product(product_type_id=product_type_id)
    assert response.status_code != 404
    assert response.status_code != 500


def test_add_user_product(user_client):
    product_type_id = 420
    response = user_client.license().add_product(product_type_id=product_type_id)
    assert response.status_code != 404
    assert response.status_code != 500


def test_update_me_product(me_client):
    product_id = '420'
    ilok_user_id = '42'
    response = me_client.license().update_product(product_id=product_id, ilok_user_id=ilok_user_id)
    assert response.status_code != 404
    assert response.status_code != 500


def test_update_me_product(user_client):
    product_id = '420'
    ilok_user_id = '42'
    response = user_client.license().update_product(product_id=product_id, ilok_user_id=ilok_user_id)
    assert response.status_code != 404
    assert response.status_code != 500


def test_get_product_types(me_client):
    response = me_client.license().get_product_types()
    assert response.status_code != 404
    assert response.status_code != 500


def test_get_product_type_details(me_client):
    product_type_id = 420
    response = me_client.license().get_product_type_details(product_type_id=product_type_id)
    assert response.status_code != 404
    assert response.status_code != 500


def test_reset_trials_for_product_type(me_client):
    product_type_id = 420
    reset_date = '2019-10-10T17:01:33+13:00'
    response = me_client.license().reset_trials_for_product_type(product_type_id=product_type_id, reset_date=reset_date)
    assert response.status_code != 404
    assert response.status_code != 500


def test_admin_get_products(me_client):
    checkout_order_id = 420
    response = me_client.license().admin_get_products(checkout_order_id=checkout_order_id)
    assert response.status_code != 404
    assert response.status_code != 500


def test_admin_add_product(me_client):
    product_type_id = 420
    created_by_user_id = '111'
    user_email_address = 'lollies@lollyjar.com'
    nfr = 'true'
    notes = 'I want this person to have a NFR.'
    response = me_client.license().admin_add_product(product_type_id=product_type_id,
                                                     user_email_address=user_email_address,
                                                     created_by_user_id=created_by_user_id,
                                                     nfr=nfr,
                                                     notes=notes)
    assert response.status_code != 404
    assert response.status_code != 500


def test_admin_update_product(me_client):
    product_id = 420
    response = me_client.license().admin_update_product(product_id=product_id)
    assert response.status_code != 404
    assert response.status_code != 500


def test_delete_product(me_client):
    product_id = 420
    response = me_client.license().delete_product(product_id=product_id)
    assert response.status_code != 404
    assert response.status_code != 500


def test_get_product_info(me_client):
    product_id = 420
    response = me_client.license().get_product_info(product_id=product_id)
    assert response.status_code != 404
    assert response.status_code != 500
