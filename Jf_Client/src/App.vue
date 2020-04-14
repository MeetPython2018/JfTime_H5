<template>
  <div id="app">
    <div class="container-full">
      <el-container>
        <div class="navs rows">
          <el-header class="col-sm-12 col-xs-8">
            <nav class="navbar">
              <el-image :src="logo_index">
                <div slot="placeholder" class="image-slot">
                  加载中<span class="dot">...</span>
                </div>
              </el-image>
              <ul class="nav-items">
                <li class="nav-item" @click="routerTo('/Home')">
                  <div class="phone">
                    <i class="iconfont icon-zhuye1"></i>
                    <span>主页</span>
                  </div>
                  <span class="pc">主页</span>
                </li>
                <li class="nav-item" @click="routerTo('/About')">
                  <div class="phone">
                    <i class="iconfont icon-about"></i>
                    <span>关于</span>
                  </div>
                  <span class="pc">关于</span>
                </li>
                <li class="nav-item" @click="routerTo('/Sign_')" v-if="!login">
                  <div class="phone">
                    <i class="iconfont icon-user-outline"></i>
                    <span>登录</span>
                  </div>
                  <span class="pc">登录</span>
                </li>
                <li class="nav-item" v-else>
                  <div class="phone">
                    <img @click="enterMyCenter" src="http://120.77.223.229:100/net_index/users.png"/>
                    <span>退出</span>
                  </div>
                  <div id="user-img" class="pc">
                    <img  @click="enterMyCenter" src="http://120.77.223.229:100/net_index/users.png"/>
                    <i class="iconfont icon-dianyuan" @click="SignOut"></i>
                  </div>
                </li>
              </ul>
            </nav>
            <div class="audio_menu">
              <div class="audio_img">
            <div id="player" class="aplayer"></div>
          </div>
            </div>
          </el-header>
        </div>
      </el-container>
    </div>
    <transition name="fade">
      <router-view @load_audio_top="load_audio_top"></router-view>
    </transition>
  </div>
</template>
<style scoped>
  * {
    padding: 0;
    margin: 0;
      font-family: Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  }
  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    padding: 0;
    margin: 0;
  }
  /*导航栏*/
  .navs{
    width: 100%;
    background: #1DA1F2!important;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 3.5rem;
  }
  .el-header{
    width: 100%!important;
    max-width: 1260px!important;
    line-height: 3.5rem;
    height: 3.5rem!important;
    color: #fff;
    padding: 0 1.5rem 0 1.1rem;
  }
  .navbar{
    height: 3.5rem;
    background: #1DA1F2!important;
    padding: 0;
  }
  .navbar-collapse{
    display: flex;
    justify-content: flex-end;
    align-items: center;
    z-index: 1000;
    flex-direction: row!important;
  }
  .navbar-nav{
    height: 3.5rem!important;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .nav-items{
    width: 30%;
    height: 3.5rem;
    font-size: .89rem;
    background: #1DA1F2!important;
    right: 0;
    color: #fff!important;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .nav-item{
    list-style: none;
  }
  .nav-item:hover{
    cursor: pointer;
  }
  .nav-items a{
    text-decoration: none;
    color: #fff!important;
    list-style: none;
  }
  #user-img{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  #user-img img{
    width: 2rem;
    height: 2rem;
    margin-right: .5rem;
  }
  #user-img i{
    font-size: 1.2rem;
  }
  .el-image{
    background: #1DA1F2;
    width: 6.4rem;
    height: 2.4rem;
  }
  /* 可以设置不同的进入和离开动画 */
  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }
  .phone{
    display: none;
  }
  @media screen and (max-width: 600px) { /*当屏幕尺寸小于600px时，应用下面的CSS样式*/
    .el-image{
      display: none;
    }
    .el-container,.el-header{
      height: 5rem!important;
    }
    .navs{
      height: 100%;
    }
    .nav-items{
      width: 100%;
    }
    .nav-items{
      height: 5rem;
    }
    .phone{
      display: flex;
      flex-direction: column;
    }
    .phone img{
      width: 2rem;
      height: 2rem;
      margin-top: .64rem;
    }
    .phone i{
      display: block;
      height: 2.5rem;
    }
    .phone span{
      height: 2.5rem;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 1rem;
    }
    .pc{
      display: none;
    }
    #user-img{
      display: none;
    }
    .nav-item{
      height: 3.5rem;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    .icon-zhuye1,.icon-about{
      font-size: 2rem;
    }
    .icon-dianyuan,.icon-user-outline{
      font-size: 2.2rem;
    }
  }
  /*播放按钮*/
  .audio_menu{
    position: fixed;
    height: 3.5rem;
    left: 0;
    right: 0;
    top: 0;
    margin: 0 auto;
    width: 15rem;
    border: 0!important;
    z-index: 1200;
    color: #333;
  }
</style>
<script>
  import store from "./store";
  import APlayer from 'aplayer'
  export default {
    data() {
      return {
        login:'',
        logo_index:'http://120.77.223.229:100/JfTime/net_img/JF_logo.png',
        routers:[
          {
            id:0,
            name:'Home',
            router:'/Home'
          },
          {
            id:1,
            name:'About',
            router:'/About'
          },
          {
            id:2,
            name:'Sign',
            router:'/Sign_'
          }
        ],
        index:0,
        font_chose:'color:#ccc;',
        font_chosed:'color:#fff;'
      };
    },
    methods:{
      routerTo(val){
        this.$router.push(val)
      },
      errorHandler() {
        return false
      },
      // 进入我的中心
      enterMyCenter(){
        this.$router.push({name:'PersonalCenter'})
      },
      // 退出登录
      SignOut(){
        this.$axios({
          methods: 'get',
          url:'/ajax/sign_out',
        }).then((response)=>{
          if(response.data.sign_out==='ok'){
            this.login = false
            store.commit('login_out')
            let demo = JSON.stringify({'logined':false,'username':''})
            sessionStorage.setItem('state',demo)
          }
        })
      },
      // 获取音频
      load_audio_top:function (val) {
        const ap = new APlayer({
          container: document.getElementById('player'),
          fixed: false,
          autoplay: true,
          listFolded: true,
          listMaxHeight: 90,
          audio: [
            {
              name: val.audio_name,
              artist: val.creator,
              url: val.audio_src,
              cover: '',
            }
          ]
        })
        ap.on('pause', ()=>{
          this.index = ''
        });
        ap.on('play', ()=>{
          this.index = val.index
        });
        this.demo = ap
      }
    },
    created(){
      fetch("/ajax/get_sessions").then(function (e) {
        return e.json()
      }).then((e)=>{
        if(e.sessions==='ok'){
          this.login = true
        }else{
          this.login = false
        }
      })
      var url = this.$route.name
      if(url===null){
        this.$router.push('/Home/HotAudio')
        this.index = 0
      }else if(url==='About'){
        this.$router.push('/About')
        this.index = 1
      }else if(url==='Sign_'){
        this.$router.push('/Sign_')
        this.index = 2
      }
    },
    updated(){
          // if(sessionStorage.getItem('state')){
          //     let demo = JSON.parse(sessionStorage.getItem('state'))
          //     this.login = demo.logined
          // }
      fetch("/ajax/get_sessions").then(function (e) {
        return e.json()
      }).then((e)=>{
        if(e.sessions==='ok'){
          this.login = e.sessions
        }
      })
    },
    watch: {
      '$route' (to, from) {
        if(to.path==='/Home'){
          this.$router.push('/Home/HotAudio')
          this.index = 0
        }else if(to.path==='/About'){
          this.$router.push('/About')
          this.index = 1
        }else if(to.path==='/Sign_'){
          this.$router.push('/Sign_')
          this.index = 2
        }
      },
    },
  }
</script>
