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
    component:()=>import("../views/pc/friendlyLinkPage.vue"),
    meta: {
      title: '友情链接'
    }
  }
]

const router = new VueRouter({
  base: process.env.BASE_URL,
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
