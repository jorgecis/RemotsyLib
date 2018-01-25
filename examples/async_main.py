from aiohttp.web import (Application, run_app, View, json_response)
from asyncio import (get_event_loop, set_event_loop_policy)
from remotsylib.api_async import API

remotsy = API()

class Login(View):
    async def post(self):
        args = await self.request.json()
        username_arg = args.get('username', None)
        password_arg = args.get('password', None)
        self.request.app['remotsy_auth'] = await remotsy.login(auth=dict(username=username_arg, password=password_arg))
        return json_response(self.request.app['remotsy_auth'], status=200)

class List_Controls(View):
    async def post(self):
        data = dict(auth_key=self.request.app['remotsy_auth'])
        controls = await remotsy.list_controls()
        return json_response(controls, status=200)

def bind_routes_to_server(app):
    app.router.add_post('/login', Login)
    app.router.add_post('/list_controls', List_Controls)

def make_server(close=False):
    app = Application()
    app['remotsy_auth'] = None
    bind_routes_to_server(app)
    loop = get_event_loop()
    loop.close() if close else None
    loop.create_server(run_app(app, port=8080))
    loop.run_forever()

def main():
    try:
        make_server()
    except KeyboardInterrupt:
        make_server(close=True)
    except Exception as e:
        print('Application Error: {}'.format(e))
        make_server(close=True) 

if __name__ == "__main__":
    main()