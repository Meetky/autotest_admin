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
          {{ username }}<i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item icon="el-icon-switch-button"
            ><span @click="logout">退出登录</span></el-dropdown-item
          >
        </el-dropdown-menu>
      </el-dropdown>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      username: "Concon",
    };
  },
  methods: {
    sendNavBarStatus() {
      this.$bus.$emit("navBarStatus");
    },
    logout() {
      console.log("用户点击退出了");
      this.$router.push("/");
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