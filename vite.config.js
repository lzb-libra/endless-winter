import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import AutoImport from "unplugin-auto-import/vite";
import Components from "unplugin-vue-components/vite";
import vueDevTools from "vite-plugin-vue-devtools";
import { NaiveUiResolver } from "unplugin-vue-components/resolvers";

export default defineConfig({
	base: "/endless-winter/",
	plugins: [
		vue(),
		vueDevTools(),
		AutoImport({
			imports: ["vue", "vue-router"], // 自动导入 Vue 和 Vue Router API
			resolvers: [NaiveUiResolver()], // 自动解析 Naive UI 组件
		}),
		Components({
			resolvers: [NaiveUiResolver()], // 自动注册 Naive UI 组件
		}),
	],
	resolve: {
		alias: {
			"@": fileURLToPath(new URL("./src", import.meta.url)),
		},
	},
});
