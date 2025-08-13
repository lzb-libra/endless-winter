<template>
	<n-config-provider :theme="darkTheme">
		<n-layout class="app-container">
			<n-layout-header class="main-menu">
				<n-menu v-model:value="activeKey" mode="horizontal" :options="menuOptions" responsive />
			</n-layout-header>
			<n-layout-content class="main-content">
				<router-view />
			</n-layout-content>
		</n-layout>
	</n-config-provider>
</template>

<script setup>
import { h, onMounted, ref } from "vue";
import { RouterLink } from "vue-router";
import { NConfigProvider, NLayout, NLayoutHeader, NLayoutContent, darkTheme } from "naive-ui";

const activeKey = ref("hero");

const menuOptions = [
	{
		label: () =>
			h(
				RouterLink,
				{
					to: {
						name: "Hero",
					},
				},
				{ default: () => "英雄" }
			),
		key: "hero",
	},
	{
		label: () =>
			h(
				RouterLink,
				{
					to: {
						name: "Pet",
					},
				},
				{ default: () => "宠物" }
			),
		key: "pet",
	},
	{
		label: () =>
			h(
				RouterLink,
				{
					to: {
						name: "Expert",
					},
				},
				{ default: () => "专家" }
			),
		key: "expert",
	},
	{
		label: () =>
			h(
				RouterLink,
				{
					to: {
						name: "Activity",
					},
				},
				{ default: () => "活动" }
			),
		key: "activity",
	},
	{
		label: () =>
			h(
				RouterLink,
				{
					to: {
						name: "About",
					},
				},
				{ default: () => "关于" }
			),
		key: "about",
	},
];

onMounted(() => {
	const pathname = window.location.pathname;
	activeKey.value = pathname.replace("/endless-winter/", "");
});
</script>

<style scoped>
.app-container {
	min-height: 100vh;
}

.main-menu {
	padding: 20px;
	position: fixed;
	z-index: 999;
	width: 1650px;
}

.main-content {
	margin-top: 100px;
	margin-bottom: 20px;
}
</style>
