import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import News from "../views/News.vue";
import Tournaments from "../views/Tournaments.vue";
import Players from "../views/Players.vue";
import Matches from "../views/Matches.vue";

const routes = [
  { path: "/", component: Home, name: "Home" },
  { path: "/news", component: News, name: "News" },
  { path: "/tournaments", component: Tournaments, name: "Tournaments" },
  { path: "/players", component: Players, name: "Players" },
  { path: "/matches", component: Matches, name: "Matches" },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
