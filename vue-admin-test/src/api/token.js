import {
    get,
    post
} from "@/utils/request.js"

export const verifyToken = () => get("/token/")