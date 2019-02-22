# /usr/bin/python3.6
""" Python3+ async Remotsy API """
from aiohttp import ClientSession
from yarl import urljoin
from asyncio import get_event_loop, ensure_future


class Requests():
    """ Generic Get/Post request client """

    async def do_get(self, url, data=None):
        """ Get request """
        async with ClientSession() as session:
            async with session.get(url, json=data) as response:
                j_resp = await response.json()
                return j_resp

    async def do_post(self, url, data=None):
        """ Post request """
        async with ClientSession() as session:
            async with session.post(url, json=data) as response:
                j_resp = await response.json()
                return j_resp


class API():
    """ This is the main API  """

    def __init__(self, api_url='https://remotsy.com/rest/', auth_key=None):
        self.api_url = api_url
        self.requests = Requests()
        self.auth_key = auth_key

    async def post(self, partial_url=None, data=None):
        """ Carries out the request to Remotsy's server """
        try:
            if partial_url is not None:
                if self.auth_key is not None:
                    data['auth_key'] = self.auth_key
                endpoint = urljoin(self.api_url, partial_url)
                response = await self.requests.do_post(url=endpoint, data=data)
                return response
        except KeyError as error:
            return dict(error='API Error', message=error, status=409)

    async def login(self, auth=None):
        """ Login and recieve a api key """
        if auth is not None:
            login_status = await self.post(
                partial_url='session/login', data=auth)
            print(login_status)
            if login_status['status'] == 'success':
                self.auth_key = login_status['data']['auth_key']
                return login_status
        return dict(error='Login', message='No credentials!', status=401)

    async def list_controls(self):
        """ List all the controls available """
        controls_list = await self.post('controls/list', data={})
        if controls_list['status'] == 'success':
            return controls_list['data']['controls']
        return dict(
            error='List Controls', message='No controls found', status=409)

    async def list_buttons(self, controller_id):
        """  List all buttons for a specific controller """
        buttons = await self.post(
            'controls/get_buttons_control', dict(id_control=controller_id))
        if buttons['status'] == 'success':
            return buttons['data']['buttons']
        return dict(
            error='List Buttons', message='No Controller ID', status=409)

    async def blast(self, device_id, button_id, ntime=1):
        """ Blast a button to a device nTimes """
        blast_resp = await self.post(
            'codes/blast', dict(id_dev=device_id, code=button_id, ntime=ntime))
        if blast_resp['status'] == 'success':
            return blast_resp
        return dict(error='IR Blast', message=False, status=409)

    async def list_routines(self):
        """ List all the routines available """
        routines = await self.post('routines/list', data={})
        if routines['status'] == 'success':
            return routines
        return dict(error='List Routines', message=False, status=409)

    async def play_routine(self, routine_id):
        """ Play a specific routine """
        played = await self.post('routines/play_routine', dict(idroutine=routine_id))
        if played['status'] == 'success':
            return played
        return dict(error='Play Routine', message=False, status=409)

    async def blink_led(self, device_id):
        """ blink Remotsy's led """
        blink = await self.post('devices/blink', dict(id_dev=device_id))
        if blink['status'] == 'success':
            return blink
        return dict(error='Blink LED', message=False, status=409)

    async def update_firmware(self, device_id):
        """ Update Remotsy's firmware """
        fw_update = await self.post('devices/updatefirmware', dict(id_dev=device_id))
        if fw_update['status'] == 'success':
            return fw_update
        return dict(error='Firmware Update', message=False, status=409)


def run_remotsy_api_call(api_call=None):
    if api_call is not None:
        return get_event_loop().run_until_complete(api_call)
    raise ValueError('api_call is not defined!')

