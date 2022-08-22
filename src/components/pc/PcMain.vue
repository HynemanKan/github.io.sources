<template xmlns:el-col="http://www.w3.org/1999/html">
  <el-container>
    <el-header style="height: 60px;background-color: #ffffff;box-shadow: 0 2px 12px 0 rgba(0,0,0,0.1);">
      <el-row style="height: 100%">
        <el-col :span="1">
          <div><p>&nbsp;</p></div>
        </el-col>
        <el-col :span="4" style="height: 100% ">
          <div class="navbarOption" @click="jumpTo('/pcHome')">
            <el-image fit="contain"
                      src="/android-chrome-512x512.png"
                      style="height: 80%;margin: 0.75vh;float: left;"></el-image>
            <h1 style="float: left;padding: 2vh 0 2vh 0 ">Hyneman's Blog</h1>
          </div>
        </el-col>
        <el-col :span="1" style="height: 100% ">
          <div class="navbarOption" @click="jumpTo('/pcHome')">
            <p style="padding: 2vh 0 2vh 0;font-size: 15px;">主页</p>
          </div>
        </el-col>
        <el-col :span="1" style="height: 100% ">
          <div class="navbarOption" @click="jumpTo('/history')">
            <p style="padding: 2vh 0 2vh 0;font-size: 15px;">归档</p>
          </div>
        </el-col>
        <el-col :span="1" style="height: 100% ">
          <div class="navbarOption" @click="jumpTo('/friendLink')">
            <p style="padding: 2vh 0 2vh 0;font-size: 15px;">友链</p>
          </div>
        </el-col>
        <el-col :span="1" style="height: 100% ">
          <div class="navbarOption" @click="jumpTo('/fish')">
            <p style="padding: 2vh 0 2vh 0;font-size: 15px;">摸🐟</p>
          </div>
        </el-col>
      </el-row>
    </el-header>
    <el-main style="height: calc(95vh - 60px);padding: 10px;">
      <el-row style="height: 100%;">
        <el-col :span="6">
          <pc-avatar-card :statistics.sync="statistics"></pc-avatar-card>
          <pc-group-card :group-data.sync="groupData"></pc-group-card>
          <pc-category-card :categories.sync="categories"></pc-category-card>
        </el-col>
        <el-col :span="12" class="mainWindow" style="height: calc(100% - 20px);margin: 10px 0 10px 0;">
          <router-view ></router-view>
        </el-col>
        <el-col :span="6">
          <pc-latest-card :latest-article.sync="latestArticle"></pc-latest-card>
          <pc-history-card :history-data.sync="historyData"></pc-history-card>
        </el-col>
      </el-row>
      <el-backtop :bottom="100" target=".mainWindow">
        <div
            style="{
        height: 100%;
        width: 100%;
        background-color: #f2f5f6;
        box-shadow: 0 0 6px rgba(0,0,0, .12);
        text-align: center;
        line-height: 40px;
        color: #505050;
      }"
        >
          UP
        </div>
      </el-backtop>
    </el-main>
    <el-footer style="height: 5vh;background-color: #ffffff;box-shadow: 0 2px 12px 0 rgba(0,0,0,0.1);">
      <el-row justify="space-between" style="height: 100%" type="flex">
        <el-col :span="4" style="font-size: x-small;margin: 10px 0 10px 0">
          Copyright © 2018 - 2022 Hyneman's Blog
        </el-col>
        <el-col :span="4" style="font-size: x-small;margin: 10px 0 10px 0">
          Powered by vue ◆ Designed by Hyneman
        </el-col>
      </el-row>
    </el-footer>
  </el-container>
</template>

<script>
import PcAvatarCard from "@/components/pc/PcAvatarCard";
import PcCategoryCard from "@/components/pc/PcCategoryCard";
import PcHistoryCard from "@/components/pc/PcHistoryCard";
import PcLatestCard from "@/components/pc/PcLatestCard";
import PcGroupCard from "@/components/pc/PcGroupCard";

export default {
  name: "PcMain",
  components: {PcGroupCard, PcLatestCard, PcHistoryCard, PcCategoryCard, PcAvatarCard},
  data() {
    return {
      categories: [],
      statistics: [],
      historyData: [],
      latestArticle:[],
      groupData:[]
    }
  },
  methods: {
    jumpTo(href) {
      console.log(href)
      this.$router.replace(href);
    }
  },
  created() {
    this.$axios.get("/data/index/categories.json")
        .then(res => {
          this.categories = res.data;
        });
    this.$axios.get("/data/index/statistics.json")
        .then(res => {
          this.statistics = res.data;
        });
    this.$axios.get('/data/index/latestArticle.json')
        .then(res=>{
          this.latestArticle=res.data;
        });
    this.$axios.get('/data/index/historyData.json')
        .then(res=>{
          this.historyData=res.data;
        });
    this.$axios.get("/data/index/groups.json")
        .then(res=>{
          this.groupData=res.data;
        })
  },
  mounted() {
    console.log(this.$route.path);
  }
}
</script>

<style scoped>
.navbarOption {
  height: 100%;
  width: 100%;
}

.navbarOption:hover {
  background-color: #f4f4f4;
}

.mainWindow{
  overflow-y:scroll;height: 82.5vh;
}
.mainWindow::-webkit-scrollbar {
  display: none;
}
</style>