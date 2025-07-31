from rich.console import Console
from rich.panel import Panel
from rich.traceback import install
from rich import box
from random import choice


class Notify :
    def __init__(self,debug=True,log=True):
        install()
        self.__debug = debug
        self.__log = log
        self.console = Console()
        self.logsetting = {
            "success":['✅','green'],
            "fail":["❌",'red'],
            "warning":['⚠️',"yellow"],
            "info":['💭', 'blue']
        }

    def printLog(self,message,type_="info",**kwargs):
        """
            message :   str (helloworld)
            type_   :   success,info,fail,warning
            kwargs  :   msg:str,froms:func,state:bool
        """
        if not self.__log:
            return
        self.console.print(f"🚥 [{self.logsetting[type_][1]}][bold]{type_.upper()}{self.logsetting[type_][0]} [/][/] ~> [{self.logsetting[type_][1]}] {message.capitalize()}")
        if isinstance(kwargs,dict) and kwargs:
            self.printOutput(**kwargs)
            
    def printOutput(self,msg:str,froms:callable,state:bool=None,subtitle:str=None):
        if not self.__debug:
            return 
        
        try :
            froms = str(froms.__name__).capitalize()
        except (ValueError,AttributeError):
            froms = "CtkTailwind".capitalize()

        if not isinstance(subtitle,str):
            subs = "Action failed" if isinstance(state,bool) and not state else "Action module completed" if isinstance(state,bool) and state else "Information output"
        else : subs = subtitle

        style = "red" if isinstance(state,bool) and not state else "green" if isinstance(state,bool) and state else "blue"
        list_box = [
            x for x in dir(box)
            if not x.startswith("_") and isinstance(getattr(box, x), box.Box)
        ]
        rand_box = choice(list_box)
        boxs = getattr(box,rand_box)
        

        conf = {"renderable"        :       f"[{style}]{msg.capitalize()}",
                "title"             :       f"[white] Output {froms} : ",
                "subtitle"          :       f"[white]{subs.capitalize()}",
                "style"             :       style,
                "expand":False,
                "padding":(5,10)}
        try :
            INNER = Panel(box=boxs,**conf)
        except AttributeError:
            boxs = box.SQUARE_DOUBLE_HEAD
            INNER = Panel(box=boxs,**conf)
        self.console.print(INNER)

