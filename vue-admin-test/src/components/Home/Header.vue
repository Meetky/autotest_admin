<template>
  <el-row>
    <el-col>
      <el-button
        class="openBar"
        type="primary"
        icon="el-icon-s-fold"
        @click="sendNavBarStatus"
      ></el-button>
      <el-dropdown trigger="click">
        <span class="el-dropdown-link">
          <el-avatar
            src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
          ></el-avatar>
          {{ this.$route.query.username
          }}<i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item icon="el-icon-switch-button"
            ><span @click="logout">退出登录</span></el-dropdown-item
          >
          <el-dropdown-item
            ><span @click="test">测试token</span></el-dropdown-item
          >
          <el-dropdown-item
            ><span @click="testApi1">测试testApi</span></el-dropdown-item
          >
        </el-dropdown-menu>
      </el-dropdown>
    </el-col>
  </el-row>
</template>

<script>
import { verifyToken } from "@/api/token.js";
import { get } from "@/utils/request.js";
import axios from "axios";
export default {
  name: "Header",
  data() {
    return {
      nickname: "",
    };
  },
  methods: {
    sendNavBarStatus() {
      this.$bus.$emit("navBarStatus");
    },
    logout() {
      console.log("用户点击退出了");
      localStorage.removeItem("token");
      this.$router.push("/");
    },
    test() {
      verifyToken();
    },
    testApi1() {
      const header = {
        Authorization: "Token " + localStorage.getItem("token"),
      };
      // axios.get("/api/testApi/", { headers: header }).then((response) => {
      //   console.log(response.data);
      // });
      get("/testApi/");
    },
  },
};
</script>

<style>
/* 头像和昵称 */
.el-dropdown {
  float: right;
  font-size: 16px;
  margin-right: 8px;
  margin-top: 7px;
}
/* 导航栏展开收起按钮 */
.openBar {
  float: left;
  height: 60px;
  font-size: 25px;
  color: black;
  background: #b3c0d1;
  border: 0px;
}
</style>