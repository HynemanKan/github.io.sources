<template>
  <div class="markdown-body">
    <h1 style="border-bottom:none;">{{articleData.title}}</h1>

    <div style="display: inline-block">
      <p style="font-size: x-small">{{articleData.date}}</p>
      <el-tag type="info" effect="plain" style="margin-right: 5px;">分类: {{articleData.group}}</el-tag>
      <el-tag type="info" v-for="tag in articleData.tag" :key="tag" effect="plain" style="margin-right: 5px;">#{{ tag }}</el-tag>
    </div>
    <el-divider></el-divider>
    <MarkdownPreview :initialValue="article" theme="github"></MarkdownPreview>
  </div>
</template>

<script>
import { MarkdownPreview } from 'vue-meditor';
export default {
  name: "MdToArticle",
  data(){
    return {
      articleData:{}
    }
  },
  components:{
    MarkdownPreview
  },
  props:["article"],
  methods:{
    computeArticleData(art){
      var pattern = /\[[a-zA-Z]*\]:.*\r\n/g;
      var res = art.match(pattern);
      var newArticleData={}
      res.forEach(function (temp){
        var key = temp.split(":")[0].slice(1,-1);
        var value = temp.split(":")[1].replace(/\r\n/,"");
        newArticleData[key]=value;
      })
      if("tag" in newArticleData){
        newArticleData.tag=newArticleData.tag.split(",")
      }
      this.articleData=newArticleData;
      document.title=this.articleData.title;
    }
  },
  watch:{
    article(val,valNew){
      console.log(val,valNew);
      if(valNew == null){
        this.computeArticleData(val);
        return;
      }
      this.computeArticleData(valNew);
    }
  },
}
</script>

<style scoped>
.markdown-body{
  text-align: left;
}
.markdown-body >>> p {
  text-indent:2em !important;
}
.markdown-body >>> h1,h2,h3,h4,h5,h6 {
  border: none;
  margin-bottom: 10px;
}
</style>