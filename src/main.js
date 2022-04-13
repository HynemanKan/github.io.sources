import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import NutUI from '@nutui/nutui';
import '@nutui/nutui/dist/nutui.css';
import axios from 'axios';
import 'github-markdown-css/github-markdown.css'
import 'github-markdown-css/github-markdown.css'
import hljs from 'highlight.js'
// 如果开启了typescript 需要额外安装 npm install @types/highlight.js
// 通过 import * as hljs from 'highlight.js' 引入
Vue.directive('highlight', function (el) {
  const blocks = el.querySelectorAll('pre code')
  blocks.forEach(block => {
    hljs.highlightBlock(block)
  })
})
Vue.prototype.$axios = axios;
NutUI.install(Vue);
Vue.use(ElementUI);
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

//百度统计
// eslint-disable-next-line
var _hmt = _hmt || [];
// eslint-disable-next-line
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?36766813310accee5bec07ffbd0cfcaf";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();


