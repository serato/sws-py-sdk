from sws_py_sdk.sws import Sws
from sws_py_sdk.identity import Identity
import pytest

app_id = "MyClientId"

# Set up config
SERVICE_URI = {
    "id": "192.168.4.7"
}
def test_init_sws():
    """Check that SWS object cannot be initialised without app config"""
    with pytest.raises(Exception):
        client = Sws()
    
def test_init_sws_with_client_data():
    """Check that SWS object has app  config"""
    client = Sws(app_id=app_id, secret='myclientapppassword', service_uri=SERVICE_URI)
    assert client.app_id == app_id
    assert client.secret == 'myclientapppassword'
