<template>
  <el-container>
    <div style="float: left">
      <Aside></Aside>
    </div>
    <div class="main" style="float: left">
      <el-header><Header></Header></el-header>
      <el-main>Main</el-main>
    </div>
  </el-container>
</template>

<script>
import Header from "./Header.vue";
import Aside from "./Aside.vue";
export default {
  name: "Home",
  components: {
    Header,
    Aside,
  },
};
</script>

<style>
.el-header {
  background-color: #b3c0d1;
  padding: 0px;
  height: 50px;
}
.main {
  position: static;
  height: 100%;
  width: 100%;
}
.main > .el-main {
  position: fixed;
  height: 100%;
  width: 100%;
}

/* .el-aside {
  background-color: #d3dce6;
  color: #333;
  line-height: 200px;
} */

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
}
/* 
body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
} */
</style>
