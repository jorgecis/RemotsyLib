# /usr/bin/python3.6
""" Remotsy async Python API """
from asyncio import get_event_loop
from aiohttp.web import (Application, run_app, View, json_response)
from remotsylib.api_async import API


class Login(View):
    """ Our login function"""

    async def post(self):
        """ POST """
        args = await self.request.json()
        username_arg = args.get('username', None)
        password_arg = args.get('password', None)
        self.request.app['remotsy_auth'] = await API().login(auth=dict(
            username=username_arg, password=password_arg))
        return json_response(self.request.app['remotsy_auth'], status=200)


class ListControls(View):
    """ Lists all the Controls """

    async def post(self):
        """ POST """
        #data = dict(auth_key=self.request.app['remotsy_auth'])
        controls = await API().list_controls()
        return json_response(controls, status=200)


def bind_routes_to_server(app):
    """ Binds all the routes to the server """
    app.router.add_post('/login', Login)
    app.router.add_post('/list_controls', ListControls)


def make_server(close=False):
    """ Creates the server """

    app = Application()
    app['remotsy_auth'] = None
    bind_routes_to_server(app)
    loop = get_event_loop()
    _ = loop.close() if close else None
    loop.create_server(run_app(app, port=8080))
    loop.run_forever()


def main():
    """ runs the server """
    try:
        make_server()

    except KeyboardInterrupt:
        make_server(close=True)

if __name__ == "__main__":
    main()
