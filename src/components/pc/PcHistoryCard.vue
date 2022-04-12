<template>
  <el-card style="margin: 10px;">
    <div slot="header" class="clearfix">
      <span style="float: left;">归档</span>
    </div>
    <div>
      <div
          v-for="year in historyData"
          :key="year.name"
          @click="jumpTo('/history/'+year.name)"
          style="padding: 5px 0 5px 0;">
        <el-row justify="space-between" type="flex">
          <el-col :span="4">{{ year.name }}</el-col>
          <el-col :span="4">
            <el-tag type="info">{{ year.count }}</el-tag>
          </el-col>
        </el-row>
      </div>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "PcHistoryCard",
  props:["historyData"],
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