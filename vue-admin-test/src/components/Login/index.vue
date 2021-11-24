<!--
 * @Description  : 
 * @Author       : Concon
 * @Date         : 2021-10-28 21:50:46
 * @LastEditors  : Concon
 * @LastEditTime : 2021-10-30 12:11:46
 * @FilePath     : \\Projects\\TestPlatform\\VueDemo\\vue-admin-test\\vue-admin-test\\src\\components\\Login\\index.vue
 * Copyright (C) 2021 Concon. All rights reserved.
-->
<template>
  <div class="loginPage">
    <el-card class="box-card" shadow="hover">
      <h3>登录页面</h3>
      <el-form
        :rules="rules"
        :model="loginForm"
        label-width="80px"
        label-color="red"
      >
        <el-form-item label="用户名" prop="username">
          <el-input
            prefix-icon="el-icon-user-solid"
            v-model="loginForm.username"
          ></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input
            type="password"
            prefix-icon="el-icon-lock"
            v-model="loginForm.password"
            show-password
          ></el-input>
          <span
            v-if="this.loginForm.errorInfo"
            style="font-size: 10px; color: red"
            >{{ loginForm.errorInfo }}</span
          >
        </el-form-item>
        <el-form-item class="btn">
          <el-button type="primary" @click="login">登录</el-button>
          <el-button @click="regist">注册</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import { login } from "@/api/login.js";
export default {
  name: "Login",
  data() {
    return {
      loginForm: {
        username: "",
        password: "",
        errorInfo: "",
      },
      rules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          {
            pattern: /^(?!\s+).*(?<!\s)$/,
            message: "首尾不能为空格",
            trigger: "change",
          },
        ],
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          {
            pattern: /^(\w){5,16}$/,
            message: "只能输入5-16个字母、数字、下划线",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    login() {
      if (this.loginForm.username === "" || this.loginForm.password === "") {
        console.log("输入为空");
        this.$message({
          showClose: true,
          message: "账号或密码输入不能为空",
          type: "error",
        });
      } else {
        // axios({
        //   method: "post",
        //   url: "/api/login/",
        //   data: {
        //     username: this.username,
        //     password: this.password,
        //   },
        // }).then(
        login({
          username: this.loginForm.username,
          password: this.loginForm.password,
        }).then(
          (response) => {
            if (response.status === 200 && response.data.result) {
              localStorage.setItem(
                "token",
                // JSON.stringify(response.data.detail.token) token转成字符串后，后端无法校验
                response.data.detail.token
              );
              //登录成功,跳转至首页,传递用户名
              this.$router.push({
                path: "/home",
                query: {
                  username: this.loginForm.username,
                },
              });
            } else {
              this.loginForm.errorInfo = response.data.errorInfo;
            }
          },
          (error) => {
            console.log("请求失败", error.message);
            this.$message({
              showClose: true,
              message: "服务器抛锚啦！请耐心等待...",
              type: "error",
            });
          }
        );
      }
    },
    // regist() {
    //   register().then(
    //     (response) => {
    //       console.log(response.data);
    //       this.$message.error("还不支持注册噢");
    //     },
    //     (error) => {
    //       console.log("请求失败", error.message);
    //       this.$message.error("还不支持注册噢");
    //     }
    //   );
    // },
    regist() {
      this.$router.push({
        path: "/register",
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.loginPage {
  background: url("@/../../../assets/login.jpg");
  background-size: 100% 100%;
  text-align: center;
  position: fixed;
  height: 100%;
  width: 100%;

  .box-card {
    width: 480px;
    margin: 0 auto;
    border: 0px;
    margin-top: 230px;
    background: Transparent;
    span {
      float: right;
    }
  }
  .box-card:hover {
    background: rgba(0, 0, 0, 0.3);
    border-radius: 100px;
  }
  .btn {
    margin-right: 46px;
  }
}
button:hover {
  box-shadow: 0px 15px 20px rgba(175, 177, 176, 0.4);
  transform: translateY(-7px);
}

button:active {
  transform: translateY(-1px);
}
</style>