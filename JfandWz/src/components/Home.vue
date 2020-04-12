/* eslint-disable*/
<template>
    <div id="Home">
        <div class="container-full">
            <el-container>
                <div class="audio_menu">
                        <div class="audio_img">
                            <div id="player" class="aplayer"></div>
                        </div>
                    </div>
                <div class="nav-small">
                    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :router="true" @select="handleSelect">
                        <el-menu-item index="/Home/HotAudio">近期热门</el-menu-item>
                        <el-submenu index="2">
                            <template slot="title">江峰时刻</template>
                            <el-menu-item index="/Home/JfAudio/jfmt">江峰漫谈</el-menu-item>
                            <el-menu-item index="/Home/JfAudio/today_history">历史上的今天</el-menu-item>
                            <el-menu-item index="/Home/JfAudio/trump_twitter">川普推推推</el-menu-item>
                        </el-submenu>
                        <el-menu-item index="/Home/wenzhao">文昭谈古论今</el-menu-item>
                        <el-menu-item index="/Home/search">搜一搜</el-menu-item>
                    </el-menu>
                </div>
                <router-view :first-page-date="first_page_date" :infos="infos" :dataLength="dataLength" @upupEvent="upupEvent" :key="key"></router-view>
                <div id="bottom">
                        <el-footer class="col-sm-12 col-xs-8">
                            <div class="links">
                                <a href="https://www.youtube.com"  target="_blank" style="color: #D31C1F"><i class="iconfont icon-youtobe"></i></a>
                                <a href="https://www.twitter.com" target="_blank" style="color: #1CA0F1"><i class="iconfont icon-twitter"></i></a>
                                <a href="https://www.facebook.com" target="_blank" style="color: #3B5998"><i class="iconfont icon-icon-facebook"></i></a>

                        </div>
                            <div class="words">
                            <em>越是習慣,別人越是得寸進尺。</em>
                            <em>越是懼怕,别人越是肆無忌憚。</em>
                        </div>
                        </el-footer>
                    </div>
            </el-container>
        </div>
    </div>
</template>
<style scoped>
    * {
        padding: 0;
        margin: 0;
        font-family: Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    }
    #Home {
        width: 100%;
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        padding: 0;
        margin: 0;
        background: #f7f7f7;
    }
    .el-container{
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
    }
    /*二级导航*/
    .nav-small{
        width: 100%;
        max-width: 1260px;
        margin: 1.5rem auto 0;
        padding: 0 1.5rem;
        height: 3.05rem;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        background: #f7f7f7;
    }
    .nav-small ul{
        height: 3.05rem;
        line-height: 3.05rem;
        background: #f7f7f7;
    }
    .el-menu-demo{
        width: 100%;
        display: flex;
        justify-content: flex-start;
        align-items: center;
    }
    .el-menu-demo li{
        margin-right: 1rem;
    }
    .el-menu-demo li:nth-child(3){
        margin-right: 2rem;
    }
    .el-breadcrumb__item{
        font-size: .89rem;
    }
    .el-menu-item{
        height: 3.05rem!important;
        line-height: 3.05rem!important;
    }
    .el-menu--horizontal>.el-submenu .el-submenu__title{
        height: 3.05rem!important;
        line-height: 3.05rem!important;
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
    }
    /*底部样式*/
    #bottom{
        width: 100%;
        background: #fff!important;
    }
    .el-footer{
        width: 100%!important;
        max-width: 1260px!important;
        margin: 0 auto;
        padding: 0 1.5rem;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        height: 3.5rem!important;
    }
    .links{
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .el-footer .links a{
        display: flex;
        justify-content: center;
        align-items: center;
        text-decoration: none;
        margin-right: 1rem;
    }
    .el-footer .links a:last-child{
        margin-right: 0;
    }
    .el-footer .links i{
        font-size: 1.5rem;
    }
    .el-footer .words{
        margin-left: 1rem;
    }
    .el-footer .words em{
        font-size: .72rem;
        letter-spacing: .05rem;
    }
    .el-footer .words em:first-child{
        margin-right: .5rem;
        /*margin-left: 6.4rem;*/
    }
    .el-carousel__item h3 {
        color: #475669;
        font-size: 18px;
        opacity: 0.75;
        line-height: 300px;
        margin: 0;
    }
</style>
<script>
    import APlayer from 'aplayer'
    export default {
        name: "Home",
        data() {
          return {
            btnStyle:'el-icon-video-play',
            visible: false,
            active: '',
            id:'',
            index:0,
            play:0,
            audio_menu:'',
            flag: false,
            demo: '',
              fits:'fill',
              first_page_data:'',
              activeIndex: '/Home/HotAudio',

              data_len:0,
                demo_data_len:'',
                all_data:'',
              first_page_date: [],
              infos:{},
              stream:[],
              dataLength:0,
              data:'',
                title:'',
                title_son:''

        };
      },
        methods:{
          // 音频控件
          playAudio(audio_src,audio_name,creator,index){
            this.index = index
            this.demo.destroy()
            const ap = new APlayer({
                container: document.getElementById('player'),
                fixed: false,
                autoplay: true,
                listFolded: true,
                listMaxHeight: 90,
                audio: [
                    {name: audio_name,
                    artist: creator,
                    url: audio_src,
                    cover: '',
                    }
                ]
                })
            ap.on('pause', ()=>{
                this.index = ''

            });
            ap.on('play', ()=>{
                this.index = index
            });
            console.log(this.index)
            this.demo = ap
        },
          handleSelect(key, keyPath){
              if(key.substr(-4,4) === 'jfmt'){
                  this.dataLength = this.demo_data_len['data1_len']
                  this.items = 'jfmt'
                  this.first_page_date = this.all_data[0]
                  this.infos = {"title":'江峰漫谈',"title_son":'蹭熱點，不蹭熱鬧；看新聞，更看門道。',"dataLength":this.demo_data_len['data1_len']}
                }
                if(key.substr(-13,13) === 'today_history'){
                    this.dataLength = this.demo_data_len['data2_len']
                    this.items = 'today_history'
                    this.first_page_date = this.all_data[1]
                    this.infos = {"title":'历史上的今天',"title_son":'講出歷史真相，道出生命冷暖。',"dataLength":this.demo_data_len['data2_len']}
                }
                if(key.substr(-13,13) === 'trump_twitter'){
                    this.dataLength = this.demo_data_len['data3_len']
                    this.items = 'trump_twitter'
                    this.first_page_date = this.all_data[2]
                    this.infos = {"title":'川普推推推',"title_son":'通過推特總統，了解美國，了解正常人類秩序，一起為未來的中國尋找智慧和久違的神性。',"dataLength":this.demo_data_len['data3_len']}
                }
          },
          upupEvent:function (val) {
              console.log(val)
              fetch("/ajax/jftime/handleCurrentChange?objects="+val.object+"&offset="+val.offset).then(function (e) {
                return e.json()
            }).then((e)=>{
                this.first_page_date = e
            })
          }
      },
        async mounted() {
            fetch("/ajax/jftime/PullAudios").then(function (e) {
                return e.json()
            }).then((e)=>{
                this.all_data = e
            }),
                //  获取节目数
            fetch("/ajax/jftime/dataLength").then(function (e) {
              return e.json()
          }).then((e)=>{
                this.demo_data_len = e
            })

        },
        computed:{
            key() {
                return this.$route.name !== undefined? this.$route.name + new Date(): this.$route + new Date()
            }
        }
  }
</script>

