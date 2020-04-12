/* eslint-disable*/
<template>
    <div id="HotAudio">
        <div class="container-full">
            <el-container>
                <div id="center">
                    <el-main>
                        <ul class="jf_audio">
                            <div class="divider col-md-12 col-xs-8">
                                <h4>
                                    <span>近期热门</span>
                                    <i class="iconfont icon-hot_icon"></i>
                                </h4>
                                <h5>YouTube上面质量最高的时政评论节目之一。</h5>
                            </div>
                            <div class="item">
                                <div class="jiemu row">
                                    <div style="width: 300px" class="col-xs-6 col-lg-2" v-for="todo in first_page_hotAudios" :key="todo.title">
                                        <el-image :src="todo.cover_src">
                                                  <div slot="placeholder" class="image-slot">
                                                    加载中<span class="dot">...</span>
                                                  </div>
                                                </el-image>
                                        <h4 class="title">
                                            {{todo.title}}
                                        </h4>
                                        <li class="audioInfos">
                                            <span>{{todo.upload_date}}</span>
                                            <span>{{todo.audio_time}}</span>
                                        </li>
                                        <li class="tools">
                                            <i class="iconfont icon-liuyan" @click="message(todo.audio_name)"></i>

                                            <i class="iconfont icon-Dialogue" @click="seeMessages(todo.audio_name)"></i>

                                            <i class="iconfont icon-xihuan" @click="like"></i>
                                            <i :class="index===todo.id ? 'el-icon-video-pause':btnStyle" @click="playAudio(todo.audio_src,todo.audio_name,todo.creator,todo.id)"></i>
                                        </li>
                                    </div>
                                </div>
                                <!--分页-->
                                <div class="block">
                                    <el-pagination
                                            layout="prev, pager, next"
                                            :page-size="5"
                                            :total="dataLength"
                                            @current-change="handleCurrentChange"
                                          >
                                          </el-pagination>
                                </div>
                                <!--隐藏的评论页-->
                                <el-dialog
                                  title="过往留言"
                                  :visible.sync="dialogVisible">
                                    <div class="infinite-list-wrapper" style="overflow:auto;height: 18rem">
                                        <ul class="list" v-infinite-scroll="load" infinite-scroll-disabled="disabled">
                                          <li v-for="i in count" class="list-item">
                                              <div>
                                                  <span><i class="iconfont icon-user-outline"></i> {{i.users}} <i class="iconfont icon-zhifeiji"></i> {{i.audio}}</span>
                                                  <span> <i class="iconfont icon-riqi"></i> {{new Date(parseInt(i.comment_time)).toLocaleString().replace(/:\d{1,2}$/,' ')}}</span>
                                              </div>
                                              <p>
                                                  <i class="iconfont icon-huihua"></i> {{i.content}}
                                              </p>
                                          </li>
                                        </ul>
                                        <p v-if="loading">加载中...</p>
                                        <p v-if="noMore">没有更多了</p>
                                      </div>
                                </el-dialog>
                            </div>
                        </ul>
                    </el-main>
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
    #HotAudio {
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
    /*音频卡片样式*/
    #center{
        width: 100%;
        background: #f5f5f5!important;
        display: flex;
        justify-content: center;
        align-items: center;
        height: auto;
    }
    .el-main{
        width: 100%!important;
        max-width: 1260px!important;
        margin: 0 auto;
        padding: 0 1.5rem;
    }
    /*播放面板*/
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
    .jf_audio{
        width: 100%;
        height: auto;
        list-style: none;
        margin: 1rem 0;
    }
    .jf_audio .el-divider i{
        margin-left: .5rem;
    }
    .jf_audio .item{
        width: 100%;
        height: auto;
        position: relative;
    }
    .jf_audio .item .jiemu{
        height: auto;
        margin: 0;
        display: flex;
        justify-content: flex-start;
        align-items: center;
    }
    .jf_audio .item .jiemu .col-lg-2{
        margin-bottom: 1rem;
        margin-right: 1rem;
        display: flex;
        flex-basis: 10rem;
        justify-content: space-between;
        align-items: center;
        padding: 0!important;
    }
    .jf_audio .item .jiemu div{
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        position: relative;
        transition: all .5s;
        background: #fff;
    }
    .jf_audio  .item .jiemu div .el-image{
        width: 10rem;
        height: 6rem;
        padding: .5rem!important;
    }
    .title{
        width: 100%;
        height: 3rem;
        text-align: justify;
        font-size: .64rem;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 3;
        line-height: 1rem;
        overflow: hidden;
        padding: 0 .5rem!important;
    }
    .audioInfos{
        width: 100%;
        height: 1.5rem;
        display: flex!important;
        justify-content: space-between!important;
        flex-direction: row!important;
        align-items: center!important;
        padding: .25rem .5rem;
    }
    .audioInfos span{
        font-size: .64rem;
        margin: 0;
        font-family: 楷体;
    }
    .tools{
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 .5rem;
        margin-bottom: .25rem;
    }
    .tools i{
        font-size: 1.1rem;
    }
    .icon-liuyan{
        color: #24ACF2;
    }
    .icon-Dialogue{
        color: #32DD90;
    }
    .icon-xihuan{
        color: #DD4F43;
    }
    @media screen and (max-width: 600px) { /*当屏幕尺寸小于600px时，应用下面的CSS样式*/
      .col-xs-6{
          width: 45%!important;
      }
        .jf_audio .item .jiemu .col-lg-2{
        margin-bottom: 1rem;
        margin-right: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0!important;
        }
    }
    .el-menu--horizontal>.el-submenu .el-submenu__title{
        height: 3rem!important;
    }
    .col-xs-6 .el-image{
        width: 100%!important;
        height: 100%;
    }
    .col-xs-6 .title{
        height: 3.8rem;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 3;
        line-height: 1.3rem;
        overflow: hidden;
    }
    /*分页样式*/
    .el-pagination{
        width: 100%;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }
    .el-pager{
        background: #fff;
    }
    .el-pagination li{
        margin: 0!important;
    }
    /*分割线*/
    .divider{
        height: auto;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: flex-start;
        font-size: 1.1rem;
        color: #a06619;
        padding: .64rem 0;
    }
    .divider h4{
        font-size: 1.1rem;
        margin-bottom: .32rem;
    }
    .divider h4 em{
        font-style: normal;
        margin-right: .5rem;
    }
    .divider h5{
        font-size: .64rem;
        margin-right: .5rem;
    }
    .el-image{
        padding: 0!important;
        box-shadow: none!important;
    }
    .el-icon-video-play,.el-icon-video-pause{
        font-size: 1.6em;
        color: #a06619;
    }
    /*查看留言*/
    .el-dialog{
        width: 64%!important;
        height: 16rem!important;
        overflow: hidden!important;
    }
    .list-item{
        width: 89%;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
        height: 3rem;
        margin: .5rem auto;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }
    .list-item div{
        width: 89%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: .2rem 0;
        font-size: .72rem;
    }
    .list-item p{
        width: 89%;
        margin-bottom: .2rem;
        font-size: .72rem;
        text-align: left;
    }
</style>
<script>
    import APlayer from 'aplayer'
    import store from "../store";
    export default {
        name: "HotAudio",
        data() {
            return {
                btnStyle:'el-icon-video-play',
                active: '',
                id:'',
                index:0,
                play:0,
                audio_menu:'',
                flag: false,
                demo: '',
                // 节目总数
                hotAudios:[],
                first_page_hotAudios:[],
                dataLength:11,
                fits:'fill',
                data_len:'',
                dialogVisible: false,
                count: 0,
                loading: false
            };
        },
        methods:{
            //  上下翻页
            handleCurrentChange(val){
                var offset = (val-1)*5
                console.log(offset)
                this.first_page_hotAudios = this.hotAudios.slice(offset,offset+5)
            },
            // 音频控件
            playAudio(audio_src,audio_name,creator,index){
            this.index = index
            // this.demo.destroy()
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
            message(el){
              fetch("/ajax/get_sessions").then(function (e) {
                return e.json()
                  }).then((e)=>{
                      console.log(e)
                      if(e.sessions==='ok'){
                          var author= el
                          this.$prompt('To the:'+author,'评论' ,{
                              confirmButtonText: '确定',
                              cancelButtonText: '取消',
                              inputType:'textarea',
                              showClose:true,
                              inputPattern: /^.{1,100}$/,
                              inputErrorMessage: '评论不能为空，或超出一百字'
                            }).then(({ value }) => {
                                var time_stamp = (new Date()).valueOf()
                                var user = store.state.username
                                this.$axios({
                                    method:'post',
                                    url:'/ajax/comment',
                                    headers:{
                                        'Content-Type': 'application/x-www-form-urlencoded',
                                    },
                                    data:this.qs.stringify({
                                        user:user,
                                        comment:value,
                                        time_stamp:time_stamp,
                                        audio_id:author
                                    })
                                }).then((res)=>{
                                    if(res.data.status==='success'){
                                        this.$message({
                                            type: 'success',
                                            message: '评论成功！'
                                        });
                                    }else {
                                        this.$message({
                                            type: 'waring',
                                            message: '评论失败！'
                                        });
                                    }
                                })
                            }).catch(() => {
                              this.$message({
                                type: 'info',
                                message: '取消评论！'
                              });
                          });
                      }
                      else{
                          this.$message({
                            type: 'waring',
                            message: '请先登录！'
                          });
                      }
                  })
          },
            seeMessages(val){
              this.$axios.get('/ajax/seeMessages',{params:{
                    audio_id:val
              }
                }).then((res)=>{
                  console.log(res)
                  if(res.data.length===0){
                      this.count=0
                      this.loading = false
                  }else{
                      this.count = res.data
                      this.loading = false
                  }
                  this.dialogVisible = true
              })

            },
            like(){
                this.$message({
                  message: '收藏节目成功！',
                  type: 'success'
              });
            },
            load () {
                this.loading = false
                setTimeout(() => {
                    // this.count += 2
                    this.loading = false
                }, 2000)
            }
        },
        computed: {
            noMore () {
                return this.count >= 50
            },
            disabled () {
                return this.loading || this.noMore
            }
        },
        async mounted() {
          // 获取音频
          fetch("/ajax/jftime/hotAudios").then(function (e) {
                return e.json()
          }).then((e)=>{
              this.first_page_hotAudios = e.slice(0,5)
              this.hotAudios = e
              this.dataLength = 11
          })
      }
    }
</script>

