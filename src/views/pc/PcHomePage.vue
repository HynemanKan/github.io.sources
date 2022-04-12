<template>
  <el-card style="margin: 10px;">
    <div style="text-align: left">
      <md-to-article :article.sync="article"></md-to-article>
    </div>
  </el-card>
</template>

<script>
// @ is an alias to /src


import MdToArticle from "@/components/MdToArticle";
export default {
  name: 'Home',
  components: {
    MdToArticle
  },
  data(){
    return{
      article:""
    }
  },
  created() {
    this.$axios.get("/data/article/bilibili-vertex-bot.md")
        .then(res=>{
          this.article=res.data;
        })
  }
}
</script>
