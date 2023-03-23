""" This file exposes endpoints from the SWS Cloud Libary Service
"""

from sws_py_sdk.service import Service

class Cloudlib(Service):

    def __init__(self, sws):
        super().__init__(sws)
        self.service_uri = sws.service_uris['cloudlib']

    def me_create_file_upload(self, md5_hash, mime_type, size, name=None):
        """ Post a file via /api/v1/files endpoint
            user_id : int
                MD5hash base64 encoding            
            md5_hash : str
                MD5hash base64 encoding
            mime_type : str
                File mime type
            size : int
                Size of the file
            name : str
                name of the file
        """

        endpoint = f'/api/v1/me/files'
        return self.fetch(
            auth='bearer',
            endpoint=endpoint,
            body={"md5_hash": md5_hash, "mime_type": mime_type, "size": size, "name": name},
            method='POST',
        )

    def user_create_file_upload(self, user_id, md5_hash, mime_type, size, name=None):
        """ Post a file id via /api/v1/users/{user_id}/files endpoint
            user_id : int
                MD5hash base64 encoding            
            md5_hash : str
                MD5hash base64 encoding
            mime_type : str
                File mime type
            size : int
                Size of the file
            name : str
                name of the file
        """
        
        endpoint = f'/api/v1/users/{user_id}/files'
        return self.fetch(
            auth='bearer',
            endpoint=endpoint,
            body={"md5_hash": md5_hash, "mime_type": mime_type, "size": size, "name": name},
            method='POST',
        )

    def me_get_file(self, file_id):
        """ Get file via /api/v1/users/{user_id}/files/:file_id endpoint
        """

        endpoint = f'/api/v1/me/files/{file_id}'
        return self.fetch(
            auth='bearer',
            endpoint=endpoint,
            method='GET',
        )

    def user_get_file(self, file_id, user_id):
        """ Get file id via /api/v1/files/:file_id endpoint
        """
        endpoint = f'/api/v1/users/{user_id}/files/{file_id}'
        return self.fetch(
            auth='bearer',
            endpoint=endpoint,
            method='GET',

        )
