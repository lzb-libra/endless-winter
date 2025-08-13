import { createRouter, createWebHistory } from "vue-router";
import Hero from "../views/Hero.vue";
import Pet from "../views/Pet.vue";
import Activity from "../views/Activity.vue";
import Expert from "../views/Expert.vue";
import About from "../views/About.vue";

const routes = [
	{ path: "/", redirect: "/hero" },
	{ path: "/hero", name: "Hero", component: Hero },
	{ path: "/pet", name: "Pet", component: Pet },
	{ path: "/expert", name: "Expert", component: Expert },
	{ path: "/activity", name: "Activity", component: Activity },
	{ path: "/about", name: "About", component: About },
];

const router = createRouter({
	history: createWebHistory("/endless-winter/"),
	routes,
});

export default router;
