const routes=[
    {path:'/home',component:home},
    {path:'/projectview',component:projectview}
]

// const router = new VueRouter({
//     routes
// })

// const app = new Vue({
//     router
// }).$mount('#app')


const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes
  })
  const app = Vue.createApp({})
  app.use(router)
  app.mount('#app')