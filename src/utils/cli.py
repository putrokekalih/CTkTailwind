from rich.console import Console
from rich.panel import Panel
from rich.traceback import install
from rich import box
from random import choice
import json,pathlib



class Init_cmd:
    def __init__(self):
        self.state()

    def state(self):
        try :
            path_setting = pathlib.Path(__file__).parent.parent /"conf"/"settings.conf"
            with open(path_setting,mode="r",encoding="utf-8") as file :
                result:dict = json.load(file)
                key:dict = result.get("cli")
                return [x for x in key.values()]
        except (AttributeError,KeyError):
            return [False,False]
        


class Cmd:
    def __init__(self):
        install()
        self.__debug,self.__log= Init_cmd().state()
        self.console = Console()
        self.logsetting = {
            "success":['✅','yellow'],
            "fail":["❌",'purple'],
            "warning":['⚠️',"green"],
            "info":['💭', 'blue']
        }
        

    def printLog(self,message,type_="info",**kwargs):
        """
            message :   str (helloworld)
            type_   :   success,info,fail,warning
            kwargs  :   msg:str,froms:func,state:bool
        """
        if self.__log :
            self.console.print(f"🚥 [{self.logsetting[type_][1]}][bold]{type_.upper()}{self.logsetting[type_][0]} [/][/] ~> [{self.logsetting[type_][1]}] {message.capitalize()}")
            if isinstance(kwargs,dict) and kwargs:
                input(kwargs)
                self.printOutput(**kwargs)
        else :
            pass
            
    def printOutput(self,msg:str,froms:callable,state:bool=None,subtitle:str=None):
        if self.__debug :
            msg = str(msg)
            try :
                froms = str(froms.__name__).capitalize()
            except (ValueError,AttributeError):
                froms = "CtkTailwind".capitalize()

            if not isinstance(subtitle,str):
                subs = "Action failed" if isinstance(state,bool) and not state else "Action module completed" if isinstance(state,bool) and state else "Information output"
            else : subs = subtitle

            style = "purple" if isinstance(state,bool) and not state else "yellow" if isinstance(state,bool) and state else "blue"
            list_box = [
                x for x in dir(box)
                if not x.startswith("_") and isinstance(getattr(box, x), box.Box)
            ]
            rand_box = choice(list_box)
            
            conf = {"renderable"        :       f"[{style}]{msg.capitalize()}",
                    "title"             :       f"[white] Output {froms} : ",
                    "subtitle"          :       f"[white]{subs.capitalize()}",
                    "style"             :       style,
                    "expand":False}
            try :
                INNER = Panel(**conf,box = getattr(box,rand_box))
            except AttributeError:
                INNER = Panel(**conf)
            finally:
                self.console.print(INNER)
        else :
            pass

