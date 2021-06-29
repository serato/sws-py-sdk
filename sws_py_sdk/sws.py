""" This class is a representation of the Serato Web Services.
    The purpose is to improve the integration of Python with our APIs.
    Encapsulates the functionality required to communicate with the endpoints we provide.
    The definitions of each service will be contained in separate classes
"""
from sws_py_sdk import identity, license, ecom

service_uri_default = {
    'id': 'id.serato.com',
    'license': 'license.serato.com',
    'ecom': 'ecom.serato.com',
    # profile: 'profile.serato.com'
}


class Sws(object):

    def __init__(
        self,
        app_id,
        secret=None,
        user_id=0,
        timeout=3000,
        service_uri={},
        invalid_access_token_handler=None,
        test_env=False
    ):
        """
        Create SWS object
        config : object
            Configuration options
        appId : str
            Application ID
        secret : str
            Application secret
        user_id : int
            End user ID
        timeout : float
            Request timeout
        service_uri : object
            Base URIs for SWS services
        service_uri.id : str
            Base URI for SWS ID Service
        service_uri.license : str
            Base URI for SWS License Service
        auto_refresh : boolean
            Determines if the client will attempt to refresh the access token if invalid or expired.
        """
        self.app_id = app_id
        self.secret = secret
        self.user_id = user_id
        self.timeout = timeout
        self.access_token = ''
        self.refresh_token = ''
        self.service_uris = {
            'id': service_uri['id'] if 'id' in service_uri.keys() else service_uri_default['id'],
            'license': service_uri['license'] if 'license' in service_uri.keys() else service_uri_default['license'],
            'ecom': service_uri['ecom'] if 'ecom' in service_uri.keys() else service_uri_default['ecom']
        }

        self.service = {
            'id': identity.Identity(sws=self),
            'license': license.License(sws=self),
            'ecom': ecom.Ecom(sws=self)
            # Define more clients here
        }
        self.invalid_access_token_handler = invalid_access_token_handler
        self.test_env = test_env

    def identity(self):
        """ Getter for the id service instance """
        return self.service['id']

    def license(self):
        """ Getter for the license service instance """
        return self.service['license']

    def ecom(self):
        """ Getter for the ecom service instance """
        return self.service['ecom']
