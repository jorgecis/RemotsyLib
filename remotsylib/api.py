from json import dumps, loads
from sys import exit
from urllib2 import Request, urlopen, HTTPError, URLError


class API():
    
    def __init__(self, apiurl = "https://remotsy.com/rest/"):
        self.apiurl = apiurl
        self.auth_key = None

    def post(self, url, data):
        req = Request(self.apiurl + url)
        req.add_header('Content-Type', 'application/json')
        if self.auth_key is not None:
           data["auth_key"] = self.auth_key
        try:
            resp = urlopen(req, dumps(data))
        except HTTPError as e:
            print e
            exit(-1)
        except URLError as e:
            print e
            exit(-2)
        else:
            body = loads(resp.read())
            return  body

    def login(self, username, password):
        data = {"username": username,
                "password": password}

        self.auth_key = None
        ret = self.post("session/login",  data)
        if ret["status"] == "success":
            self.auth_key = ret["data"]["auth_key"]
        return self.auth_key

    def list_controls(self):
        ret = self.post("controls/list",{})
        if ret["status"] == "success":
            return ret["data"]["controls"]
        else:
            return None

    def list_buttons(self, idctl):
        ret = self.post("controls/get_buttons_control",{"id_control": idctl})
        if ret["status"] == "success":
            return ret["data"]["buttons"]
        else:
            return None

    def blast(self, iddev, idbto, ntime = 1):
        ret = self.post("codes/blast",{"id_dev": iddev, "code": idbto, "ntime": ntime})
        if ret["status"] == "success":
            return True
        else:
            return False


