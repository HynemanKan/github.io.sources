import json
import re

def include(args,this=None,parent=None):
    try:
        with open(args[0],"r",encoding="utf-8") as file:
            return True,json.loads(file.read())
    except Exception as e:
        return False,str(e)

def superMethod(args,this=None,parent=None):
    if not isinstance(parent,dict):
        raise AttributeError("parent should be a dict")
    if args[0] in parent.keys():
        return True,parent[args[0]]
    else:
        return False,f"key {args[0]} not in parent"
COMMANDS={
    "include":include,
    "super":superMethod
}

def doJsonMix(src,parent=None):
    if isinstance(src, dict):
        for key in src.keys():
            if isinstance(src[key], dict) or isinstance(src[key],list):
                doJsonMix(src[key],parent=src)
            elif isinstance(src[key], str):
                src[key]=stringQuery(src[key],this=src,parent=parent)
            else:
                pass
    else:
        for i in range(len(src)):
            if isinstance(src[i], dict):
                doJsonMix(src[i],parent=src)
            elif isinstance(src[i], str):
                src[i]=stringQuery(src[i],this=src,parent=parent)
            else:
                pass
    return src
def argFormat(s:str):
    if s[0] in "\'\"" and s[-1] in "\"\'":
        return s[1:-1]
    elif s.isdecimal():
        return int(s)
    raise AttributeError("unknown type")


def stringQuery(s:str,this=None,parent=None):
    if s[:2]!= "$$":
        return s
    else:
        commandName = re.match("\$\$[a-zA-Z]*",s)
        if commandName is None:
            raise AttributeError("syntax error,no command name not found")
        commandName = commandName.group()[2:]
        if commandName not in COMMANDS.keys():
            raise AttributeError("syntax error,no such command")
        argStr = re.search("\(.*\)",s)
        if argStr is None:
            raise AttributeError("syntax error,() not found")
        args = argStr.group()[1:-1].split(",")
        args = tuple(map(argFormat,args))
        state,res = COMMANDS[commandName](args,this=this,parent=parent)
        if state:
            return res
        else:
            raise AttributeError(f"command {commandName} error:{res}")