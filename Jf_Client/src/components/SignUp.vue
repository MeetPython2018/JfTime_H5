<template>
    <div id="signUp">
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
            </div>
        </div>
        <!--<div class="container-full">-->
            <!--<div class="row">-->
                <!--<el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px"-->
                         <!--class="demo-ruleForm col-xs-8 col-lg-4">-->
                    <!--<div class="title">-->
                        <!--<span>注册账号</span>-->
                    <!--</div>-->
                    <!--<el-form-item label="账  号" prop="userName">-->
                        <!--<el-input v-model="ruleForm.userName" placeholder="邮箱地址"></el-input>-->
                    <!--</el-form-item>-->
                    <!--<el-form-item label="密  码" prop="pass" hide-required-asterisk="1">-->
                        <!--<el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>-->
                    <!--</el-form-item>-->
                    <!--<el-form-item label="确认密码" prop="checkPass">-->
                        <!--<el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>-->
                    <!--</el-form-item>-->
                    <!--<div class="btns">-->
                        <!--<el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>-->
                        <!--<el-button @click="resetForm('ruleForm')">重置</el-button>-->
                    <!--</div>-->
                    <!--<div class="SignIn">-->
                        <!--<router-link to="/SignIn">已有账号，直接登录!</router-link>-->
                    <!--</div>-->
                <!--</el-form>-->
            <!--</div>-->
        <!--</div>-->
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
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        padding: 0;
        margin: 0;
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





    .navs {
        width: 100%;
        background: #343a40 !important;
    }

    .el-header {
        max-width: 1200px !important;
        margin: 0 auto;
        padding: 0 !important;
    }

    .row{
        width: 100%;
        height: auto;
        padding: 2rem 0;
        margin: 0 auto;
    }

    .el-main {
        padding: 0 !important;
        max-width: 1260px !important;
        margin: 0 auto;
        background: #f5f5f5 !important;
    }

    .demo-ruleForm {
        width: 25rem;
        height: auto;
        background: #fff;
        padding: 1rem 2rem;
        margin: 0 auto;
        border-radius: 1rem;
    }
    .el-form-item{
        margin-bottom: 1rem!important;
    }
    .title{
        height: 2.5rem;
        font-size: 1.2rem;
        color: #a06619;
        line-height: 2.5rem;
        margin-bottom: 1rem;
    }
    .btns{
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .btns .el-form-item__content {
        margin-left: 0 !important;
    }

    .btns img{
        width: 6.5rem;
        height: 5rem;
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
    .SignIn{
        height: 2.5rem;
        line-height: 2.5rem;
        display: flex;
        justify-content: flex-end;
        font-size: .64rem;
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
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        console.log(this.ruleForm)
                        let userName = this.ruleForm["userName"]
                        let password = this.ruleForm["pass"]

                        fetch("/ajax/sign_up?userName="+userName+'&password='+password).then(function (e) {
                           return e.json()
                        }).then(e=>{
                            if(e[0]["sign_up"]===200){
                                this.$router.push('/SignIn')
                            }else {
                                alert("该注册失败！")
                            }

                        })
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        }
    }
</script>

