<template>
	<n-layout>
		<n-layout-header style="padding: 10px 0;">
			<n-select v-model:value="selectValue" :options="selectOptions" @update:value="handleUpdateValue" />
		</n-layout-header>
		<n-layout-content :native-scrollbar="false">
			<n-grid x-gap="10" y-gap="10" cols="2 s:3 m:5 xl:12" responsive="screen">
				<n-gi v-for="(obj, index) in showHeros" :key="index">
					<n-card  :title="renderCardTitle(obj)" :hoverable="true" :embedded="true" size="small" class="hero-card-main" @click="clictItem(obj)">
						<template #cover>
							<n-image object-fit="contain" :src="renderAvatar(obj)" class="hero-avatar-image" preview-disabled />
						</template>
						<template #footer>
							<img v-if="obj.as === 1" src="/images/as-hypaspist.png" style="width: 30px" />
							<img v-else-if="obj.as === 2" src="/images/as-spearman.png" style="width: 30px" />
							<img v-else="obj.as === 3" src="/images/as-archers.png" style="width: 30px" />
							<img v-if="obj.type === 1" src="/images/type-output.png" style="width: 30px" />
							<img v-else="obj.type === 1" src="/images/type-develop.png" style="width: 30px" />
						</template>
					</n-card>
				</n-gi>
			</n-grid>
		</n-layout-content>
	</n-layout>
</template>

<script setup>
import { ref, h, onMounted } from "vue";
import { useRouter } from 'vue-router'

import allHeroDatum from "@/data/heros.json";

const router = useRouter()

const selectValue = ref("0");
const selectOptions = ref([
	{ label: '全部', value: '0', type: '0'},
	{ label: '盾兵', value: '1', type: '0'},
	{ label: '矛兵', value: '2', type: '0'},
	{ label: '弓兵', value: '3', type: '0'},
	{ label: '稀有', value: 'rare', type: '1'},
	{ label: '史诗', value: 'epic', type: '1'},
]);

const showHeros = ref();

const renderCardTitle = obj => {
	const levelDesc = obj.level === "rare" ? "稀有" : obj.level === "epic" ? "史诗" : obj.level;
	const colorStyle = obj.level === "rare" ? 
		{ textColor: '#4d99b9', borderColor: '#4d99b9' } : 
		obj.level === 'epic' ?  { textColor: '#db8efe', borderColor: '#db8efe' }:
		{ textColor: '#f7cb50', borderColor: '#f7cb50' }

	return h("div", {
		display: 'flex',
		alignItems: 'center',
		justifyContent: 'center'	
	}, [
		h("div", { style: { paddingRight: "5px" }, class: "n-tag_hero_card_name" }, obj.name), 
		h(NTag, { color: colorStyle, size: 'small', class: "n-tag_hero_card_level" }, levelDesc)
	]);
};

const renderAvatar = obj => {
	const imgUrl = `${import.meta.env.BASE_URL}images/heros/${obj.addr}/avatar.png`;
	return new URL(imgUrl, import.meta.url).href;
};

function handleUpdateValue(value, option) {
  console.log(`value: ${JSON.stringify(value)}`)
  console.log(`option: ${JSON.stringify(option)}`)
	if(option.type === '0') {
		if(value === '0') {
			showHeros.value = allHeroDatum;
		} else {
			showHeros.value = allHeroDatum.filter(item => String(item.as) === value);
		}
	} else {
		showHeros.value = allHeroDatum.filter(item => item.level === value);
	}
}

const clictItem = obj => {
	router.push({ name: 'HeroDetail', params: { id: obj.id } });
};

onMounted(() => {
	showHeros.value = allHeroDatum.sort((a, b) => b.id - a.id);

	const showAllLevel = [...new Set(allHeroDatum.map(hero => hero.level))];
	console.log(showAllLevel)
	showAllLevel.forEach((item, index) => {
		if(item !== 'rare' && item !== "epic") {
			selectOptions.value.push({ label: item, value: item, type: '1' });
		}
	})
});

</script>

<style scoped>
.hero-card-main {
	width: calc(50vw - 30px); 
	cursor: pointer;
}

.hero-avatar-image {
	display: flex; 
	justify-content: center;
	width: 80px;
	height: 80px;
	margin: auto;
	margin-top: 20px;
	margin-bottom: 10px;
}

:deep(.n-card-header__main) {
	display: flex;
	align-items: center;
	justify-content: center;
}

:deep(.n-card-header__main > div) {
	display: flex;
	align-items: center;
}

:deep(.n-card__footer) {
	text-align: center;
}

@media (min-width: 640px) { 
	.hero-card-main {
		width: calc(33vw - 30px); 
		cursor: pointer;
	}
}

@media (min-width: 1024px) {
  	.hero-card-main {
		width: calc(20vw - 30px); 
		cursor: pointer;
	}
}

@media (min-width: 2048px) {
  	.hero-card-main {
		width: calc(8.3vw - 30px); 
		cursor: pointer;
	}

	.hero-avatar-image {
		width: 120px;
		height: 120px;
	}
}
</style>
