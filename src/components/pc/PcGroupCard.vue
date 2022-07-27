<template>
  <el-card style="margin: 10px;">
    <div slot="header" class="clearfix">
      <span style="float: left;">分类</span>
    </div>
    <div>
      <div
          v-for="group in groupData"
          :key="group.name"
          @click="jumpTo(group.path)"
          style="padding: 5px 0 5px 0;">
        <el-row justify="space-between" type="flex">
          <el-col :span="4">{{ group.name }}</el-col>
          <el-col :span="4">
            <el-tag type="info">{{ group.count }}</el-tag>
          </el-col>
        </el-row>
      </div>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "PcGroupCard",
  props:["groupData"],
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