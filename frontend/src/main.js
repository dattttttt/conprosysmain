import { createApp } from "vue"
import App from "./App.vue"
import router from "./router"
// import store from "./store" // bỏ nếu chưa dùng plugin đúng
import "./assets/styles.css"
import FontAwesomeIcon from './icons'

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router)
// app.use(store) // chỉ dùng nếu store đúng dạng plugin
app.mount("#app")
