from typing import Tuple

from core.utils.network.requests import request

class APIv2:

    url="https://cf-v2.uapis.cn"

    @classmethod
    def login(cls,username:str,password:str)->dict:
        data=request.get(cls.url+"/login",{
            "username":username,
            "password":password
        }).json()
        if data["code"]==200:
            return data["data"]
        else:
            return None
    @classmethod
    def getUserTunnelList(cls,usertoken:str)->dict:
        data=request.get(cls.url+"/tunnel",{
            "token":usertoken
        }).json()
        if data["code"]==200:
            redata={}
            for i in data["data"]:
                redata[i["id"]]=i
            return redata
        else:
            return None
    
    @classmethod
    def getUserInfo(cls,usertoken:str)->dict:
        data=request.get(cls.url+"/userinfo",{
            "token":usertoken
        }).json()
        if data["code"]==200:
            return data["data"]
        else:
            return None
        
    @classmethod
    def delTunnel(cls,usertoken:str,tunnelID:int)->Tuple[bool,str]:
        data:dict=request.get(cls.url+"/delete_tunnel",{
            "tunnelid":tunnelID
        },{"authorization":f"Bearer {usertoken}"}).json()
        if data["code"]==200:
            return (True,data["msg"])
        else:
            return (False,data["msg"])
        
class APIv1:
    
    url="https://cf-v1.uapis.cn/api"

    @classmethod
    def reToken(cls,usertoken:str)->str:
        data:dict=request.get(cls.url+"/userinfo",{
            "token":usertoken
        }).json()
        if "newToken" in data.keys():
            return data["newToken"]
        else:
            return None