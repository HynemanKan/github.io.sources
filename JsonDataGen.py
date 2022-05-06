import json
import re
from pathlib import Path
from urllib.parse import quote

targetdir="./public/data/article"
categoriesMax = 5
articles=[]
for article in Path(targetdir).rglob('*.md'):
    a={}
    a["path"] = article.as_posix()
    a["name"] = article.name
    a["charCount"]=0
    with open(article,'r',encoding="utf-8") as file:
        for line in file.readlines():
            if re.match("\[[a-zA-Z]*]:.*",line) is None:
                a["charCount"] += len(line.strip())
                continue
            key = line.split(":")[0][1:-1]
            value = ":".join(line.split(":")[1:]).replace("\n", "")
            a[key]=value

    articles.append(a)
articles.sort(key=lambda x:x["date"])
print(articles)


#categories
categories={}
for a in articles:
    tags = set(a['tag'].split(","))
    for tag in tags:
        if tag in categories.keys():
            categories[tag]+=1
        else:
            categories[tag]=1
print(categories)
categoriesOut = []
for key in categories.keys():
    categoriesOut.append({
        "name":key,
        "path":f"/category/{quote(key,encoding='gb2312')}",
        "count":categories[key]
    })
categoriesOut.sort(key=lambda x:x["count"], reverse=True)
print(categoriesOut)
with open("public/data/index/categories.json","w",encoding="utf-8") as file:
    file.write(json.dumps(categoriesOut))

#group
groupNames=[]
for a in articles:
    if a["group"] not in groupNames:
        groupNames.append(a["group"])
groups = []
for g in groupNames:
    groups.append({
        "name":g,
        "path":f"/group/{quote(g,encoding='utf-8')}"
    })
with open("public/data/index/groups.json","w",encoding="utf-8") as file:
    file.write(json.dumps(groups))


#statistics
statistics=[]
statistics.append({
    "name":"文章",
    "count": str(len(articles))
})
statistics.append({
    "name":"标签",
    "count": str(len(categoriesOut))
})
charCount =sum(map(lambda x:x['charCount'],articles))/1000
if charCount>10:
    charCountStr = round(charCount)
else:
    charCountStr = round(charCount,1)
statistics.append({
    "name":"字数",
    "count":"{}k".format(charCountStr)
})
statistics.append({
    "name":"分类",
    "count":len(groups)
})
print(statistics)
with open("public/data/index/statistics.json","w",encoding="utf-8") as file:
    file.write(json.dumps(statistics))
#latestArticle
latestArticle=articles[:3]
with open("public/data/index/latestArticle.json",'w',encoding="utf-8") as file:
    file.write(json.dumps(latestArticle))

