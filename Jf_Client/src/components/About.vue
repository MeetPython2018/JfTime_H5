<template>
  <div id="About">
    <div class="container-full">
      <el-container>
        <div id="center">
          <el-main>
            <div class="row">
              <div class="jf">
                <div class="block col-md-9">
                  <el-image :src="creator_img_url[0]" @click="viweImg">
                    <div slot="placeholder" class="image-slot">
                      加载中<span class="dot">...</span>
                    </div>
                  </el-image>
                </div>
                <ul class="col-md-2">
                  <em>专栏:</em>
                  <li>
                                            <el-badge :value="jfmt_datas" :max="99" class="item" type="primary">
                                                <el-popover
                                                    placement="bottom"
                                                    title="江峰漫谈"
                                                    width="200"
                                                    trigger="click"
                                                    content="蹭熱點，不蹭熱鬧；看新聞，更看門道。">
                                                    <el-button slot="reference">江峰漫谈</el-button>
                                                </el-popover>
                                            </el-badge>
                                        </li>
                  <li>
                    <el-badge :value="historyToday_datas" :max="99" class="item" type="primary">
                      <el-popover placement="bottom" title="歷史上的今天" width="200" trigger="click" content="歷史本來不應該枯燥，因為他是有血有肉的人、和他們有血有肉的故事組成的。假如你能發現那人內心的靈性，故事背後的靈動，歷史便開始變得鮮活起來。。。">
                        <el-button slot="reference">歷史上的今天</el-button>
                      </el-popover>
                    </el-badge>
                  </li>
                  <li>
                    <el-badge :value="trump_twitter_datas" :max="99" class="item" type="primary">
                      <el-popover placement="bottom" title="川普推推推" width="200" trigger="click" content="經罵又經踹的川普天天推推推！通過推特總統了解美國，了解正常人類秩序，一起為未來的中國尋找智慧和久違的神性。">
                        <el-button slot="reference">川普推推推</el-button>
                      </el-popover>
                    </el-badge>
                  </li>
                  <h4>
                                        <el-button type="text" @click="dialogTableVisible1 = true" style="color: #a06619">关于创作者</el-button>
                            <el-dialog title="江峰" :visible.sync="dialogTableVisible1">
                                <span>穿透谎言的迷雾，启迪国人的思想。独裁者惧怕的声音，海内外最好的中文节目之一。江先生您好！﻿</span>
                            </el-dialog>
                                    </h4>
                </ul>
              </div>
              <div class="wz">
                <div class="block col-md-9">
                  <el-image :src="creator_img_url[1]" @click="viweImg">
                    <div slot="placeholder" class="image-slot">
                      加载中<span class="dot">...</span>
                    </div>
                  </el-image>
                </div>
                <ul class="col-md-2">
                  <em>专栏:</em>
                  <li>
                    <el-badge :value="wenzhao_datas" :max="99" class="item" type="primary">
                      <el-popover placement="bottom" title="文昭谈古论今" width="200" trigger="click" content="华语世界最受欢迎的评论节目之一">
                        <el-button slot="reference">文昭谈古论今</el-button>
                      </el-popover>
                    </el-badge>
                  </li>
                  <li>
                    <el-badge :value="0" :max="99" class="item" type="primary">
                      <el-popover placement="bottom" title="会员专享" width="200" trigger="click" content="更多样的视听内容，会员专属特别节目，购买本网站推出的文化产品时可享有一定的折扣。">
                        <el-button slot="reference">会员专享</el-button>
                      </el-popover>
                    </el-badge>
                  </li>
                  <h4>
                    <el-button type="text" @click="dialogTableVisible2 = true" style="color: #a06619">关于创作者</el-button>
                    <el-dialog title="文昭" :visible.sync="dialogTableVisible2">
                      <span>旅加中国问题评论人士、文化学者、影视剧编剧文昭先生。</span>
                    </el-dialog>
                  </h4>
                </ul>
              </div>
            </div>
          </el-main>
        </div>
        <div id="bottom">
                        <el-footer class="col-sm-12 col-xs-8">
                            <div class="links">
                                <a href="https://www.jfengtime.com/"  target="_blank" style="color: #BF8040"><i class="iconfont icon-weibiaoti2zhuanhuan"></i>江峰时刻</a>
                                <a href="https://www.wenzhao.ca/" target="_blank" style="color: #A06619"><i class="iconfont icon-weibiaoti2zhuanhuan"></i>文昭谈古论今</a>
                        </div>
                            <div class="words">
                            <em>沒有從天而降的英雄，只有挺身而出的凡人。</em>
                        </div>
                        </el-footer>
                    </div>
      </el-container>
    </div>
    <router-view/>
  </div>
</template>
<style scoped>
    *{
        padding: 0;
        margin: 0;
        list-style: none;
    }
    #About {
      font-family: 'Avenir', Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      padding: 0;
      margin: 0;
    }
    .container-full{
        background: #f7f7f7!important;
    }
    .el-container{
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
    }
    /*内容区*/
    #center{
        width: 100%;
        height: auto;
        margin-top: 2rem;
    }
    .el-main{
        width: 100%!important;
        max-width: 1260px!important;
        margin: 0 auto;
        padding: 0 1.5rem;
    }
    .row{
        width: 100%!important;
        display: flex!important;
        justify-content: space-between;
        align-items: center;
        margin: 0 auto;
    }
    .col-xs-8{
        margin: 0 auto;
    }
    .el-button{
        font-size: .64rem;
        text-align: center;
        padding: .5rem .89rem;
    }
    .jf,.wz{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background-size: 100% auto;
      background-repeat: no-repeat;
      margin-bottom: 1.5rem;
      position: relative;
    }
    ul{
      width: 20%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      list-style: none;
      font-size: .64rem;
    }
    ul em{
      color: #a06619;
      font-size: .89rem;
      font-style: normal;
      margin-top: 1.5rem;
    }
    ul li{
      color: #fff;
      font-size: .72rem;
      font-style: normal;
      margin-top: 1.5rem;
    }
    .el-button{
      padding: .5rem;
    }
    .el-image{
      width: 100%;
      box-shadow: 13px 13px 20px #cbced1,
        -13px -13px 20px #ffffff;
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
        height: 3.5rem;
    }
    .el-footer .links{
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .el-footer .links a{
        display: flex;
        justify-content: flex-start;
        align-items: center;
        text-decoration: none;
        margin-right: .5rem;
        font-size: .64rem;
    }
    .el-footer .links i{
        font-size: 1.6rem;
    }
    .el-footer .words{
        /*margin-left: 1rem;*/
    }
    .el-footer .words em{
        font-size: .89rem;
        letter-spacing: .05rem;
    }
  @media screen and (max-width: 600px) { /*当屏幕尺寸小于600px时，应用下面的CSS样式*/
    .jf,.wz{
      width: 100%;
    }
    .el-image{
      width: 100%;
      height: 20rem;
    }
    ul{
      width: 89%;
      position: absolute;
      left: 1rem;
      bottom: 1rem;
      display: flex;
      flex-direction: row;
      justify-content: space-around;
      align-items: center;
      height: auto;
    }
    ul li{
      margin-top: 0;
      margin-right: 1.2rem;
    }
    ul em{
      margin: 0;
    }
  }
</style>
<script>
  export default {
    name: "About",
    data() {
      return {
        dialogTableVisible1: false,
        dialogTableVisible2: false,
        visible: false,
        active:'',
        creator_img_url:['http://120.77.223.229:100/JfTime/net_img/jfTime.png','http://120.77.223.229:100/WenZhao/net_img/wz.png'],
        logo_index:'http://120.77.223.229:100/net_index/logo.png',
        fit: 'contain',
        id:'',
        // 节目数
        jfmt_datas:0,
        historyToday_datas:0,
        trump_twitter_datas:0,
        wenzhao_datas:0,
    };
    },
    methods:{
      viweImg(){
	      document.body.style = "";
      }
    },
    async mounted(){
      fetch("/ajax/dataLength").then(function (e) {
        return e.json()
      }).then((e)=>{
        this.jfmt_datas = e['data1_len']
        this.historyToday_datas = e['data2_len']
        this.trump_twitter_datas = e['data3_len']
        this.wenzhao_datas = e['data4_len']
      })
    }
  }
</script>

