<template>
  <el-card style="margin: 10px;">
    <div>
      <el-avatar :size="100" src="/image/avatar.jpg"></el-avatar>
    </div>
    <div style="margin: 5px"><h2>Hyneman</h2></div>
    <el-row justify="space-around" type="flex">
      <el-col v-for="item in statistics" :key="item.name">
        <h3>{{ item.count }}</h3>
        <p style="font-size: small">{{ item.name }}</p>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
export default {
  name: "PcAvatarCard",
  props:["statistics"]
}
</script>

<style scoped>

</style>