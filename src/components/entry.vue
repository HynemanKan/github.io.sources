<template>
  <div>
    <pc-main v-if="!isPhone"></pc-main>
    <mobile-main v-else></mobile-main>
  </div>
</template>

<script>
import PcMain from "@/components/pc/PcMain";
import MobileMain from "@/components/mobile/MobileMain";
export default {
  name: "entry",
  components: {MobileMain, PcMain},
  data(){
    return{
      isPhone:/Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent),
    }
  }
}
</script>

<style scoped>

</style>