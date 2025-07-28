<template>
	<n-flex>
		<n-card v-for="(obj, index) in allPets" :key="index" :title="obj.name" :hoverable="true" :embedded="true" size="small" header-style="text-align: center" footer-style="text-align: center" style="width: 225px; cursor: pointer">
			<template #header-extra>
				<span v-if="obj.level === '良好'" style="color: #67ee7a">{{ obj.level }}</span>
				<span v-if="obj.level === '稀有'" style="color: #70b8f1">{{ obj.level }}</span>
				<span v-if="obj.level === '史诗'" style="color: #aa6ae2">{{ obj.level }}</span>
				<span v-if="obj.level === '传说'" style="color: #f9ae59">{{ obj.level }}</span>
			</template>
			<template #cover>
				<n-image object-fit="contain" width="100" height="150" :src="renderPetImg(obj)" style="display: flex; justify-content: center; margin-top: 20px; margin-bottom: 10px" preview-disabled />
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
						<n-image object-fit="contain" width="50" height="50" :src="renderPetSkillImg(obj)" style="margin-top: 20px; display: flex; flex-direction: row" preview-disabled />
					</template>
					<template #header>
						<n-text strong depth="1">{{ obj.skill.name }}</n-text>
					</template>
					<p>{{ obj.skill.desc }}</p>
				</n-popover>
			</template>
		</n-card>
	</n-flex>
</template>

<script setup>
import { ref, onMounted } from "vue";

const allPets = [
	{ skill: { name: "城建助手", desc: "建造速度提升: 5.00%/7.00%/9.00%/12.00%/15.00%", coolingTime: "冷却时间: 23小时" }, level: "", data: ["5.02", "5.02", "3.56", "3.80", "3.82", "4.15", "3.58", "3.86"], name: "洞斑鬓狗", key: "dongBanBinGou" },
	{ skill: { name: "心灵伴侣", desc: "恢复体力: 35点/40点/45点/50点/55点/60点", coolingTime: "冷却时间: 23小时" }, level: "良好", data: ["10.06", "10.06", "3.89", "3.28", "2.85", "3.26", "3.95", "3.85"], name: "北极狼", key: "beiJiLang" },
	{ skill: { name: "重物搬运", desc: "凭借着麝牛惊人的力量和耐力，下一次抵达野外的资源点时将瞬间完成采集", coolingTime: "冷却时间: 1天11小时/1天7小时/1天3小时/23小时/19小时/15小时" }, level: "良好", data: ["10.06", "10.06", "2.11", "2.37", "2.40", "2.08", "2.27", "2.16"], name: "麝牛", key: "sheNiu" },
	{ skill: { name: "敏锐感官", desc: "宠物口粮: 200份/250份/300份/350份/400份/450份/500份", coolingTime: "冷却时间: 23小时" }, level: "稀有", data: ["0", "0", "0", "0", "0", "0", "0", "0"], name: "巨貘", key: "juMo" },
	{ skill: { name: "锋锐铁喙", desc: "使敌方部队的生命值降低: 1.50%/2.00%/2.50%/3.00%/3.50%/4.00%/5.00%", coolingTime: "冷却时间: 20小时" }, level: "稀有", data: ["0", "0", "0", "0", "0", "0", "0", "0"], name: "泰坦巨鸟", key: "taiTanJuNiao" },
	{ skill: { name: "大地馈赠", desc: "大角鹿凭借神秘的本能, 随机发现1份遗失在雪原中的珍宝", coolingTime: "冷却时间: 2天3小时/1天23小时/1天19小时/1天15小时/1天11小时/1天7小时/1天3小时/23小时" }, level: "史诗", data: ["0", "0", "0", "0", "0", "0", "0", "0"], name: "大角鹿", key: "daJiaoLu" },
	{ skill: { name: "迅猛急袭", desc: "使我军行军速度提升: 15.00%/17.00%/19.00%/21.00%/23.00%/25.00%/27.00%/30.00% \r\n 敌方部队穿透力降低: 1.50%/2.00%/2.50%/3.00%/3.50%/4.00%/4.50%/5.00%", coolingTime: "冷却时间: 20小时" }, level: "史诗", data: ["0", "0", "0", "0", "0", "0", "0", "0"], name: "雪豹", key: "xueBao" },
	{ skill: { name: "野性咆哮", desc: "使我军全体部队攻击力提升: 2.50%/3.00%/3.50%/4.00%/5.00%/6.00%/7.00%/8.00%/9.00%/10.00%", coolingTime: "冷却时间: 20小时" }, level: "传说", data: ["0", "0", "0", "0", "0", "0", "0", "0"], name: "洞狮", key: "dongShi" },
	{ skill: { name: "势如雪崩", desc: "使出征部队数量: 1500/3000/4500/6000/7500/9000/10500/12000/13500/15000", coolingTime: "冷却时间: 20小时" }, level: "传说", data: ["0", "0", "0", "0", "0", "0", "0", "0"], name: "雪猿", key: "xueYuan" },
	{ skill: { name: "兽群战术", desc: "使集结部队数量提升: 60.000/70.000/80.000/90.000/100.000/110.000/120.000/130.000/140.000/150.000", coolingTime: "冷却时间: 20小时" }, level: "传说", data: ["0", "0", "0", "0", "0", "0", "0", "0"], name: "板齿犀", key: "banChiXi" },
	{ skill: { name: "猛虎出山", desc: "使部队穿透力提升 2.50%/3%/3.50%/4%/5%/6%/7%/8%/9%/10%", coolingTime: "冷却时间: 20小时" }, level: "传说", data: ["0", "0", "0", "0", "0", "0", "0", "0"], name: "剑齿虎", key: "jianChiHu" },
	{ skill: { name: "硬化皮肤", desc: "使部队防御力提升2.50%/3.00%/3.50%/4.00%/5.00%/6.00%/7.00%/8.00%/9.00%/10.00%", coolingTime: "冷却时间: 20小时" }, level: "传说", data: ["0", "0", "0", "0", "0", "0", "0", "0"], name: "猛犸象", key: "mengMaXiang" },
	{ skill: { name: "亘古不灭", desc: "使部队生命力提升2.50%/3.00%/3.50%/4.00%/5.00%/6.00%/7.00%/8.00%/9.00%/10.00%", coolingTime: "冷却时间: 20小时" }, level: "传说", data: ["0", "0", "0", "0", "0", "0", "0", "0"], name: "冰霜古猿", key: "bingShuangGuYuan" },
];

const renderPetImg = obj => {
	const imgUrl = `/images/pets/${obj.key}.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderPetSkillImg = obj => {
	const imgUrl = `/images/pets/${obj.key}_skill.png`;
	return new URL(imgUrl, import.meta.url).href;
};

onMounted(() => {});
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
