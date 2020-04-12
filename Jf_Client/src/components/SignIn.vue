<template>
    <div id="signIn">
        <div class="container-full">
            <div class="cons">
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
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        height: 35rem;
        background: #ecf0f3;
    }
    .container-full{
        width: 100%;
        height: 100%;
        max-width: 1260px;
        padding: 0 1.5rem;
        margin: 0 auto;
        display: flex;
        justify-content: flex-end;
        align-items: flex-start;
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
        margin-top: 2rem;
    }
    @media screen and (max-width: 600px) { /*当屏幕尺寸小于600px时，应用下面的CSS样式*/
        .container-full{
            display: flex;
            justify-content: center;
            align-items: flex-start;
        }
      .login-div{
            width: 28rem;
            height: auto;
            padding: 2rem 1.5rem 1.5rem 1.5rem;
            border-radius: 2rem;
            background: #ecf0f3;
            box-shadow: 13px 13px 20px #cbced1,
                  -13px -13px 20px #ffffff;
            margin-top: 2rem;
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

    .row{
        /*width: 100%;*/
        /*height: auto;*/
        /*padding: 2rem 0;*/
        margin: 2rem auto;
        width:430px;
        height: 500px;
        padding: 60px 35px 35px 35px;
        border-radius: 40px;
        background: #ecf0f3;
        box-shadow: 13px 13px 20px #cbced1,
              -13px -13px 20px #ffffff;
    }
    .el-main {
        padding: 0 !important;
        max-width: 1260px !important;
        margin: 0 auto;
        background: #f5f5f5 !important;
    }

    .demo-ruleForm {
        width: 30rem;
        height: auto;
        background: #fff;
        padding: 2rem;
        margin: 0 auto;
        border-radius: 1rem;
    }
    .title{
        height: 2.5rem;
        font-size: 1.1rem;
        color: #a06619;
        line-height: 2.5rem;
        margin-bottom: 1rem;
    }
    .el-form-item__label{
        width: 5rem!important;
    }
    .btns{
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .btns .el-form-item__content {
        margin-left: 0 !important;
    }

    .btns img {
        width: 6.5rem;
        height: 5rem;
        /*margin-left: 0!important;*/
    }
    .el-button{
        padding: .5rem 1rem;
        display: flex;
        justify-items: center;
        align-items: center;
        font-size: .64rem;
    }

    .codde {
        width: 100%;
        display: flex;
        justify-content: flex-start;
        margin-bottom: 1rem;
    }

    .code img {
        width: 6rem;
    }
    .code-input {
        width: 6rem;
        float: left;
        margin-right: 1rem;
    }
    .SignUp{
        height: 2.5rem;
        line-height: 2.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 1.2rem;
    }
    .SignUp .session{
        font-size: .64rem;
    }
    .SignUp a{
        font-size: .64rem;
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
                            console.log(response.data)
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

