<template>
  <div id="signUp">
    <div class="container-full">
      <div class="cons">
        <el-main>
          <div class="login-div">
          <ul>
            <div class="logo"></div>
            <div class="title">江峰时刻</div>
          </ul>
          <div class="fields">
            <div class="username">
                            <i class="iconfont icon-youxiang-copy"></i>
                            <input type="username"  @blur="checking" v-model="email" class="user-input" placeholder="username" />
                        </div>
            <div class="password">
              <i class="iconfont icon-mima"></i>
              <input type="password"  maxlength="16" v-on:input="intensity" v-model="password" class="pass-input" placeholder="password" />
            </div>
            <div class="strong">
                              <ul>
                                  <span>密码强度</span>
                                  <el-rate
                              v-model="value"
                              disabled
                              disabled-void-color="#ccc"
                              :max="max"
                              :low-threshold="low_threshold"
                              :high-threshold="high_threshold"
                              text-color="#000"
                              :colors="colors"
                              score-template="{value}">
                            </el-rate>
                              </ul>
                              <ul>
                                  <li>
                                  <i class="iconfont icon-yuanquan" :class=" pick1===0 ? 'icon-yuanquan':'icon-duihao'"></i>
                                  <span>6-16个字符</span>
                              </li>
                                  <li>
                                  <i class="iconfont icon-yuanquan" :class=" pick2===0 ? 'icon-yuanquan':'icon-duihao'"></i>
                                  <span>只能包含大小写字母、数字、非空字符</span>
                              </li>
                              </ul>
                          </div>
          </div>
          <button class="signin-button" @blur="Login">Login</button>
          <div class="link">
                          <a href="#">No account ?</a> or <router-link to="/SignIn">Sign in</router-link>
                      </div>
        </div>
        </el-main>
      </div>
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
    </div>
    <router-view/>
  </div>
</template>
<style scoped>
  * {
      padding: 0;
      margin: 0;
      font-family: '苹方';
  }
  #signUp {
      width: 100%;
      height: auto;
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
  .strong{
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      align-items: center;
      margin-bottom: 1rem;
  }
  .strong ul:first-child{
      width: 100%;
      display: flex;
      justify-content: flex-start;
      align-items: center;
  }
  .strong ul:last-child{
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-start;
      list-style: none;
  }
  .strong ul:last-child li{
      display: flex;
      justify-content: flex-start;
      align-items: center;
  }
  .icon-yuanquan{
      margin-top: .2rem;
      padding-right: .3rem;
  }
  .icon-duihao{
      color: #2DAF7D;
  }
  .el-rate{
      display: flex;
      justify-content: flex-start;
      align-items: center;
      margin-left: .5rem;
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
      font-size: 1.2rem;
      color: #a06619;
      line-height: 2.5rem;
      margin-bottom: 1rem;
  }
  .btns .el-form-item__content {
      margin-left: 0 !important;
  }
  .btns img{
      width: 6.5rem;
      height: 5rem;
  }
  .code img {
      width: 6rem;
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
  export default {
    name: "SignUp",
    data() {
      return {
        pick1:0,
        pick2:0,
        email:'',
        password:'',
        value: 0,
        colors:['#FF4B47','#F9AE35','#2DAF7D'],
        iconClasses:['el-icon-unlock','el-icon-lock','el-icon-lock'],
        max:8,
        low_threshold:3,
        high_threshold:5
      };
    },
    methods: {
      // 密码强度检测
      intensity(){
                var value = this.password
                var value_length = value.length;
                var code_length = 0;
                if (/[0-9]/.test(value)) {
                    code_length++;
                }
                if (/[a-z]/.test(value)) {
                    code_length++;
                }
                if (/[A-Z]/.test(value)) {
                    code_length++;
                }

                //密码是否包含除数字和字母之外的字符
                if(value_length >= 6){
                    this.pick1 = 1
                }else {
                    this.pick1 = 0
                }
                if (!/\s/.test(value) && !/[^a-zA-Z0-9]/.test(value) && code_length > 2) {
                    this.pick2 = 1
                }else {
                    this.pick2 = 0
                }


    //安全级别
    if (code_length >= 2 && value_length >= 15) {
        this.value = 7
        console.log('高')
    } else if (code_length >= 2 && value_length >= 10) {
        this.value = 4
        console.log('中')
    } else if (code_length >= 1 && value_length >= 6) {
        this.value = 3
        console.log('低')
    }else {
        this.value = 0
    }
    // if (value_length >= 6 && value_length <= 20 && code_length >= 2) flag = true;
    // return flag;


            },
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
      // 登录
      Login(){
                if(this.email && this.password){
                    fetch("/ajax/sign_up?userName="+this.email+'&password='+this.password).then(function (e) {
                     return e.json()
                    }).then(e=>{
                        if(e[0]["sign_up"]===200){
                                this.$router.push('/SignIn')
                        }else{
                            this.$notify({
                                title: '警告',
                                message: '请检查你的邮箱和密码是否输入正确！',
                                type: 'warning'
                            });
                        }
                    })
                }else{
                    this.$notify({
                        title: '警告',
                        message: '邮箱和密码不能为空！',
                        type: 'warning'
                    });
                }

            },
    }
  }
</script>

