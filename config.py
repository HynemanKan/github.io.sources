SEO_TARGET={
    "templatePath": "./seoTemplate",
    "webRoot": "./dist",
    "insertPoint": "index.html",
    "seoRoot": "./seo",
    "template": "entry.html",
    "pages": [
        {
            "type": "singlePage",
            "template": "friendlyLink.html",
            "path": "./friendlyLink.html",
            "realPath":"/#/friendLink",
            "title":"友情链接",
            "data": {
                "title": "$$super('title')",
                "realPath":"$$super('realPath')",
                "friendlyLink": "$$include('./public/data/friendlyLink.json')"
            }
        }
    ]
}