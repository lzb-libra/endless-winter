<template>
	<n-config-provider :theme="isDarkMode ? darkTheme : lightTheme">
		<n-layout style="height: 100vh;">
			<n-layout-header position="absolute" style="padding: 5px 5vw;" bordered>
				<n-menu v-model:value="activeKey" mode="horizontal" :options="menuOptions" responsive />
			</n-layout-header>
			<n-layout-content position="absolute" style="padding: 52px 5vw 70px 5vw;" bordered>
				<n-message-provider>
					<router-view />
				</n-message-provider>
			</n-layout-content>
			<n-layout-footer position="absolute" style="text-align: center; padding: 15px 5vw;" bordered>
				<span style="padding-right: 3px;">{{ `Copyright &copy; ${new Date().getFullYear()}` }}</span>
				<a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener noreferrer">蒙ICP备2025029497号</a>
			</n-layout-footer>
		</n-layout>
	</n-config-provider>
</template>

<script setup>
import { h, onMounted, ref, onUnmounted, watch } from "vue";
import { RouterLink, useRoute } from "vue-router";
import { NConfigProvider, NLayout, NLayoutHeader, NLayoutContent, darkTheme, lightTheme } from "naive-ui";

const route = useRoute();
const activeKey = ref("hero");
const isDarkMode = ref(false);

const darkModeQuery = window.matchMedia('(prefers-color-scheme: dark)');

const isPC = () => {
  const ua = navigator.userAgent.toLowerCase();
  const mobiles = ['mobile', 'android', 'iphone', 'ipod', 'ipad', 'windows phone'];
  for (let m of mobiles) {
    if (ua.includes(m)) return false;
  }
  return true;
}

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
						name: "Chat",
					},
				},
				{ default: () => "图表" }
			),
		key: "chat",
	},
	{
		label: () =>
			h(
				RouterLink,
				{
					to: {
						name: "Seat",
					},
				},
				{ default: () => "工具" }
			),
		key: "seat",
		show: isPC(),
	},
	{
		label: () =>
			h(
				RouterLink,
				{
					to: {
						name: "Logs",
					},
				},
				{ default: () => "日志" }
			),
		key: "logs",
	},
];

const updateSystemScheme = e => {
	isDarkMode.value = e.matches
}

watch(() => route.path, newPath => {
	console.log(newPath);

	let pathname = window.location.pathname;
	pathname = pathname.replace("/endless-winter/", "");
	if(pathname.includes('hero')) pathname = 'hero';
	activeKey.value = pathname;
});

onMounted(() => {
	darkModeQuery.addEventListener('change', updateSystemScheme);
	isDarkMode.value = darkModeQuery.matches
});
</script>

<style scoped></style>
