<template>
	<div style="padding: 0 15px">
		<n-flex>
			<n-card v-for="(obj, index) in allHeroDatum" :key="index" :title="renderCardTitle(obj)" :hoverable="true"
				:embedded="true" size="small" header-style="text-align: center" footer-style="text-align: center"
				style="width: 169px; cursor: pointer" @click="clictItem(obj)">
				<template #cover>
					<n-image object-fit="contain" :width="120" :height="120" :src="renderAvatar(obj)"
						style="display: flex; justify-content: center; margin-top: 20px; margin-bottom: 10px"
						preview-disabled />
				</template>
				<template #footer>
					<img v-if="obj.as === 1" src="/images/as-hypaspist.png" style="width: 30px" />
					<img v-else-if="obj.as === 2" src="/images/as-spearman.png" style="width: 30px" />
					<img v-else="obj.as === 3" src="/images/as-archers.png" style="width: 30px" />
					<img v-if="obj.type === 1" src="/images/type-output.png" style="width: 30px" />
					<img v-else="obj.type === 1" src="/images/type-develop.png" style="width: 30px" />
				</template>
			</n-card>
		</n-flex>
	</div>

	<n-modal v-model:show="showModal" transform-origin="center" @after-leave="onAfterLeave"
		style="width: 1650px; height: 100vh;">
		<div style="display: flex;">
			<n-card style="width: 600px; padding-top: 30px;">
				<div style="display: flex; flex-direction: column; align-items: center">
					<!-- 立绘 -->
					<n-badge
						:value="showModalInfo.level === 'rare' ? '稀有' : showModalInfo.level === 'epic' ? '传说' : showModalInfo.level">
						<n-image object-fit="contain" :height="300" :show-toolbar="false" :preview-disabled="true"
							:src="renderPortrait(showModalInfo)"
							style="display: flex; justify-content: center; margin-top: 20px; margin-bottom: 10px" />
					</n-badge>
					<div style="display: flex; align-items: center;">
						<!-- 名称 -->
						<h2>{{ showModalInfo.name }}</h2>
						<!-- 兵种、类型、天赋 -->
						<div style="display: flex; align-items: center; margin-left: 5px;">
							<img v-if="showModalInfo.as === 1" src="/images/as-hypaspist.png" style="width: 30px" />
							<img v-else-if="showModalInfo.as === 2" src="/images/as-spearman.png" style="width: 30px" />
							<img v-else="showModalInfo.as === 3" src="/images/as-archers.png" style="width: 30px" />
							<img v-if="showModalInfo.type == 1" src="/images/type-output.png" style="width: 30px" />
							<img v-else="showModalInfo.type == 1" src="/images/type-develop.png" style="width: 30px" />
							<div v-if="showModalInfo.talent" style="padding-top: 7px">
								<n-popover trigger="hover">
									<template #trigger>
										<img :src="renderTalent()" style="width: 30px; cursor: pointer" />
									</template>
									<span>
										<p style="font-weight: bold; font-size: 1.25em">{{ showModalInfo.talent.name }}
										</p>
										<p>{{ showModalInfo.talent.desc }}</p>
									</span>
								</n-popover>
							</div>
						</div>
					</div>
				</div>
				<div style="padding-top: 20px;" v-html="showModalInfo.story"></div>
			</n-card>
			<n-card style="width: 1000px; flex: 1;" :bordered="false" size="huge" role="dialog" aria-modal="true">
				<!-- 英雄来源 -->
				<div style="display: flex; justify-content: space-between;">
					<div v-if="showModalInfo.source" style="flex: 1; padding-right: 20px;">
						<h3>英雄来源</h3>
						<div>
							<n-space>
								<n-tag v-for="(item, index) in showModalInfo.source" type="success">{{ item }}</n-tag>
							</n-space>
						</div>
					</div>
					<video v-if="showModalInfo.hasVideo" style="height: 250px; width: 500px;" :src="renderVideo()"
						controls></video>
				</div>

				<!-- 英雄技能 -->
				<div v-show="showModalInfo.skill">
					<n-divider />

					<h3>英雄技能</h3>
					<di style="display: flex">
						<n-card title="探险" size="small" :bordered="false">
							<div style="height: 80px">
								<div>英雄攻击: {{ showModalInfo.skill.data[0] || 0 }}</div>
								<div>英雄防御: {{ showModalInfo.skill.data[1] || 0 }}</div>
								<div>英雄生命: {{ showModalInfo.skill.data[2] || 0 }}</div>
							</div>
							<div class="hero-skill-item" v-if="showModalInfo.skill.tx_1">
								<div :class="renderSkillClass(1, 1)"
									:style="{ backgroundImage: `url(${renderTxImg()})` }">
								</div>
								<div style="flex: 1; padding-left: 20px">
									<div style="font-size: 1.25em; font-weight: bold">{{ showModalInfo.skill.tx_1.label
									}}
									</div>
									<div>{{ showModalInfo.skill.tx_1.desc }}</div>
								</div>
							</div>
							<div class="hero-skill-item" v-if="showModalInfo.skill.tx_2">
								<div :class="renderSkillClass(2, 1)"
									:style="{ backgroundImage: `url(${renderTxImg()})` }">
								</div>
								<div style="flex: 1; padding-left: 20px">
									<div style="font-size: 1.25em; font-weight: bold">{{ showModalInfo.skill.tx_2.label
									}}
									</div>
									<div>{{ showModalInfo.skill.tx_2.desc }}</div>
								</div>
							</div>
							<div class="hero-skill-item" v-if="showModalInfo.skill.tx_3">
								<div :class="renderSkillClass(3, 1)"
									:style="{ backgroundImage: `url(${renderTxImg()})` }">
								</div>
								<div style="flex: 1; padding-left: 20px">
									<div style="font-size: 1.25em; font-weight: bold">{{ showModalInfo.skill.tx_3.label
									}}
									</div>
									<div>{{ showModalInfo.skill.tx_3.desc }}</div>
								</div>
							</div>
						</n-card>
						<n-card title="远征" size="small" :bordered="false">
							<div style="height: 80px">
								<div>
									{{
										`${showModalInfo.as === 1 ? "盾" : showModalInfo.as === 2 ? "矛" : "弓"}兵攻击力:
									+${showModalInfo.skill.data[3] || 0}%`
									}}
								</div>
								<div>
									{{
										`${showModalInfo.as === 1 ? "盾" : showModalInfo.as === 2 ? "矛" : "弓"}兵防御力:
									+${showModalInfo.skill.data[4] || 0}%`
									}}
								</div>
							</div>
							<div class="hero-skill-item" v-if="showModalInfo.skill.yz_1">
								<div :class="renderSkillClass(1, 2)"
									:style="{ backgroundImage: `url(${renderYzImg()})` }">
								</div>
								<div style="flex: 1; padding-left: 20px">
									<div style="font-size: 1.25em; font-weight: bold">{{ showModalInfo.skill.yz_1.label
									}}
									</div>
									<div>{{ showModalInfo.skill.yz_1.desc }}</div>
								</div>
							</div>
							<div class="hero-skill-item" v-if="showModalInfo.skill.yz_2">
								<div :class="renderSkillClass(2, 2)"
									:style="{ backgroundImage: `url(${renderYzImg()})` }">
								</div>
								<div style="flex: 1; padding-left: 20px">
									<div style="font-size: 1.25em; font-weight: bold">{{ showModalInfo.skill.yz_2.label
									}}
									</div>
									<div>{{ showModalInfo.skill.yz_2.desc }}</div>
								</div>
							</div>
							<div class="hero-skill-item" v-if="showModalInfo.skill.yz_3">
								<div :class="renderSkillClass(3, 2)"
									:style="{ backgroundImage: `url(${renderYzImg()})` }">
								</div>
								<div style="flex: 1; padding-left: 20px">
									<div style="font-size: 1.25em; font-weight: bold">{{ showModalInfo.skill.yz_3.label
									}}
									</div>
									<div>{{ showModalInfo.skill.yz_3.desc }}</div>
								</div>
							</div>
						</n-card>
					</di>
				</div>

				<!-- 专属装备 -->
				<div v-if="showModalInfo.weapon">
					<n-divider />

					<h3>专属装备</h3>
					<div style="display: flex">
						<div>
							<n-image object-fit="contain" width="100" height="100" :src="renderZwImg()"
								preview-disabled />
							<div style="text-align: center; font-weight: bold; padding-top: 3px;">{{
								showModalInfo.weapon.name }}</div>
							<div v-if="showModalInfo.weapon.strength"
								style="display: flex; align-items: center; justify-content: center; padding-top: 3px;">
								<n-image object-fit="contain" width="15" height="15" src="/endless-winter/images/strength.png"
									preview-disabled />
								<span style="padding-left: 3px;">{{ showModalInfo.weapon.strength }}</span>
							</div>
						</div>
						<div style="padding-left: 20px; width: 300px">
							<div>英雄攻击: {{ showModalInfo.weapon.data[0] }}</div>
							<div>英雄防御: {{ showModalInfo.weapon.data[1] }}</div>
							<div>英雄生命: {{ showModalInfo.weapon.data[2] }}</div>
							<div>护卫攻击: {{ showModalInfo.weapon.data[3] }}</div>
							<div>护卫防御: {{ showModalInfo.weapon.data[4] }}</div>
							<div>护卫生命: {{ showModalInfo.weapon.data[5] }}</div>
							<div>{{ showModalInfo.as === 1 ? "盾兵" : showModalInfo.as === 2 ? "矛兵" : "射手" }}杀伤力: +{{
								showModalInfo.weapon.data[6] }}%</div>
							<div>{{ showModalInfo.as === 1 ? "盾兵" : showModalInfo.as === 2 ? "矛兵" : "射手" }}生命值: +{{
								showModalInfo.weapon.data[7] }}%</div>
						</div>
						<div style="padding-left: 40px; display: flex; flex-direction: column; justify-content: space-between">
							<div style="display: flex">
								<div>
									<n-image object-fit="contain" width="80" height="80" :src="renderZwTxImg()"
										preview-disabled />
									<div style="text-align: center">探险</div>
								</div>
								<div style="padding-left: 20px">
									<div style="font-weight: bold">{{ showModalInfo.weapon.tx.name }}</div>
									<div>{{ showModalInfo.weapon.tx.desc }}</div>
								</div>
							</div>
							<div style="display: flex; margin-top: 20px;">
								<div>
									<n-image object-fit="contain" width="80" height="80" :src="renderZwYzImg()"
										preview-disabled />
									<div style="text-align: center">远征</div>
								</div>
								<div style="padding-left: 20px">
									<div style="font-weight: bold">{{ showModalInfo.weapon.yz.name }}</div>
									<div>{{ showModalInfo.weapon.yz.desc }}</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</n-card>
		</div>
	</n-modal>
</template>

<script setup>
import { ref, h, onMounted } from "vue";
import allHeroDatum from "../data/heros.json";

const showModal = ref(false);
const showModalInfo = ref({});

const renderCardTitle = obj => {
	return h("div", {}, [h("span", { style: { paddingRight: "5px" } }, obj.name), h(NTag, { type: "success" }, obj.level === "rare" ? "稀有" : obj.level === "epic" ? "史诗" : obj.level)]);
};

const renderSkillClass = (index, type) => {
	let myClass = "";
	if (showModalInfo.value.level === "rare") {
		myClass += "icon-skill-item-double-skill-img";
	} else if (showModalInfo.value.level == "epic") {
		if (type === 2) myClass += "icon-skill-item-double-skill-img";
		else myClass += "icon-skill-item-img";
	} else {
		myClass += "icon-skill-item-img";
	}

	myClass += " icon-skill-item-img-" + index;
	console.log(myClass);

	return myClass;
};

const renderVideo = () => {
	const imgUrl = `${import.meta.env.BASE_URL}videos/heros/${showModalInfo.value.addr}/cg.mp4`;
	return new URL(imgUrl, import.meta.url).href;
}

const renderAvatar = obj => {
	const imgUrl = `${import.meta.env.BASE_URL}images/heros/${obj.addr}/avatar.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderPortrait = obj => {
	const imgUrl = `${import.meta.env.BASE_URL}images/heros/${obj.addr}/portrait.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderTalent = () => {
	const imgUrl = `${import.meta.env.BASE_URL}images/heros/${showModalInfo.value.addr}/tf.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderTxImg = () => {
	const imgUrl = `${import.meta.env.BASE_URL}images/heros/${showModalInfo.value.addr}/tx.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderYzImg = () => {
	const imgUrl = `${import.meta.env.BASE_URL}images/heros/${showModalInfo.value.addr}/yz.png`;
	console.log("renderYzImg: " + imgUrl);
	return new URL(imgUrl, import.meta.url).href;
};

const renderZwImg = () => {
	const imgUrl = `${import.meta.env.BASE_URL}images/heros/${showModalInfo.value.addr}/zw.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderZwTxImg = () => {
	const imgUrl = `${import.meta.env.BASE_URL}images/heros/${showModalInfo.value.addr}/zw-tx.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderZwYzImg = () => {
	const imgUrl = `${import.meta.env.BASE_URL}images/heros/${showModalInfo.value.addr}/zw-yz.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const clictItem = obj => {
	console.log(obj);
	showModal.value = true;
	showModalInfo.value = obj;
};

const onAfterLeave = () => {
	showModalInfo.value = {};
};

onMounted(() => {

})
</script>

<style scoped>
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

.icon-skill-item-double-skill-img {
	width: 80px;
	height: 80px;
	background-size: 190%;
	background-repeat: no-repeat;
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
