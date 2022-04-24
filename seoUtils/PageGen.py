import os
from pathlib import Path
from jinja2 import Environment
from .PathCheckCreate import pathCheckCreate

class PageGen:
    def __init__(self,seoTarget:dict,env:Environment):
        self.seoTarget= seoTarget
        self.env = env
        self.pageGenMethod={}
        self.webRoot = seoTarget["webRoot"]
        self.seoRoot = seoTarget["seoRoot"]
        self.insertPoint = Path(os.getcwd()).joinpath(self.webRoot).joinpath(seoTarget["insertPoint"])
        self.methodInit()

    def methodInit(self):
        self.pageGenMethod["singlePage"]=self._singlePageGen

    def _singlePageGen(self, target:dict):
        outPagePath = Path(self.webRoot).joinpath(self.seoRoot).joinpath(target["path"])
        template = self.env.get_template(target["template"])
        outHtml = template.render(**target["data"])
        pathCheckCreate(outPagePath)
        with open(outPagePath,"w",encoding="utf-8") as file:
            file.write(outHtml)
        print(f'gen page {Path(self.seoRoot).joinpath(target["path"])} name as {target["title"]}')
        return Path(self.seoRoot).joinpath(target["path"]),target["title"]

    def genPage(self,target:dict):
        if target["type"] not in self.pageGenMethod.keys():
            raise AttributeError("page gen method not found")
        return self.pageGenMethod[target["type"]](target)

    def gen(self):
        links=[]
        for page in self.seoTarget["pages"]:
            url,name = self.genPage(page)
            links.append({
                "url":url,
                "name":name
            })
        template = self.env.get_template("entry.html")
        outHtml = template.render(links=links)
        with open(self.insertPoint,"r",encoding="utf-8") as file:
            source = file.read()
        source = source.replace("{% seoInsert %}",outHtml)
        with open(self.insertPoint,"w",encoding="utf-8") as file:
            file.write(source)
        print(f"entry Insert to {Path(self.webRoot).joinpath(self.seoTarget['insertPoint'])}")


