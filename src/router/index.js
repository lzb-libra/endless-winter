import { createRouter, createWebHistory } from "vue-router";
import Hero from "../views/Hero.vue";
import HeroDetail from "../views/HeroDetail.vue";
import Pet from "../views/Pet.vue";
import Activity from "../views/Activity.vue";
import Expert from "../views/Expert.vue";
import Logs from "../views/Logs.vue";
import Chat from "../views/Chat.vue";

import Seat from "../views/tools/Seat.vue";

const routes = [
	{ path: "/", redirect: "/hero" },
	{ path: "/hero", name: "Hero", component: Hero },
	{ path: "/heroDetail/:id", name: "HeroDetail", component: HeroDetail },
	{ path: "/pet", name: "Pet", component: Pet },
	{ path: "/chat", name: "Chat", component: Chat },
	{ path: "/expert", name: "Expert", component: Expert },
	{ path: "/activity", name: "Activity", component: Activity },
	{ path: "/seat", name: "Seat", component: Seat },
	{ path: "/logs", name: "Logs", component: Logs },
];

const router = createRouter({
	history: createWebHistory("/endless-winter/"),
	routes,
});

export default router;
