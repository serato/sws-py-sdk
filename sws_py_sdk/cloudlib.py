""" This file exposes endpoints from the SWS Cloud Libary Service
"""

from sws_py_sdk.service import Service

class Cloudlib(Service):

    def post_file(self, post_file=''):
        """ Post a file
        """

        endpoint = '/api/v1/me/files'
        return self.fetch(
            auth='bearer',
            endpoint=endpoint,
            body={"post_file": post_file},
            method='POST',
        )

    def post_file_id(self, post_file_id=''):
        """ Post a file id
        """
        
        endpoint = '/api/v1/user/files/:file_id'
        return self.fetch(
            auth='bearer',
            endpoint=endpoint,
            body={"post_file_id": post_file_id},
            method='POST',
        )

    def get_file(self, get_file=''):
        """ Get a file
        """

        endpoint = '/api/v1/me/files'
        return self.fetch(
            auth='bearer',
            endpoint=endpoint,
            body={"get_file": get_file},
            method='GET',
        )

    def get_file_id(self, get_file_id=''):
        """ Get a file id
        """
        endpoint = '/api/v1/user/files/:file_id'
        return self.fetch(
            auth='bearer',
            endpoint=endpoint,
            body={"get_file_id": get_file_id},
            method='GET',
        )
