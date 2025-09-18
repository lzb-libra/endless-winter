<template>
	<n-grid x-gap="10" y-gap="10" cols="1 m:2 xl:4" responsive="screen">
		<n-gi v-for="(obj, index) in showAllPets" :key="index">
			<n-card :hoverable="true" :embedded="true" size="small" class="pet_card_main">
				<div class="pet_card_base_info" style="">
					<n-image object-fit="contain" width="100" height="150" :src="renderPetImg(obj)" class="pet_card_img" preview-disabled />
					<div style="flex: 1; padding-left: 15px;">
						<div style="display: flex; align-items: center; justify-content: space-between;">
							<div style="font-size: 1.5em; padding-right: 10px;">{{ obj.name }}</div>
							<div style="display: flex;">
								<div>
									<n-tag size="small" v-if="obj.rarity === '良好'" style="color: #67ee7a">{{ obj.rarity }}</n-tag>
									<n-tag size="small" v-if="obj.rarity === '稀有'" style="color: #70b8f1">{{ obj.rarity }}</n-tag>
									<n-tag size="small" v-if="obj.rarity === '史诗'" style="color: #aa6ae2">{{ obj.rarity }}</n-tag>
									<n-tag size="small" v-if="obj.rarity === '传说'" style="color: #f9ae59">{{ obj.rarity }}</n-tag>
								</div>
								<div style="padding-left: 10px; flex: 1;">
									<n-tag size="small" type="info">{{ obj.level }}</n-tag>
								</div>
							</div>
						</div>
						<div style="display: flex;">
							<div style="font-size: 0.8em; width: 120px;">
								<div>部队攻击力:{{ `+${obj.data[0]}%` }}</div>
								<div>部队防御力:{{ `+${obj.data[1]}%` }}</div>
								<div>盾兵穿透力:{{ `+${obj.data[2]}%` }}</div>
								<div>盾兵生命力:{{ `+${obj.data[3]}%` }}</div>
								<div>矛兵穿透力:{{ `+${obj.data[4]}%` }}</div>
								<div>矛兵生命力:{{ `+${obj.data[5]}%` }}</div>
								<div>射手穿透力:{{ `+${obj.data[6]}%` }}</div>
								<div>射手生命力:{{ `+${obj.data[7]}%` }}</div>
							</div>
							<div class="pet_card_skill" style="flex: 1; font-size: 0.8em;">
								<n-image object-fit="contain" width="50" height="50" :src="renderPetSkillImg(obj)" preview-disabled />
								<div>
									<div style="font-size: 1.25em;">{{ obj.skill.name }}</div>
									<div>{{ obj.skill.desc }}</div>
									<div style="padding-top: 3px;">{{ obj.skill.coolingTime }}</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="pet_card_skill_mobile">
					<n-image object-fit="contain" width="60" height="60" :src="renderPetSkillImg(obj)" preview-disabled />
					<div style="padding-left: 5px; flex: 1;">
						<div style="font-size: 1.25em;">{{ obj.skill.name }}</div>
						<div>{{ obj.skill.desc }}</div>
						<div style="padding-top: 3px;">{{ obj.skill.coolingTime }}</div>
					</div>
				</div>
			</n-card>
		</n-gi>
	</n-grid>
</template>

<script setup>
import { onMounted, ref } from "vue";
import allPets from "@/data/pets.json";

const showAllPets = ref()

const renderPetImg = obj => {
	const imgUrl = `${import.meta.env.BASE_URL}images/pets/${obj.key}.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderPetSkillImg = obj => {
	const imgUrl = `${import.meta.env.BASE_URL}images/pets/${obj.key}_skill.png`;
	return new URL(imgUrl, import.meta.url).href;
};

onMounted(() => { 
	showAllPets.value = allPets.sort((a, b) => b.id - a.id);
});
</script>

<style scoped>
.pet_card_main {
	width: 100%;
	height: 295px;
}

.pet_card_img {
	display: flex; 
	justify-content: center;
	align-items: center;
}

.pet_card_skill {
	display: none;
}

.pet_card_base_info {
	display: flex;
}

.pet_card_skill_mobile {
	display: flex;
	padding-top: 10px;
	font-size: 0.8em; 
	width: 100%;
}

@media (min-width: 640px) {
	.pet_card_main {
		width: 100%;
		height: 202px;
	}

	.pet_card_skill {
		flex: 1; 
		display: block;
		font-size: 0.8em;
	}

	.pet_card_base_info {
		height: 100%;
	}

	.pet_card_skill_mobile {
		display: none;
	}
}

/* 中等屏幕（平板等） */
@media (min-width: 1024px) {
	.pet_card_main {
		width: calc(25vw - 75px);
		height: 205px;
	}

	.pet_card_skill {
		flex: 1; 
		display: block;
		font-size: 0.8em;
	}

	.pet_card_base_info {
		height: 100%;
	}

	.pet_card_skill_mobile {
		display: none;
	}
}

/* 大屏幕（桌面等） */
@media (min-width: 2048) {
	.pet_card_main {
		width: calc(25vw - 75px);
		height: 205px;
	}

	.pet_card_skill {
		flex: 1; 
		display: block;
		font-size: 0.8em;
	}

	.pet_card_base_info {
		height: 100%;
	}

	.pet_card_skill_mobile {
		display: none;
	}
}
</style>
