import axios from "axios"

//新建axios实例
let instance = axios.create({
    baseURL: "/api"
})

//请求拦截器
instance.interceptors.request.use(
    //在发送请求前
    request => {
        const auth = "Token" + localStorage.getItem("token");
        request.headers.Authorization
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