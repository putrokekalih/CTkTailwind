import json 
import pathlib
from typing import Iterable,Optional
from .cli import Cmd

class JsonManager:
    def __init__(self):
        self.__dirconf = pathlib.Path(__file__).parent.parent / "conf" 
        self.path_setting = self.__dirconf / "settings.conf"
        self.path_color = self.__dirconf / "color.json"
        self.__cmd = Cmd()

    def read_conf(self,path:pathlib.Path | str,default={}) -> Optional[dict | list[dict]]:
        """ load json conf """
        try :
            with open(path,mode="r",encoding="utf-8") as file :
                result =  json.load(file)
                self.__cmd.printLog(f"read {path.name} complete ! ",'success')
                self.__cmd.printOutput(msg=result,froms="xx",state=True)
        except (FileNotFoundError,json.JSONDecodeError) as e:
            result = default
            self.__cmd.printLog(f"read {path.name} with Errror return {default} ! ",'warning')
            self.__cmd.printOutput(msg=e,froms="xxxxxx",state=False)
        finally :
            return result

            
    @property 
    def readsetting(self) -> dict :
        return self.read_conf(self.path_setting,{})

    def write(self,data:Iterable | dict | list[dict] ,path:pathlib.Path|str) -> dict:
        try :
            with open(path,mode="w",encoding="utf-8") as file :
                json.dump(data,file,indent=4) 
        except Exception as e :
            pass
