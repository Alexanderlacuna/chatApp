import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "@/assets/css/tailwind.css";
import vuetify from "./plugins/vuetify";
import socketio from "socket.io-client";
import VueSocketIO from "vue-socket.io";

// export const SocketInstance = socketio('http://localhost:5000');

Vue.config.productionTip = false;
Vue.use(new VueSocketIO({
  debug: true,
  connection: socketio('http://127.0.0.1:5000',{}), //options object is Optional
  vuex: {
    store,
    actionPrefix: "SOCKET_",
    mutationPrefix: "SOCKET_"
  }
})
);
new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
