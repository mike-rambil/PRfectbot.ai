import asyncio
from . import Request, Response


class TestClient:
    def __init__(self, app):
        self.app = app

    def post(self, path, json=None, headers=None):
        return asyncio.run(self._call("POST", path, json, headers))

    def get(self, path, json=None, headers=None):
        return asyncio.run(self._call("GET", path, json, headers))

    async def _call(self, method, path, body, headers):
        handler = self.app.routes[method].get(path)
        if not handler:
            return Response(status_code=404)
        req = Request(method, path, headers=headers, body=body)
        # apply middleware
        call = handler
        for mw in reversed(self.app._middleware):

            async def next_call(request, mw=mw, call=call):
                return await mw(request, call)

            call = next_call
        resp = await call(req)
        if isinstance(resp, dict):
            return Response(resp)
        return resp
