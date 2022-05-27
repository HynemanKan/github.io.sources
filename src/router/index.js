import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: "/pcHome",
    name: "pcHome",
    component:()=>import("../views/pc/PcHomePage.vue"),
    meta: {
      title: 'hyneman\'s blog'
    }
  },
  {
    path: '/friendLink',
    name: "friendLink",
    component:()=>import("../views/pc/pcFriendlyLinkPage.vue"),
    meta: {
      title: '友情链接'
    }
  },
  {
    path: '/article/:articleName',
    name: "articlePage",
    component:()=>import("../views/pc/pcArticlePage.vue")
  },{
    path: "/list/:type/:target",
    name: "listPage",
    component:()=>import("../views/pc/pcListArticlePage.vue")
  }
]

const router = new VueRouter({
  base: "./",
  routes
})

router.beforeEach((to, from, next) => {
  /* 路由发生变化修改页面title */
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})

export default router
