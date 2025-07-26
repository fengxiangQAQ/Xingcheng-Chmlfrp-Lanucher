import urllib.request
import urllib.parse
import http.client
import json as p_json

class re_requests:

    def __init__(self,re_requests:http.client.HTTPResponse):
        self.content=re_requests.read()

    def json(self)->str:
        return p_json.loads(self.content)

class request:

    _headers = {
        "user-agent": "fx-xcl/test"
    }

    @classmethod
    def _requests(cls,Request:urllib.request.Request):
        return urllib.request.urlopen(Request)

    @classmethod
    def get(cls,url:str,params:dict=None)->re_requests:
        if params is not None:
            qs=urllib.parse.urlencode(params)
            url+="?"+qs
        Request=urllib.request.Request(url, headers=cls._headers)
        return re_requests(cls._requests(Request))

    @classmethod
    def post(cls,url:str,json:dict=None):
        if json is not None:
            _json=bytes(p_json.dumps(json).encode("utf-8"))
            Request = urllib.request.Request(url,data=_json, headers=cls._headers)
        else:
            Request = urllib.request.Request(url,data=bytes(), headers=cls._headers)
        return re_requests(cls._requests(Request))