import {
    get,
    post
} from "@/utils/request.js"

export const login = (loginForm) => post("/login/", loginForm)
// const login = (loginForm) => {
//     post("/login/", loginForm)
// }