import json
import urllib2
import sys


class Api():
    def __init__(self, apiurl = "https://remotsy.com/rest/"):
        self.apiurl = apiurl
        self.auth_key = None


    def post(self, url, data):
        req = urllib2.Request(self.apiurl + url)
        req.add_header('Content-Type', 'application/json')
        if self.auth_key is not None:
           data["auth_key"] = self.auth_key
        try:
            resp = urllib2.urlopen(req, json.dumps(data))
        except urllib2.HTTPError as e:
            print e
            sys.exit(-1)
        except urllib2.URLError as e:
            print e
            sys.exit(-2)
        else:
            body = json.loads(resp.read())
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
