import {
    get,
    post
} from "@/utils/request.js"

export const testApi = () => {
    const header = {
        "Authorization": "Token " + localStorage.getItem("token")
    }
    get("/testApi/", header)
}