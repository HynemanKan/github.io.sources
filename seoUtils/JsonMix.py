import json
import re

def include(args):
    try:
        with open(args[0],"r",encoding="utf-8") as file:
            return True,json.loads(file.read())
    except Exception as e:
        return False,str(e)
COMMANDS={
    "include":include
}

def doJsonMix(src):
    if isinstance(src, dict):
        for key in src.keys():
            if isinstance(src[key], dict):
                doJsonMix(src[key])
            elif isinstance(src[key], str):
                src[key]=stringQuery(src[key])
            else:
                pass
    else:
        for i in range(len(src)):
            if isinstance(src[i], dict):
                doJsonMix(src[i])
            elif isinstance(src[i], str):
                src[i]=stringQuery(src[i])
            else:
                pass
    return src
def argFormat(s:str):
    if s[0] in "\'\"" and s[-1] in "\"\'":
        return s[1:-1]
    elif s.isdecimal():
        return int(s)
    raise AttributeError("unknown type")


def stringQuery(s:str):
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
        state,res = COMMANDS[commandName](args)
        if state:
            return res
        else:
            raise AttributeError(f"command {commandName} error:{res}")