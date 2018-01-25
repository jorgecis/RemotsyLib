#!/usr/local/bin/python3.5
from aiohttp import (ClientSession, TCPConnector, BasicAuth)
from asyncio import get_event_loop
from yarl import urljoin

class Requests():
    """
        @param `proxy`: use proxy in session if passed
    """

    async def do_get(self, url, data=None):
        async with ClientSession() as session:
            async with session.get(url, json=data) as response:
                j_resp = await response.json()
                return j_resp

    async def do_post(self, url, data=None):
        async with ClientSession() as session:
            async with session.post(url, json=data) as response:
                j_resp = await response.json()
                return j_resp

class API():

    def __init__(self, api_url='https://remotsy.com/rest/'):
        self.api_url = api_url
        self.requests = Requests()
        self.auth_key = None

    async def post(self, partial_url=None, data=None):
        try:
            if partial_url is not None:
                if self.auth_key is not None:
                    data['auth_key'] = self.auth_key
                endpoint = urljoin(self.api_url, partial_url)
                response = await self.requests.do_post(url=endpoint, data=data)
                return response
        except Exception as e:
            return dict(error='API Error', message=e, status=409)

    async def login(self, auth=dict(username=None, password=None)):
        if auth['username'] is not None and auth['password'] is not None:
            login_status = await self.post(partial_url='session/login', data=auth)
            print(login_status)
            if login_status['status'] == 'success':
                self.auth_key = login_status['data']['auth_key']
                return login_status
        return dict(error='Login', message='No credentials!', status=401)

    async def list_controls(self):
        controls_list = await self.post('controls/list', data={})
        if controls_list['status'] == 'success':
            return controls_list['data']['controls']
        return dict(error='List Controls', message='No controls found', status=409)


