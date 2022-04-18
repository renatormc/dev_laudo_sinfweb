import requests
from datetime import datetime
import jwt
from database import repo

class TokenExpiredException(Exception):
    pass


class TokenNoFoundException(Exception):
    pass


class Requester:

    def __init__(self):
        self.token = ""
        self.__load_token()

    def __load_token(self):
        now = datetime.now()
        token = repo.get_token("sinfweb")
        if not token:
            raise TokenNoFoundException("Token not found")
        headers = jwt.get_unverified_header(token)
        try:
            if headers['exp'] < datetime.timestamp(now):
                raise TokenExpiredException("Expired token")
        except KeyError:
            pass
        self.token = token

    def get(self, url, headers={}, *args, **kargs):
        headers['Authorization'] = f"Bearer {self.token}"
        return requests.get(url, headers=headers, *args, **kargs)

    def post(self, url, headers={}, *args, **kargs):
        headers['Authorization'] = f"Bearer {self.token}"
        return requests.post(url, headers=headers, *args, **kargs)

    def delete(self, url, headers={}, *args, **kargs):
        headers['Authorization'] = f"Bearer {self.token}"
        return requests.delete(url, headers=headers, *args, **kargs)

    def patch(self, url, headers={}, *args, **kargs):
        headers['Authorization'] = f"Bearer {self.token}"
        return requests.patch(url, headers=headers, *args, **kargs)
