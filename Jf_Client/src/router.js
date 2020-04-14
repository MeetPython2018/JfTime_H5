import Vue from 'vue'
import Router from 'vue-router'
import Home from './components/Home.vue'                          // 主页路径
import hotAudio from './components/hotAudio.vue'                 // 近期热门的节目
import JfAudio from './components/JfAudio.vue'                  // 江峰旗下的节目
import wenzhao from './components/wenzhao.vue'                 // 文昭谈古论今
import search from './components/search.vue'                  // 搜索

import About from './components/About.vue'                  // 关于本站路径
import Sign_ from './components/Sign_.vue'                 // 注册&&注册路径
import PersonalCenter from './components/PersonalCenter.vue'     // 个人中心


Vue.use(Router)

const routerPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return routerPush.call(this, location).catch(error=> error)
}

export default new Router({
  routes: [
    {
      path: '/Home',
      name: 'Home',
      component: Home,
      children:[
        {
          path:'hotAudio',
          component: hotAudio
        },
        {
          path:'JfAudio/:author',
          component: JfAudio
        },
        {
          path:'wenzhao',
          component: wenzhao
        },
        {
          path:'search',
          component: search
        }
        ]
      },
      {
        path: '/About',
        name: 'About',
        component: About
      },
      {
        path: '/PersonalCenter',
        name:'PersonalCenter',
        component:PersonalCenter
      },
      {
        path: '/Sign_',
        name: 'Sign_',
        component: Sign_
      }
  ]
})
