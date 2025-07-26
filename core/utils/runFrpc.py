import os

def runFrpc(frpcPath:str,runDir:str,userToken:str,tunnelID:str)->None:
    with open(runDir+"\lastLanucher.bat","w") as file:
        file.write(f"@echo off\n\"{frpcPath}\" -u {userToken} -p {tunnelID}\npause\nexit")
    os.system(f"start \"frpc-{tunnelID}\" {runDir}\lastLanucher.bat")