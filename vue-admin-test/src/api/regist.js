import {
    get,
    post
} from "@/utils/request.js"

export const register = (registerFormData) => post("/register/", registerFormData)