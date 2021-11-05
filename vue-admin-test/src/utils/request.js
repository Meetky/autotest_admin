import axios from "axios"
import {
    MessageBox
} from 'element-ui';

//新建axios实例
let instance = axios.create({
    baseURL: "/api"
})

//请求拦截器
instance.interceptors.request.use(
    //在发送请求前
    request => {
        const auth = "Token " + localStorage.getItem("token");
        request.headers.Authorization = auth
        return request;
    },
    //出现错误
    error => {
        console.log("#出错咯！", error)
        return Promise.reject(error);
    }

)

//响应拦截器
instance.interceptors.response.use(
    response => {
        return response;
    },
    error => {
        // 后端验证token过期以后 会返回401 
        if (error.response.status == 401) {
            MessageBox.confirm('登录过期，请重新登录', '确定登出', {
                confirmButtonText: '重新登录',
                // 禁用各种取消弹窗操作,强制点击重新登录按钮
                showCancelButton: false,
                showClose: false,
                closeOnClickModal: false,
                closeOnPressEscape: false,
                type: 'warning'
            }).then(() => {
                // 调用接口退出登录
                get('/logout/').then(response => {
                    // 移除本地缓存的token
                    localStorage.removeItem("token");
                    location.reload();
                })
            })
        }
        return Promise.reject(error);
    }
)

//封装get请求
export function get(url, params) {
    return new Promise((resolve, reject) => {
        instance.get(url, {
            params
        }).then(response => {
            resolve(response)
        }).catch(error => {
            reject(error)
        })
    })
}

//封装post请求
export function post(url, params) {
    return new Promise((resolve, reject) => {
        instance.post(url, params)
            .then(response => {
                resolve(response)
                // return resolve(response)
            }).catch(error => {
                reject(error)
            })
    })
}