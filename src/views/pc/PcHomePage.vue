<template>
  <el-card style="margin: 10px;">
    <el-empty :image="emptyImgUrl" description="施工中"></el-empty>
  </el-card>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  data(){
    return{
      article:"",
      emptyImgUrl:require("@/assets/empty.svg")
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
