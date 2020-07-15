import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Client from "@/components/Client.vue";
import Account from "@/components/Account.vue";
import ClientDetail from "@/components/ClientDetail.vue";
import Savings from "@/components/Savings.vue";
import Checking from "@/components/Checking.vue";
import NotFound from "@/views/404.vue";
// import Homepage from "@/views/Homepage/Homepage.vue";
Vue.use(VueRouter);

const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err);
};

const routes = [
  {
    path: "/",
    component: Home,
    children: [
      {
        path: ""
      },
      {
        path: "client",
        component: Client
      },
      {
        path: "client/:id",
        component: ClientDetail
      },
      {
        path: "account",
        component: Account
      },
      {
        path: "savings",
        component: Savings
      },
      {
        path: "checking",
        component: Checking
      },
      {
        path: "404",
        component: NotFound
      },
      {
        path: "*",
        component: NotFound
      }
    ]
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/bank",
    component: Home
  }
];

const router = new VueRouter({
  mode: "hash",
  base: process.env.BASE_URL,
  routes
});

export default router;
