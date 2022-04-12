<template>
  <div id="app">
    <entry></entry>
  </div>
</template>

<style>
body, div, dl, dt, dd, ul, ol, li, h1, h2, h3, h4, h5, h6, pre, code, form, fieldset,
legend, input, textarea, p, blockquote, th, td, hr, button, article, aside,
details, figcaption, figure, footer, header, hgroup, menu, nav, section {

  margin: 0;

  padding: 0;

}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
<script>
import Entry from "@/components/entry";

export default {
  components: {Entry}
}
</script>