<template>
  <el-card style="margin: 10px;">
    <div slot="header" class="clearfix">
      <span style="float: left;">标签</span>
    </div>
    <div>
      <div
          v-for="category in categories"
          :key="category.path"
          @click="jumpTo('/categories/'+category.path)"
          style="padding: 5px 0 5px 0;">
        <el-row justify="space-between" type="flex">
          <el-col :span="4">{{ category.name }}</el-col>
          <el-col :span="4">
            <el-tag type="info">{{ category.count }}</el-tag>
          </el-col>
        </el-row>
      </div>
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

</style>