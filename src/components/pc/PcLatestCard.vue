<template>
  <el-card style="margin: 10px;">
    <div slot="header" class="clearfix">
      <span style="float: left;">最近文章</span>
    </div>
    <div>
      <div
          v-for="article in LatestArticle"
          :key="article.path">
        <p style="font-size: x-small;text-align: left">{{article.date}}</p>
        <p class="articleTitle" @click="jumpTo('/article/'+article.path)">{{ article.title }}</p>
        <el-divider></el-divider>
      </div>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "PcLatestCard",
  methods: {
    jumpTo(href) {
      console.log(href)
      this.$router.replace(href);
    }
  },
  props:["LatestArticle"],
}
</script>

<style scoped>
  .articleTitle{
    font-size: medium;text-align: left;
  }
  .articleTitle:hover{
    color: #409EFF;
  }
</style>