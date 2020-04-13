<template>
  <div id="signIn">
    <div class="container-full">
      <div class="cons">
        <el-main>
          <div class="login-div">
            <div class="logo"></div>
            <div class="title">江峰时刻</div>
            <div class="fields">
                        <div class="username">
                            <i class="iconfont icon-youxiang-copy"></i>
                            <input type="username"  @blur="checking" v-model="email" class="user-input" placeholder="username" />

                        </div>
                        <div class="password">
                            <i class="iconfont icon-mima"></i>
                            <input type="password" v-model="password" class="pass-input" placeholder="password" />
                        </div>
                      </div>
            <button class="signin-button" @click="Login">Login</button>
            <div class="link">
              <a href="#">Forgot password ?</a> or <router-link to="/SignUp">Sign up</router-link>
            </div>
          </div>
        </el-main>
      </div>
      <div id="bottom">
        <el-footer class="col-sm-12 col-xs-8">
          <div class="links">
              <a href="https://www.youtube.com"  target="_blank"><i class="iconfont icon-youtobe"></i></a>
              <a href="https://www.twitter.com" target="_blank"><i class="iconfont icon-twitter"></i></a>
              <a href="https://www.facebook.com" target="_blank"><i class="iconfont icon-icon-facebook"></i></a>
            </div>
            <div class="words">
              <em>越是習慣,別人越是得寸進尺。</em>
              <em>越是懼怕,别人越是肆無忌憚。</em>
            </div>
        </el-footer>
      </div>
    </div>
  </div>
</template>
<style scoped>
  * {
        padding: 0;
        margin: 0;
        font-family: '苹方';
    }
  #signIn {
      width: 100%;
      height: auto;
      font-family: 'Avenir', Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
    }
  .container-full{
      background: #f7f7f7!important;
  }
  .el-container{
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-end;
  }
  .cons{
    width: 100%;
    background: #f7f7f7;
  }
  .el-main{
    width: 100%!important;
    max-width: 1260px!important;
    padding: 0 1.5rem;
    display: flex;
    justify-content: flex-end;
    align-items: flex-end;
    margin: 0 auto;
  }
  .login-div{
    width: 21rem;
    /*height: 26rem;*/
    height: auto;
    padding: 2rem 1.5rem 1.5rem 1.5rem;
    border-radius: 2rem;
    background: #ecf0f3;
    box-shadow: 13px 13px 20px #cbced1,
          -13px -13px 20px #ffffff;
    margin: 2rem 0;
  }
  @media screen and (max-width: 600px) { /*当屏幕尺寸小于600px时，应用下面的CSS样式*/
    .container-full{
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;
    }
    .el-main{
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .login-div{
      width: 28rem;
      height: auto;
      padding: 2rem 1.5rem 1.5rem 1.5rem;
      border-radius: 2rem;
      background: #ecf0f3;
      box-shadow: 13px 13px 20px #cbced1,
            -13px -13px 20px #ffffff;
      margin-top: 4rem;
      font-size: .64rem;
    }
    .login-div .signin-button{
        outline: none;
        border:none;
        cursor: pointer;
        width:100%;
        height: 4rem;
        border-radius: 2rem;
        font-size: .64rem;
        font-weight: 700;
        font-family: 'Lato', sans-serif;
        color:#fff;
        text-align: center;
        background: #24cfaa;
        box-shadow: 3px 3px 8px #b1b1b1,
                    -3px -3px 8px #ffffff;
        transition: 0.5s;
      }
    #bottom{
        height: 8rem;
      }
    .icon-youtobe,.icon-twitter,.icon-icon-facebook{
      font-size: 2rem!important;
    }
    #bottom footer{
        height: 8rem!important;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
      }
  }
  .logo {
      background:url("../assets/logo_sign.png");
      width: 5rem;
      height: 5rem;
      border-radius: 50%;
      margin: 0 auto;
      box-shadow:
      /* logo shadow */
      0 0 2px #5f5f5f,
      /* offset */
      0 0 0 5px #ecf0f3,
      /*bottom right */
      15px 8px 15px #a7aaaf,
      /* top left */
      -8px -8px 15px #ffffff
      ;
        background-size: 100% 100%;
    }
  .title {
        height: auto;
      text-align: center;
      font-size: 1.2rem;
      padding-top: .89rem;
      letter-spacing: .05rem;
        display: flex;
        align-items: center;
        justify-content: center;
    }
  .fields {
      width: 100%;
      padding: .5rem .25rem .25rem .25rem;
    }
  .fields input {
      border: none;
      outline:none;
      background: none;
      font-size: .89rem;
      color: #555;
      padding: .89rem .5rem .89rem .25rem;
    }
  .iconfont{
        color: #BEBFC4;
        padding-right: 1rem;
    }
  .username, .password {
        display: flex;
        justify-content: flex-start;
        align-items: center;
      margin-bottom: 1rem;
      border-radius: 1.1rem;
      box-shadow: inset 8px 8px 8px #cbced1,
                  inset -8px -8px 8px #ffffff;
    }
  .icon-youxiang-copy,.icon-mima{
        color: #BEBFC4;
        padding: 0 .5rem 0 1rem;
  }
  .icon-youtobe{
    color: #D31C1F;
  }
  .icon-twitter{
    color: #1CA0F1;
  }
  .icon-icon-facebook{
    color: #3B5998
  }
  .signin-button {
      outline: none;
      border:none;
      cursor: pointer;
      width:100%;
      height: 60px;
      border-radius: 30px;
      font-size: 20px;
      font-weight: 700;
      font-family: 'Lato', sans-serif;
      color:#fff;
      text-align: center;
      background: #24cfaa;
      box-shadow: 3px 3px 8px #b1b1b1,
                  -3px -3px 8px #ffffff;
      transition: 0.5s;
    }
  .signin-button:hover {
      background:#2fdbb6;
    }
  .signin-button:active {
      background:#1da88a;
    }
  .link {
      padding-top: 20px;
      text-align: center;
    }
  .link a {
      text-decoration: none;
      color:#aaa;
      font-size: 15px;
    }
  .title{
        height: 2.5rem;
        font-size: 1.1rem;
        color: #a06619;
        line-height: 2.5rem;
        margin-bottom: 1rem;
  }
  .btns .el-form-item__content {
        margin-left: 0 !important;
  }
  .btns img {
    width: 6.5rem;
    height: 5rem;
  }
  .code img {
        width: 6rem;
    }
  .SignUp .session{
    font-size: .64rem;
  }
  .SignUp a{
    font-size: .64rem;
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
    import store from "../store";

    export default {
        name: "SignIn",
        data() {
            return {
                email:'',
                password:'',
            };

        },
        methods: {
            // 对邮箱格式进行验证
            checking(){
                var email = this.email;
                console.log(email)
		        var reg = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
                if(!reg.test(email)){
                    this.$notify({
                        title: '警告',
                        message: '邮箱格式有误！请重新输入！',
                        type: 'warning'
                    });
                    this.email = ''
                }
            },
            saveState() {
                sessionStorage.setItem('state', JSON.stringify(this.$store.state))
            },
            // 登录
            Login(){
                if(this.email && this.password){
                    this.$axios({
                        method:'post',
                        url:'/ajax/sign_in',
                        data:this.qs.stringify({
                            userName:this.email,
                            password:this.password,
                        }),
                        headers:{
                            'Content-Type': 'application/x-www-form-urlencoded',
                        }
                    }).then((response)=>{
                        if(response.data.sign_in===200){
                            store.commit('login_in')
                            store.commit('setUserName',this.email)
                            this.saveState()
                            this.$router.push('/Home/hotAudio')
                        }else{
                            this.$notify({
                                title: '警告',
                                message: '请检查你的邮箱和密码是否输入正确！',
                                type: 'warning'
                            });
                        }
                    }).catch((error)=>{
                        console.log(error)
                    })
                }else{
                    this.$notify({
                        title: '警告',
                        message: '邮箱和密码不能为空！',
                        type: 'warning'
                    });
                }
            },

        },
    }
</script>

