import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from seoUtils import doJsonMix,PageGen
from config import SEO_TARGET

print("start seo optimize")
# json data Join
seoTarget = doJsonMix(SEO_TARGET)
# jinja init
env = Environment(loader=FileSystemLoader(Path(os.getcwd()).joinpath(SEO_TARGET["templatePath"])))
pageGen = PageGen(seoTarget,env)
pageGen.gen()
print("seo optimize finish")