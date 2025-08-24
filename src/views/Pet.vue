<template>
	<div style="padding: 0px 15px;">
		<n-flex>
			<n-card v-for="(obj, index) in allPets" :key="index" :title="obj.name" :hoverable="true" :embedded="true"
				size="small" header-style="text-align: center" footer-style="text-align: center"
				style="width: 208px; cursor: pointer">
				<template #header-extra>
					<span v-if="obj.level === '良好'" style="color: #67ee7a">{{ obj.level }}</span>
					<span v-if="obj.level === '稀有'" style="color: #70b8f1">{{ obj.level }}</span>
					<span v-if="obj.level === '史诗'" style="color: #aa6ae2">{{ obj.level }}</span>
					<span v-if="obj.level === '传说'" style="color: #f9ae59">{{ obj.level }}</span>
				</template>
				<template #cover>
					<n-image object-fit="contain" width="100" height="150" :src="renderPetImg(obj)"
						style="display: flex; justify-content: center; margin-top: 20px; margin-bottom: 10px"
						preview-disabled />
				</template>
				<template #footer>
					<div style="text-align: left">
						<div style="display: flex; justify-content: space-between">
							<div>部队攻击力:</div>
							<div>{{ `+${obj.data[0]}%` }}</div>
						</div>
						<div style="display: flex; justify-content: space-between">
							<div>部队防御力:</div>
							<div>{{ `+${obj.data[1]}%` }}</div>
						</div>
						<div style="display: flex; justify-content: space-between">
							<div>盾兵穿透力:</div>
							<div>{{ `+${obj.data[2]}%` }}</div>
						</div>
						<div style="display: flex; justify-content: space-between">
							<div>盾兵生命力:</div>
							<div>{{ `+${obj.data[3]}%` }}</div>
						</div>
						<div style="display: flex; justify-content: space-between">
							<div>矛兵穿透力:</div>
							<div>{{ `+${obj.data[4]}%` }}</div>
						</div>
						<div style="display: flex; justify-content: space-between">
							<div>矛兵生命力:</div>
							<div>{{ `+${obj.data[5]}%` }}</div>
						</div>
						<div style="display: flex; justify-content: space-between">
							<div>射手穿透力:</div>
							<div>{{ `+${obj.data[6]}%` }}</div>
						</div>
						<div style="display: flex; justify-content: space-between">
							<div>射手生命力:</div>
							<div>{{ `+${obj.data[7]}%` }}</div>
						</div>
					</div>
					<n-popover trigger="hover" :overlap="false" placement="top-start" width="trigger">
						<template #trigger>
							<n-image object-fit="contain" width="50" height="50" :src="renderPetSkillImg(obj)"
								style="margin-top: 20px; display: flex; flex-direction: row" preview-disabled />
						</template>
						<template #header>
							<n-text strong depth="1">{{ obj.skill.name }}</n-text>
						</template>
						<p>{{ obj.skill.desc }}</p>
					</n-popover>
				</template>
			</n-card>
		</n-flex>
	</div>
</template>

<script setup>
import { onMounted } from "vue";
import allPets from "@/data/pets.json";

const renderPetImg = obj => {
	const imgUrl = `${import.meta.env.BASE_URL}images/pets/${obj.key}.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderPetSkillImg = obj => {
	const imgUrl = `${import.meta.env.BASE_URL}images/pets/${obj.key}_skill.png`;
	return new URL(imgUrl, import.meta.url).href;
};

onMounted(() => { });
</script>

<style scoped>
.app-main,
.app-container {
	min-height: 100%;
}

.app-main,
.app-container {
	min-height: 100%;
}

.main-content-item {
	margin-bottom: 10px;
}

.app-container {
	padding: 0 10px;
	padding-right: 0px;
}

.main-content-head {
	padding: 10px;
	margin-bottom: 10px;
	background-color: green;
}

.hero-skill-item {
	display: flex;
	height: 120px;
}

.icon-skill-item-img {
	width: 80px;
	height: 80px;
	background-size: 300%;
	background-repeat: no-repeat;
}

.icon-skill-item-img-1 {
	background-position: 0 0;
}

.icon-skill-item-img-2 {
	background-position: -84px 0;
}

.icon-skill-item-img-3 {
	background-position: -166px 0;
}
</style>
