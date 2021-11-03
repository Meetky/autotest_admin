import Vue from 'vue'
import Router from "vue-router"
//引入路由器
import router from './router'
// //按需引入element-ui组件
// import {
//   Button,
//   Card
// } from "element-ui"

// import App from './App.vue'

// Vue.component(Button.name, Button);
// Vue.component(Card.name, Card);

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue';

Vue.use(ElementUI);
Vue.use(Router)
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
  beforeCreate() {
    Vue.prototype.$bus = this //安装全局事件总线
  },
}).$mount('#app')