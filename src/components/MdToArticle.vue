<template>
  <div class="markdown-body">
    <VueMarkdown :source="article" v-highlight></VueMarkdown>
  </div>
</template>

<script>
import VueMarkdown from 'vue-markdown';
export default {
  name: "MdToArticle",
  components:{
    VueMarkdown
  },
  props:["article"]
}
</script>

<style scoped>

</style>