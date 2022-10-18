""" This is the base class for the Web Service definitions -- includes common functions
"""
import json
from requests import Request, Session
from requests.auth import HTTPBasicAuth
from sws_py_sdk import firewall_header


class Service(object):
    def __init__(self, sws):
        """ Initializes the service object with a reference to the base SWS instance.
            sws : Sws instance
        """
        self.sws = sws
        self.service_uri = ''
        self.last_request = None
        self.invalid_access_token_handler = None
        self.FirewallHeader = firewall_header.FirewallHeader()

    def fetch(self,
              auth,
              endpoint,
              body={},
              params={},
              method='GET',
              timeout=None,
              headers={'Accept': 'application/json',
                       'Content-Type': 'application/json'}):
        """ Highest level function for handling requests
            auth : object | string
                Will either contain a configured form of authentication - like the well supported
                HTTPDigestAuth that is inbuilt to requests or  simply a string that will notify the
                service of which type of authentication to use.
            endpoint : string
                The URI path to send the request to
            body : dict
                If a GET request, will be used for the URL params.
                If a POST request this will be the data in the body of the packet.
            method : string
                The HTTP method
            timeout : float
                The time that the request will wait before timing out if there is
                no data from the server.
            headers : dict
                The headers that will be sent in the request

        """
        self.last_request = self.build_request(
            auth=auth,
            endpoint=('' if self.service_uri.find('://') != -1 else 'https://') + self.service_uri + endpoint,
            body=body,
            method=method,
            params=params,
            timeout=timeout,
            headers=headers)

        return self.fetch_request(self.last_request)

    def fetch_request(self, request):
        """ Responsible for taking the Request object and sending it - includes error handling
            request : Requests.Request
                The HTTP request that is being sent.
        """
        # First, prepare request
        session = Session()
        prepared_request = session.prepare_request(request)
        response = session.send(prepared_request)
        if not response.ok:
            data = response.json()
            if ((response.status_code == 403 and data['code'] == 2001)
                    or (response.status_code == 401 and data['code'] == 2002)):
                # Access token is invalid or expired
                # 403 2001 - Invalid access token
                # 401 2002 - Expired access token
                return self.sws.invalid_access_token_handler(self, response)

        return response

    def build_request(self, auth, endpoint, body, params, method, timeout, headers):
        """ Build up the request object.
            auth : object | string
                Will either contain a configured form of authentication - like the well supported
                HTTPDigestAuth that is inbuilt to requests or  simply a string that will notify the
                service of which type of authentication to use.
            endpoint : string
                The URI path to send the request to
            body : dict
                If a GET request, will be used for the URL params.
                If a POST request this will be the data in the body of the packet.
            method : string
                The HTTP method
            timeout : float
                The time that the request will wait before timing out if there is
                no data from the server.
            headers : dict
                The headers that will be sent in the request
        """

        request = Request(method=method, url=endpoint, headers=headers)

        if auth is 'bearer':
            request.headers['Authorization'] = f'Bearer {self.sws.access_token}'
        elif isinstance(auth, HTTPBasicAuth):
            request.auth = auth

        if method is 'GET' or method is 'DELETE':
            request.params = body

        if self.sws.test_env:
            request.headers.update(self.FirewallHeader.getHeader())

        # If test stack CDN credentials were provided, add the x-serato-cdn-auth header to the request
        if self.sws.cdn_auth_id and self.sws.cdn_auth_secret:
            request.headers.update(self.sws.get_cdn_auth_header())

        if method == 'PUT' or method == 'PATCH' or method == 'POST':
            if 'Content-Type' in headers and headers['Content-Type'] == 'application/x-www-form-urlencoded':
                request.data = body
            else:
                request.data = json.dumps(body)  # JSON in the body by default
            if params != {}:
                request.params = params
        return request
