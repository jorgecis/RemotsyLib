#!/usr/local/bin/python3.5
from aiohttp import (ClientSession, TCPConnector, BasicAuth)
from asyncio import get_event_loop
from async_timeout import timeout as aio_timeout
from yarl import urljoin

class Requests():
    """
        @param `proxy`: use proxy in session if passed
    """

    def __init__(self, proxy=None):
        self.session = self.setup_session()
        self.proxy = proxy

    def __del__(self):
        self.session.close()

    def setup_session(self, custom_headers=None, login=None):
        conn = TCPConnector()
        if login:
            session = ClientSession(connector=conn, headers=custom_headers, auth=BasicAuth(login['login'], login['password']))
        else:
            session = ClientSession(connector=conn, headers=custom_headers)
        return session

    async def do_get(self, url, data=None):
        with aio_timeout(10):
            async with self.session.get(url, proxy=self.proxy, json=data) as response:
                j_resp = await response.json()
                return j_resp

    async def do_post(self, url, data=None):
        with aio_timeout(10):
            async with self.session.post(url, proxy=self.proxy, json=data) as response:
                j_resp = await response.json()
                return j_resp

    async def close_session(self):
        await self.session.close()
        return None

class API():

    def __init__(self, api_url='https://remotsy.com/rest/', auth=dict(username=None, password=None)):
        self.api_url = api_url
        self.user = auth['username']
        self.passwd = auth['password']
        self.loop = get_event_loop()
        self.auth_key = self.loop.run_until_complete(loop.create_task(self.login()))
        self.requests = Requests()

    async def post(self, partial_url=None, data=None):
        try:
            if partial_url is not None:
                endpoint = urljoin(self.api_url, partial_url)
                response = await self.requests.do_post(url=endpoint, data=data)
                return response
        except Exception as e:
            return dict(error='API Error', message=e, status=409)

    async def login(self):
        if self.user is not None and self.passwd is not None:
            credentials = dict(username=self.user, password=self.passwd)
            login_status = await self.post(partial_url='session/login', data=credentials)
            if login_status['status'] == 'success':
                self.auth_key = login_status['data']['auth_key']
                return self.auth_key
        return dict(error='Login', message='No credentials!', status=401)

    async def list_controls(self):
        controls_list = await self.post('controls/list', data={})
        if controls_list['status'] == 'success':
            return controls_list['data']['controls']
        return dict(error='List Controls', message='No controls found', status=409)
            


if __name__ == "__main__":
    from asyncio import get_event_loop
    from time import sleep
    loop = get_event_loop()
    api = API(auth=dict(username='jasmit.tarang92@gmail.com', password='1234'))
    print(api.auth_key)
    #login = loop.create_task(api.login())
    #controls = loop.create_task(api.list_controls())
    #loop.run_until_complete(login)
    #loop.run_until_complete(controls)
    