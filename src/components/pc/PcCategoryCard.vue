<template>
  <el-card style="margin: 10px;">
    <div slot="header" class="clearfix">
      <span style="float: left;">标签</span>
    </div>
    <div class="tagsBlock">
        <el-button type="text" v-for="tag in categories" :key="tag.name" class="tag">#{{tag.name}}</el-button>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "PcCategoryCard",
  props:["categories"],
  methods: {
    jumpTo(href) {
      console.log(href)
      this.$router.replace(href);
    }
  },
}
</script>

<style scoped>
.tagsBlock{
  float: left;
  margin-bottom: 20px;
}
.tag {
  margin-right: 10px;
  display: inline-block;
  color: #909399;
}
</style>