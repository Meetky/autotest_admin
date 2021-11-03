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
      <el-form label-width="60px">
        <el-form-item label="用户名">
          <el-input v-model="username"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input type="password" v-model="password"></el-input>
          <span v-if="!this.verify" style="font-size: 10px; color: red"
            >用户名或密码输入错误</span
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
import axios from "axios";
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      verify: true,
    };
  },
  methods: {
    login() {
      if (this.username === "" || this.password === "") {
        console.log("输入为空");
        this.$message({
          showClose: true,
          message: "账号或密码输入不能为空",
          type: "error",
        });
      } else {
        axios
          .post(
            "/api/login/",
            JSON.stringify({ username: this.username, password: this.password })
          )
          .then(
            (response) => {
              if (
                response.data.code === 200 &&
                response.data.message === "success"
              ) {
                this.$router.push("/home");
              } else if (response.data.code === 500) {
                this.verify = false;
              } else {
                this.verify = false;
              }
            },
            (error) => {
              console.log("请求失败", error.message);
              this.verify = false;
            }
          );
      }
    },
    regist() {
      axios.get("/api/login/").then(
        (response) => {
          console.log(response.data);
          this.$message.error("还不支持注册噢");
        },
        (error) => {
          console.log("请求失败", error.message);
          this.$message.error("还不支持注册噢");
        }
      );
    },
  },
};
</script>

<style lang="scss">
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
  .btn {
    margin-right: 46px;
  }
}
</style>