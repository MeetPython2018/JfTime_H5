/* eslint-disable*/
<template>
  <div id="JfAudio">
    <div class="container-full">
      <el-container>
        <div id="center">
          <el-main>
            <ul class="jf_audio">
              <div class="divider col-md-12 col-xs-8">
                <h4>
                  <span>{{info.title}}</span>
                  <i class="el-icon-microphone"></i>
                </h4>
                <h5>{{info.title_son}}</h5>
              </div>
              <div class="item">
                <div class="jiemu row">
                  <div style="width: 300px" class="col-xs-6 col-lg-2" v-for="todo in firstPageData" :key="todo.title">
                    <el-image :src="todo.cover_src" @click="viweImg">
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
                    layout="prev, pager, next" :page-size="5" :total="info.dataLength"
                    @current-change="handleCurrentChange">
                  </el-pagination>
                </div>
                <!--隐藏的评论页-->
                <el-dialog title="过往留言" :visible.sync="dialogVisible">
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
    <router-view/>
  </div>
</template>
<style scoped>
  * {
    padding: 0;
    margin: 0;
    font-family: Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  }
  #JfAudio{
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
  .jf_audio{
    width: 100%;
    height: auto;
    list-style: none;
  }
  .jf_audio .el-divider i{
    margin-left: .5rem;
  }
  .jf_audio .item{
    width: 100%;
    height: auto;
  }
  .jf_audio .item h3{
    height: 3rem;
    margin: 0;
    text-align: left;
    line-height: 3rem;
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
  .jf_audio .item .jiemu div:hover{
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)
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
    .jf_audio .item .jiemu .col-sm-2{
      margin-bottom: 1rem;
      margin-right: 0!important;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0!important;
    }
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
</style>
<script>
  export default {
    name: "JfAudio",
    props:{
      'firstPageData':{
        type: Array,
        default:function(){
          return [];
        }
      },
      'info': {
        type: Object,
        default:function () {
          return {}
        }
      }
    },
    data(){
      return {
        btnStyle:'el-icon-video-play',
        visible: false,
        id:'',
        index:0,
        currentPage:1,
        dialogVisible: false,
        count: 0,
        loading: false
      };
    },
    methods:{
      //  上下翻页
      handleCurrentChange(val){
        var skip = {
          "object": this.$route.params.author,
          "offset": (val-1)*5
        }
        this.$emit('upupEvent',skip)
      },
      // 音频控件
      playAudio(audio_src,audio_name,creator,index){
        let demo = this.$store.state.playAudio(audio_src,audio_name,creator,index)
        this.$emit('load_audio',demo)
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
      },
      viweImg(){
	      document.body.style = "";
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
  }
</script>

