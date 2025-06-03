import asyncio

class Response:
    def __init__(self, content=None, status_code=200):
        self.status_code = status_code
        self.headers = {}
        self._content = content

    def json(self):
        return self._content


class Request:
    def __init__(self, method, url, headers=None, body=None):
        self.method = method
        self.url = type('URL', (), {'path': url, 'query': '', 'url': url})
        self.headers = headers or {}
        self._body = body or {}
        self.cookies = {}
        self.client = type('client', (), {'host': 'test'})
        self.query_params = {}

    async def json(self):
        return self._body


class status:
    HTTP_204_NO_CONTENT = 204


class FastAPI:
    def __init__(self):
        self.routes = {'GET': {}, 'POST': {}}
        self._middleware = []

    def middleware(self, _):
        def decorator(func):
            self._middleware.append(func)
            return func
        return decorator

    def get(self, path, response_class=None):
        def decorator(func):
            self.routes['GET'][path] = func
            return func
        return decorator

    def post(self, path):
        def decorator(func):
            self.routes['POST'][path] = func
            return func
        return decorator


class HTMLResponse(Response):
    pass
