<template>
  <div>
    <nut-navbar
        :rightShow="false"
        @on-click-back="showPop=true"
    >123
      <a slot="back-icon"><nut-icon type="more"></nut-icon></a>
    </nut-navbar>
    <nut-popup
        position="left"
        v-model="showPop"
        style="width: 80%;height: 100%"
    ></nut-popup>
  </div>
</template>

<script>
export default {
  name: "MobileMain",
  data(){
    return{
      showPop:false
    }
  }
}
</script>

<style scoped>

</style>