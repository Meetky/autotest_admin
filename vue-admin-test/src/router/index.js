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
            path: "/register",
            component: () => import("@/components/Register")
        },

        {
            name: "home",
            path: '/home',
            component: () => import("@/components/Home"),
            hidden: true,
            redirect: "/main",
            children: [{
                path: "/main",
                component: () => import("@/components/Home/Main")
            }, {
                name: "site",
                path: "/site",
                component: () => import("@/components/Site"),
                // hidden: true
            }]
        },


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
        if (to.path === '/login' || to.path === "/register") {
            next();
        } else {
            next('/')
        }
    }

})

// 解决重复点击导航报错 Uncaught (in promise) NavigationDuplicated: Avoided redundant navigation to current location
const VueRouterPush = Router.prototype.push
Router.prototype.push = function push(to) {
    return VueRouterPush.call(this, to).catch(err => err)
}

//暴露router
export default router