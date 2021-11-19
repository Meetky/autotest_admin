<template>
  <div>
    <div class="reg-bg">
      <img src="@/assets/login.jpg" />
    </div>
    <div class="reg-form">
      <div class="showInfo">
        <h3>注册</h3>
      </div>
      <div class="formdata">
        <el-form
          :model="registerForm"
          :rules="rules"
          ref="registerForm"
          label-width="100px"
          class="demo-ruleForm"
        >
          <el-form-item label="用户名" prop="username">
            <el-input
              v-model="registerForm.username"
              placeholder="请输入用户名"
              autocomplete="off"
              style="width: 321px"
              clearable
            ></el-input>
          </el-form-item>
          <el-form-item label="邮箱" prop="email">
            <el-input
              v-model="registerForm.email"
              placeholder="请输入邮箱"
              autocomplete="off"
              style="width: 321px"
              clearable
            ></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password1">
            <el-input
              placeholder="请输入密码"
              v-model="registerForm.password1"
              style="width: 321px"
            >
            </el-input>
          </el-form-item>
          <el-form-item label="确认密码" prop="password2">
            <el-input
              placeholder="再次输入密码"
              v-model="registerForm.password2"
              style="width: 321px"
            >
            </el-input
            ><br />
            <p v-if="this.errorInfo" style="font-size: 10px; color: #f56c6c">
              {{ errorInfo }}
            </p>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm">注册</el-button>
            <el-button @click="backToLogin">返回登录</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import { register } from "@/api/regist.js";
export default {
  data() {
    return {
      registerForm: {
        username: "",
        password1: "",
        password2: "",
        email: "",
      },
      errorInfo: "",
      rules: {
        username: [
          { required: true, message: "用户名不能为空" },
          { trigeer: "change" },
        ],
        email: [
          { required: true, message: "邮箱不能为空" },
          {
            pattern: /^([a-zA-Z0-9]+[-_\.]?)+@[a-zA-Z0-9]+\.[a-z]+$/,
            message: "邮箱格式不正确",
            trigger: "blur",
          },
        ],
        password1: [
          { required: true, message: "密码不能为空" },
          {
            pattern: /^(\w){5,16}$/,
            message: "只能输入5-16个字母、数字、下划线",
            trigger: "blur",
          },
        ],
        password2: [
          { required: true, message: "密码不能为空" },
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
    submitForm() {
      if (this.registerForm.password1 !== this.registerForm.password2) {
        this.errorInfo = "密码不一致";
      } else {
        register(this.registerForm).then(
          (response) => {
            console.log(response.data);
          },
          (error) => {
            console.log(error.message);
          }
        );
        console.log(this.registerForm);
      }
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    backToLogin() {
      this.$router.push({
        path: "/",
      });
    },
  },
};
</script>

<style lang="scss">
/* 注册页面背景 */
.reg-bg {
  position: fixed;
  /* background: url("@/../../../assets/login.jpg"); */
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background-size: cover;
}
.reg-bg img {
  width: 100%;
  height: 100%;
}

.reg-form {
  position: absolute;
  right: 139px;
  top: 50%;
  margin-top: -340px;
  width: 480px;
  height: 680px;
  background: rgba(221, 212, 221, 0.5);
  border-radius: 12px;
  overflow: hidden;
}
.showInfo {
  margin: 50px 0px 22px 39px;
}
.showInfo h3 {
  font-size: 36px;
  padding-bottom: 4px;
}
/* form表单的div样式 */
.formdata {
  padding-top: 48px;
  position: relative;
  width: 720px;
  overflow: hidden;
  /* float: left; */
}
.demo-ruleForm {
  margin: 0;
  padding: 0;
}

/* 按钮动画 */
button:hover {
  box-shadow: 0px 15px 20px rgba(209, 212, 211, 0.4);
  transform: translateY(-7px);
}

button:active {
  transform: translateY(-1px);
}
</style>