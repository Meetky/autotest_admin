//引入VueRouter
import Router from 'vue-router'
import Login from "@/components/Login"


//创建router实例对象，去管理一组一组的路由规则
const router = new Router({
    routes: [{
            path: '/',
            redirect: '/login'
        },
        {
            path: '/login',
            component: Login
        },
        {
            name: "home",
            path: '/home',
            component: () => import("@/components/Home")
        }

    ]
})

//定义前置路由守卫
router.beforeEach((to, from, next) => {
    let token = localStorage.getItem("token");
    if (token) {
        // token存在 访问login 跳转至产品证书制作页面
        if (to.path == '/' || to.path == '/login') {
            next('/home');
        } else {
            next();
        }
    } else {
        // token不存在  路径'/login'就是登录页面设置的path
        if (to.path === '/login') {
            next();
        } else {
            next('/')
        }
    }

})

//暴露router
export default router