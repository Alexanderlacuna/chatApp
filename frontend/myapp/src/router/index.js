import Vue from "vue";
import VueRouter from "vue-router";
import home from "@/components/home.vue";
import login from "@/components/auth/login.vue";
import register from "@/components/auth/register.vue";


Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: home
  },
  {
    path:"/login",
    name:"login",
    component:login
  },

  {
  path:"/register",
  name:"register",

  component:register
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
