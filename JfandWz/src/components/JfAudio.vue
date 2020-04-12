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
                                    <span>{{infos.title}}</span>
                                    <i class="el-icon-microphone"></i>
                                </h4>
                                <h5>{{infos.title_son}}</h5>
                            </div>
                            <div class="item">
                                <div class="jiemu row">
                                    <div style="width: 300px" class="col-xs-6 col-lg-2" v-for="todo in firstPageDate" :key="todo.id">
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
                                            <i class="iconfont icon-Dialogue"></i>
                                            <i class="iconfont icon-xihuan"></i>
                                            <i :class="index===todo.id ? 'el-icon-video-pause':btnStyle" @click="playAudio(todo.audio_src,todo.audio_name,todo.creator,todo.id)"></i>
                                        </li>

                                    </div>
                                </div>
                                <!--分页-->
                                <div class="block">
                                    <el-pagination
                                            :current-page="1"
                                            layout="prev, pager, next"
                                            :page-size="5"
                                            :total="infos.dataLength"
                                            @current-change="handleCurrentChange"
                                    >
                                    </el-pagination>
                                </div>
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
        font-size: 1rem;
        font-weight: bold;
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
    /*节目卡片浮起特效*/
    .active{
        box-shadow: 0 6px 12px 0 rgba(0, 0, 0, 0.1)!important
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
    import APlayer from 'aplayer'
    export default {
        name: "JfAudio",
        props:{
            'firstPageDate':{
                type: Array,
                default:function(){
                    return [];
                }
            },
            'infos': {
                type: Object,
                default:function () {
                    return {}
                }
            },
            "dataLength":{
                type: Number
            }
        },
        data(){
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
                data_len:10,
                selected_items: this.$parent.seletedItems,
                demo_data_len:'',
                all_data:'',
                data: [],
                page_data:'',
                title:'',
                title_son:'',
                offset:0,
                skip:{},
                currentPage:1
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
              var type = this.$route.params.author
              console.log(type)
              var offset = (val-1)*5
            },
            // 音频控件
            playAudio(audio_src,audio_name,creator,index){
            this.index = index
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
      }
  }
</script>

