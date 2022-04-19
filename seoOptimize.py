import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from seoUtils import doJsonMix,PageGen
from config import SEO_TARGET

# json data Join
doJsonMix(SEO_TARGET)
# jinja init
env = Environment(loader=FileSystemLoader(Path(os.getcwd()).joinpath(SEO_TARGET["templatePath"])))
pageGen = PageGen(SEO_TARGET,env)
pageGen.gen()
