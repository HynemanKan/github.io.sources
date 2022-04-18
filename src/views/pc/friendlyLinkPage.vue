<template>
<div>
  <el-card v-for="friendlyLink in friendlyLinks" :key="friendlyLink.url" style="margin-top: 10px;">
    <div>
      <el-row>
        <el-col :span="6">
          <el-avatar :size="75" :src="friendlyLink.avatar"></el-avatar>
        </el-col>
        <el-col :span="18" style="text-align: left">
          <h1>{{friendlyLink.title}}</h1>
          <p style="color: #909399;">{{friendlyLink.description}}</p>
          <p class="jumpLink"><span class="jumpLinkBtn" @click="jumpToOutside(friendlyLink.url)"><i class="el-icon-link"></i> go!</span></p>
        </el-col>
      </el-row>
    </div>
  </el-card>
</div>
</template>

<script>
export default {
  name: "friendlyLinkPage",
  methods:{
    jumpToOutside(link){
      window.open(link);
    }
  },
  data(){
    return {
      friendlyLinks:[]
    }
  },
  created() {
    this.$axios.get("/data/friendlyLink.json")
        .then(res => {
          this.friendlyLinks = res.data;
        });
  }
}
</script>

<style scoped>
.jumpLink{
  text-align: right;
  color: #606266;
}

.jumpLinkBtn:hover{
  color: #409EFF;
}
</style>