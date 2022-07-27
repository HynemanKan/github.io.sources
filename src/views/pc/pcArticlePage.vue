<template>
  <el-card style="margin: 10px;">
    <div>
      <MdToArticle :article.sync="article"></MdToArticle>
    </div>
  </el-card>
</template>

<script>
import MdToArticle from "@/components/MdToArticle";
export default {
  name: "pcArticlePage",
  components: {MdToArticle},
  data(){
    return{
      article:null
    }
  },
  mounted() {
      this.$axios.get("/data/article/"+this.$route.params.articleName)
          .then(res=>{
            this.article=res.data;
          })
  }
}
</script>

<style scoped>

</style>