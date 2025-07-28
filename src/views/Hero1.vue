<template>
	<n-layout class="app-main">
		<n-layout has-sider>
			<n-layout-sider>
				<n-menu v-model:value="activeKey" mode="vertical" :options="menuOptions" @update:value="handleUpdateValue" responsive />
			</n-layout-sider>
			<n-layout class="app-container">
				<n-layout-content class="main-content">
					<n-flex>
						<n-card v-for="(obj, index) in showHeros" :key="index" :title="obj.name" :hoverable="true" :embedded="true" size="small" header-style="text-align: center" footer-style="text-align: center" style="width: 159px; cursor: pointer" @click="clictItem(obj)">
							<template #cover>
								<n-image object-fit="contain" :width="100" :height="100" :src="renderAvatar(obj)" style="display: flex; justify-content: center; margin-top: 20px; margin-bottom: 10px" preview-disabled />
							</template>
							<template #footer>
								<img v-if="obj.as === 1" src="/images/as-hypaspist.png" style="width: 30px" />
								<img v-else-if="obj.as === 2" src="/images/as-spearman.png" style="width: 30px" />
								<img v-else="obj.as === 3" src="/images/as-archers.png" style="width: 30px" />
								<img v-if="obj.type == 1" src="/images/type-output.png" style="width: 30px" />
								<img v-else="obj.type == 1" src="/images/type-develop.png" style="width: 30px" />
							</template>
						</n-card>
					</n-flex>
				</n-layout-content>
			</n-layout>
		</n-layout>
	</n-layout>

	<n-modal v-model:show="showModal" transform-origin="center" @after-leave="onAfterLeave">
		<n-card style="width: 1000px" :bordered="false" size="huge" role="dialog" aria-modal="true">
			<div style="display: flex">
				<div style="width: 30%; margin-right: 20px">
					<n-image object-fit="contain" :height="showModalInfo.height" :src="renderPortrait(showModalInfo, activeKey)" style="display: flex; justify-content: center; margin-top: 20px; margin-bottom: 10px" preview-disabled />
				</div>
				<div>
					<div style="display: flex; align-items: center">
						<h2 style="padding-right: 10px">{{ showModalInfo.name }}</h2>
						<n-badge :value="showModalInfo.level === 'rare' ? '稀有' : showModalInfo.level === 'epic' ? '传说' : showModalInfo.level" />
					</div>
					<div style="display: flex; align-items: center; padding-bottom: 20px">
						<img v-if="showModalInfo.as === 1" src="/images/as-hypaspist.png" style="width: 30px" />
						<img v-else-if="showModalInfo.as === 2" src="/images/as-spearman.png" style="width: 30px" />
						<img v-else="showModalInfo.as === 3" src="/images/as-archers.png" style="width: 30px" />
						<img v-if="showModalInfo.type == 1" src="/images/type-output.png" style="width: 30px" />
						<img v-else="showModalInfo.type == 1" src="/images/type-develop.png" style="width: 30px" />
						<div v-if="showModalInfo.talent" style="padding-top: 2px">
							<n-popover trigger="hover">
								<template #trigger>
									<img :src="renderTalent()" style="width: 30px; cursor: pointer" />
								</template>
								<span>
									<p style="font-weight: bold; font-size: 1.25em">{{ showModalInfo.talent.name }}</p>
									<p>{{ showModalInfo.talent.desc }}</p>
								</span>
							</n-popover>
						</div>
					</div>
					<div v-if="showModalInfo.source" style="display: flex; flex: 1">
						<div style="margin-right: 10px; width: 100px">
							<strong>英雄来源: </strong>
						</div>
						<div>
							<n-space>
								<n-tag v-for="(item, index) in showModalInfo.source" type="success">{{ item }}</n-tag>
							</n-space>
						</div>
					</div>
				</div>
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
							<div :class="renderSkillClass(1, 1)" :style="{ backgroundImage: `url(${renderTxImg()})` }"></div>
							<div style="flex: 1; padding-left: 10px">
								<div style="font-size: 1.25em; font-weight: bold">{{ showModalInfo.skill.tx_1.label }}</div>
								<div>{{ showModalInfo.skill.tx_1.desc }}</div>
							</div>
						</div>
						<div class="hero-skill-item" v-if="showModalInfo.skill.tx_2">
							<div :class="renderSkillClass(2, 1)" :style="{ backgroundImage: `url(${renderTxImg()})` }"></div>
							<div style="flex: 1; padding-left: 10px">
								<div style="font-size: 1.25em; font-weight: bold">{{ showModalInfo.skill.tx_2.label }}</div>
								<div>{{ showModalInfo.skill.tx_2.desc }}</div>
							</div>
						</div>
						<div class="hero-skill-item" v-if="showModalInfo.skill.tx_3">
							<div :class="renderSkillClass(3, 1)" :style="{ backgroundImage: `url(${renderTxImg()})` }"></div>
							<div style="flex: 1; padding-left: 10px">
								<div style="font-size: 1.25em; font-weight: bold">{{ showModalInfo.skill.tx_3.label }}</div>
								<div>{{ showModalInfo.skill.tx_3.desc }}</div>
							</div>
						</div>
					</n-card>
					<n-card title="远征" size="small" :bordered="false">
						<div style="height: 80px">
							<div>{{ `${showModalInfo.as === 1 ? "盾" : showModalInfo.as === 2 ? "矛" : "弓"}兵攻击力: +${showModalInfo.skill.data[3] || 0}%` }}</div>
							<div>{{ `${showModalInfo.as === 1 ? "盾" : showModalInfo.as === 2 ? "矛" : "弓"}兵防御力: +${showModalInfo.skill.data[4] || 0}%` }}</div>
						</div>
						<div class="hero-skill-item" v-if="showModalInfo.skill.yz_1">
							<div :class="renderSkillClass(1, 2)" :style="{ backgroundImage: `url(${renderYzImg()})` }"></div>
							<div style="flex: 1; padding-left: 10px">
								<div style="font-size: 1.25em; font-weight: bold">{{ showModalInfo.skill.yz_1.label }}</div>
								<div>{{ showModalInfo.skill.yz_1.desc }}</div>
							</div>
						</div>
						<div class="hero-skill-item" v-if="showModalInfo.skill.yz_2">
							<div :class="renderSkillClass(2, 2)" :style="{ backgroundImage: `url(${renderYzImg()})` }"></div>
							<div style="flex: 1; padding-left: 10px">
								<div style="font-size: 1.25em; font-weight: bold">{{ showModalInfo.skill.yz_2.label }}</div>
								<div>{{ showModalInfo.skill.yz_2.desc }}</div>
							</div>
						</div>
						<div class="hero-skill-item" v-if="showModalInfo.skill.yz_3">
							<div :class="renderSkillClass(3, 2)" :style="{ backgroundImage: `url(${renderYzImg()})` }"></div>
							<div style="flex: 1; padding-left: 10px">
								<div style="font-size: 1.25em; font-weight: bold">{{ showModalInfo.skill.yz_3.label }}</div>
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
						<n-image object-fit="contain" width="100" height="100" :src="renderZwImg()" preview-disabled />
						<div style="text-align: center; font-weight: bold">{{ showModalInfo.weapon.name }}</div>
					</div>
					<div style="padding-left: 20px; width: 300px">
						<div>英雄攻击: {{ showModalInfo.weapon.data[0] }}</div>
						<div>英雄防御: {{ showModalInfo.weapon.data[1] }}</div>
						<div>英雄生命: {{ showModalInfo.weapon.data[2] }}</div>
						<div>护卫攻击: {{ showModalInfo.weapon.data[3] }}</div>
						<div>护卫防御: {{ showModalInfo.weapon.data[4] }}</div>
						<div>护卫生命: {{ showModalInfo.weapon.data[5] }}</div>
						<div>{{ showModalInfo.as === 1 ? "盾兵" : showModalInfo.as === 2 ? "矛兵" : "射手" }}杀伤力: +{{ showModalInfo.weapon.data[6] }}%</div>
						<div>{{ showModalInfo.as === 1 ? "盾兵" : showModalInfo.as === 2 ? "矛兵" : "射手" }}生命值: +{{ showModalInfo.weapon.data[7] }}%</div>
					</div>
					<div style="padding-left: 40px; display: flex; flex-direction: column; justify-content: space-between">
						<div style="display: flex">
							<div>
								<n-image object-fit="contain" width="50" height="50" :src="renderZwTxImg()" preview-disabled />
								<div style="text-align: center">探险</div>
							</div>
							<div style="padding-left: 10px">
								<div style="font-weight: bold">{{ showModalInfo.weapon.tx.name }}</div>
								<div>{{ showModalInfo.weapon.tx.desc }}</div>
							</div>
						</div>
						<div style="display: flex">
							<div>
								<n-image object-fit="contain" width="50" height="50" :src="renderZwYzImg()" preview-disabled />
								<div style="text-align: center">远征</div>
							</div>
							<div style="padding-left: 10px">
								<div style="font-weight: bold">{{ showModalInfo.weapon.yz.name }}</div>
								<div>{{ showModalInfo.weapon.yz.desc }}</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</n-card>
	</n-modal>
</template>

<script setup>
import { ref, onMounted, onBeforeMount } from "vue";

const activeKey = ref("S1");
const showModal = ref(false);
const showHeros = ref({});
const showModalInfo = ref({});

const menuOptions = [
	{ label: "稀有", key: "rare" },
	{ label: "史诗", key: "epic" },
	{ label: "S1", key: "S1" },
	{ label: "S2", key: "S2" },
	{ label: "S3", key: "S3" },
	{ label: "S4", key: "S4" },
	{ label: "S5", key: "S5" },
	{ label: "S6", key: "S6" },
	{ label: "S7", key: "S7" },
	{ label: "S8", key: "S8" },
	{ label: "S9", key: "S9" },
	{ label: "S10", key: "S10" },
	{ label: "S11", key: "S11" },
	{ label: "S12", key: "S12" },
	{ label: "S13", key: "S13" },
];

// rare=稀有、epic=史诗、lore=传说
const allHeroDatum = [
	{
		level: "rare",
		name: "史密斯",
		addr: "rare/ShiMiSi",
		width: "200",
		height: "250",
		as: 1,
		type: 2,
		story: [],
		source: ["英雄招募", "灯塔情报", "探险战斗", "通用碎片兑换"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
		},
	},
	{
		level: "rare",
		name: "尤金",
		addr: "rare/YouJin",
		width: "200",
		height: "250",
		as: 1,
		type: 3,
		story: [],
		source: ["英雄招募", "灯塔情报", "探险战斗", "通用碎片兑换"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
		},
	},
	{
		level: "rare",
		name: "查理",
		addr: "rare/ChaLi",
		width: "200",
		height: "250",
		as: 2,
		type: 3,
		story: [],
		source: ["英雄招募", "灯塔情报", "探险战斗", "通用碎片兑换"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
		},
	},
	{
		level: "rare",
		name: "克劳瑞斯",
		addr: "rare/KeLaoRuiSi",
		width: "200",
		height: "250",
		as: 3,
		type: 2,
		story: [],
		source: ["英雄招募", "灯塔情报", "探险战斗", "通用碎片兑换"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
		},
	},
	{
		level: "epic",
		name: "谢尔盖",
		addr: "epic/XieErGai",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: ["英雄招募", "灯塔情报", "探险战斗", "通用碎片兑换"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
		},
	},
	{
		level: "epic",
		name: "帕特里克",
		addr: "epic/PaTeLiKe",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: ["", "", "", "", ""],
		source: ["英雄招募", "灯塔情报", "通用碎片兑换"],
		skill: {
			data: [],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
		},
	},
	{
		level: "epic",
		name: "凌雪",
		addr: "epic/LingXue",
		width: "200",
		height: "250",
		as: 2,
		type: 2,
		story: [],
		source: ["英雄招募", "通用碎片兑换"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
		},
	},
	{
		level: "epic",
		name: "卢姆·波根",
		addr: "epic/LuMuBoGen",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: ["英雄招募", "通用碎片兑换"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
		},
	},
	{
		level: "epic",
		name: "杰西",
		addr: "epic/JieXi",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: ["英雄招募", "灯塔情报", "生存者试炼", "通用碎片兑换"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
		},
	},
	{
		level: "epic",
		name: "巴希提",
		addr: "epic/BaXiTi",
		width: "200",
		height: "250",
		as: 3,
		type: 1,
		story: [],
		source: ["完成任务", "英雄招募", "灯塔情报", "通用碎片兑换"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
		},
	},
	{
		level: "epic",
		name: "杰塞尔",
		addr: "epic/JieSaiEr",
		width: "200",
		height: "250",
		as: 3,
		type: 2,
		story: [],
		source: ["英雄招募", "通用碎片兑换"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
		},
	},
	{
		level: "epic",
		name: "吉娜",
		addr: "epic/JiNa",
		width: "200",
		height: "250",
		as: 3,
		type: 1,
		story: [],
		source: ["吉娜的复仇", "通用碎片兑换"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
		},
	},
	{
		level: "epic",
		name: "书允",
		addr: "epic/ShuYun",
		width: "200",
		height: "250",
		as: 3,
		type: 2,
		story: [],
		source: ["英雄招募", "通用碎片兑换"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
		},
	},
	{
		level: "S1",
		name: "赫罗尼莫",
		addr: "lore/S1/HeLuoNiMo",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: ["统帅礼包购买"],
		talent: {
			name: "天生领袖",
			desc: "以领袖气质感染全军，无论赫罗尼莫是否出征，都可以使我军全体部队穿透力和生命值提升15%。",
		},
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", ""],
			tx: {
				name: "",
				desc: "",
			},
			yz: {
				name: "",
				desc: "",
			},
		},
	},
	{
		level: "S1",
		name: "娜塔莉娅",
		addr: "lore/S1/NaTaLiYa",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: [],
		talent: {
			name: "白熊之力",
			desc: "赋予全军白熊般的勇气和力量。无论娜塔莉亚是否出征，均可使我军全体部队攻击力和防御力提升10%。",
		},
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", ""],
			tx: {
				name: "",
				desc: "",
			},
			yz: {
				name: "",
				desc: "",
			},
		},
	},
	{
		level: "S1",
		name: "茉莉",
		addr: "lore/S1/MoLi",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", ""],
			tx: {
				name: "",
				desc: "",
			},
			yz: {
				name: "",
				desc: "",
			},
		},
	},
	{
		level: "S1",
		name: "津曼",
		addr: "lore/S1/JingMan",
		width: "200",
		height: "250",
		as: 3,
		type: 2,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", ""],
			tx: {
				name: "",
				desc: "",
			},
			yz: {
				name: "",
				desc: "",
			},
		},
	},
	{
		level: "S2",
		name: "弗林特",
		addr: "lore/S2/FuLinTe",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S2",
		name: "菲兰德",
		addr: "lore/S2/FeiLanDe",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S2",
		name: "阿索隆",
		addr: "lore/S2/ASuoLong",
		width: "200",
		height: "250",
		as: 3,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S3",
		name: "罗根",
		addr: "lore/S3/LuoGen",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S3",
		name: "米娅",
		addr: "lore/S3/MiYa",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S3",
		name: "格雷格",
		addr: "lore/S3/GeLeiGe",
		width: "200",
		height: "250",
		as: 3,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S4",
		name: "阿赫摩斯",
		addr: "lore/S4/AHeMoSi",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S4",
		name: "玲奈",
		addr: "lore/S4/LingNai",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S4",
		name: "琳恩",
		addr: "lore/S4/LinEn",
		width: "200",
		height: "250",
		as: 3,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S5",
		name: "赫克托",
		addr: "lore/S5/HeKeTuo",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S5",
		name: "诺拉",
		addr: "lore/S5/NuoLa",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S5",
		name: "格温",
		addr: "lore/S5/GeWen",
		width: "200",
		height: "250",
		as: 3,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S6",
		name: "无名",
		addr: "lore/S6/WuMing",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S6",
		name: "芮妮",
		addr: "lore/S6/RuiNi",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S6",
		name: "韦恩",
		addr: "lore/S6/WeiEn",
		width: "200",
		height: "250",
		as: 3,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S7",
		name: "艾迪丝",
		addr: "lore/S7/AiDiSi",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S7",
		name: "哥顿",
		addr: "lore/S7/GeDun",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S7",
		name: "布拉德利",
		addr: "lore/S7/BuLaDeLi",
		width: "200",
		height: "250",
		as: 3,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S8",
		name: "阿赫摩斯",
		addr: "lore/S8/AHeMoSi",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: ["英雄殿堂", "英雄招募"],
		data: ["6573", "8568", "128538", "780.62", "780.62"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "列王意志", desc: "作为伟大列王的继承者, 加托能够开启一个“意志护盾”。护盾值相当于攻击力380%, 受到伤害时优先扣除护盾值。护盾最多存在5秒。" },
			tx_2: { label: "王权威慑", desc: "以天生的王者气势震慑敌方全体英雄, 降低其5%攻击力, 同时提升自身攻击力(提升值相当于5%*被威慑的敌方英雄数), 持续3秒。" },
			tx_3: { label: "王者舞步", desc: "加托精湛的格斗技艺有如遒劲的战舞, 使之有15%概率闪避敌方普通攻击, 攻击时有20%概率暴击。" },
			yz_1: { label: "黄金近卫", desc: "加托以近卫军的战术指挥盾兵, 使之防御力提升30%。" },
			yz_2: { label: "列王恩赐", desc: "伟大列王的庇佑惠及加托麾下的盾兵, 使其每次攻击获得相当于自身攻击力30%的护盾, 持续1回合。" },
			yz_3: { label: "王者之师", desc: "加托的精锐之师以赫赫威名震慑对手, 使敌军全体部队的攻击力降低25%。" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S8",
		name: "索尼娅",
		addr: "lore/S8/SuoNiYa",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: ["英雄殿堂", "英雄招募"],
		data: ["8568", "8568", "85692", "780.62", "780.62"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "极度深寒", desc: "喷射出冷冻液, 使一个目标冻结1.5秒, 并对其和周围目标造成攻击力*300%的范围伤害。" },
			tx_2: { label: "冷冻弹", desc: "投射出一枚冷冻弹, 对单体目标造成攻击力*140%的伤害, 并使其周围的目标攻击速度降低50%, 持续3秒。" },
			tx_3: { label: "财迷心窍", desc: "对赏金的渴望令索尼娅狂热地投入战斗, 使其攻击速度提升30%。" },
			yz_1: { label: "宝藏猎人", desc: "“找到传说中的深海宝藏后人人有份！”——索尼娅的许诺激励了所有人的士气, 使我军全体部队伤害提升20%。" },
			yz_2: { label: "赏金诱惑", desc: "索尼娅用赏金激励士兵, 使麾下矛兵每2次攻击可对目标造成75%的额外伤害, 并使我军全体部队攻击力提升25%, 持续1回合。" },
			yz_3: { label: "激流冲击", desc: "索尼娅的矛兵队伍会抓住一切机会, 如海底激流一般发起突袭。矛兵每5回合对目标造成250%伤害, 并使其眩晕1回合。" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S8",
		name: "亨德里克",
		addr: "lore/S8/HengDeLiKe",
		width: "200",
		height: "250",
		as: 3,
		type: 1,
		story: [],
		source: ["英雄殿堂", "英雄招募"],
		data: ["10410", "8568", "64268", "780.62", "780.62"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "拉莱耶之歌", desc: "召唤栖居在黑暗深渊的古老生灵袭击敌人, 对一定范围内的目标造成攻击力*300%的伤害, 并使其因为理智丧失而眩晕1.5秒。" },
			tx_2: { label: "沉沦之锚", desc: "以惊人的怪力抛出沉重的船锚, 对一定范围内的敌人造成攻击力*140%的伤害。" },
			tx_3: { label: "七鳃鳗之吻", desc: "亨德里克船长似乎有着舍去他人力量的奇异能力, 每击败一个地方单位, 可使自身攻击力提升2.5%, 效果最多可叠加15层。" },
			yz_1: { label: "蠕虫之噬", desc: "让巨大的船蛆啃噬敌人的护具, 使敌军全体部队防御力降低25%。" },
			yz_2: { label: "藤壶之铠", desc: "每4回合可让外壳坚硬的藤壶附着在我方部队的身上, 使之防御力提升30%, 持续2回合。" },
			yz_3: { label: "大衮之嗣", desc: "每3回合, 深渊古老生灵的子嗣便会协同亨德里克船长麾下的射手发动一次攻击, 对地方全体部队造成40%伤害。" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S9",
		name: "马格努斯",
		addr: "lore/S9/MaGeNuSi",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S9",
		name: "弗雷德",
		addr: "lore/S9/FuLeiDe",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S9",
		name: "修拉",
		addr: "lore/S9/XiuLa",
		width: "200",
		height: "250",
		as: 3,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S10",
		name: "格里高利",
		addr: "lore/S10/GeLiGaoLi",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S10",
		name: "芙蕾雅",
		addr: "lore/S10/FuLeiYa",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S10",
		name: "布兰琪",
		addr: "lore/S10/BuLanQi",
		width: "200",
		height: "250",
		as: 3,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S11",
		name: "埃莱奥诺拉",
		addr: "lore/S11/AiLaiAoNuoLa",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S11",
		name: "劳埃德",
		addr: "lore/S11/LaoAiDe",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S11",
		name: "鲁弗斯",
		addr: "lore/S11/LuFuSi",
		width: "200",
		height: "250",
		as: 3,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "", desc: "" },
			tx_2: { label: "", desc: "" },
			tx_3: { label: "", desc: "" },
			yz_1: { label: "", desc: "" },
			yz_2: { label: "", desc: "" },
			yz_3: { label: "", desc: "" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S12",
		name: "赫尔薇尔",
		addr: "lore/S12/HeErWeiEr",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: ["英雄殿堂", "兵工厂商店", "通用碎片兑换"],
		data: ["13674", "17826", "267398", "1451.16", "1451.16"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "撼山裂地", desc: "用巨锤猛砸地面, 足以撼动山岳的力量将对前方扇形区域内的敌人造成攻击力*140%的范围伤害, 使命中的目标眩晕1秒, 并使其遭受恫吓, 攻击力降低25%, 持续3秒。" },
			tx_2: { label: "天崩地坼", desc: "赫尔薇尔的怪力足以让敌人肝胆俱裂。她的普通攻击有25%几率造成“恫吓”, 并强化其效果, 使目标受到的伤害提升15%, “恫吓”最多叠加3层。" },
			tx_3: { label: "磐石之躯", desc: "雪山的磨练铸造了有如山岩的身躯, 使赫尔薇尔受到的伤害降低25%, 此外, 使其在每场战斗开始后的9秒内不会受到眩晕、麻痹、冰冻等打断技能影响。" },
			yz_1: { label: "战争怒吼", desc: "赫尔薇尔嘹亮的战吼让战士们热血沸腾, 使我军全体部队的杀伤力提升5%。" },
			yz_2: { label: "不灭之师", desc: "雪山的历练赋予赫尔薇尔和她的战士们坚不可摧的意志和体魄, 使她麾下的盾兵受到的普通攻击的伤害降低25%, 受到技能伤害降低30%。" },
			yz_3: { label: "战火意志", desc: "赫尔薇尔哥她的战士们为战斗而生, 奋战不息的渴望, 使她麾下的盾兵受到的伤害降低15%, 造成的伤害提升10%。" },
		},
		weapon: {
			name: "萨斯拉之锤",
			data: ["2770", "3613", "54202", "923", "1204", "18067", "362.50", "362.50"],
			tx: {
				name: "先祖荣光",
				desc: "赫尔薇尔不仅继承了历代族长的战锤, 更继承了他们的意志。荣耀赋予的力量, 使她的攻击速度提升30%, 普通攻击造成的“恫吓”几率提升25%。",
			},
			yz: {
				name: "霜风坚垒",
				desc: "赫尔薇尔严酷的训练, 使城墙之上的卫士化身磐石般的人形坚垒, 守城部队防御力提升15%。",
			},
		},
	},
	{
		level: "S12",
		name: "加罗尔",
		addr: "lore/S12/JiaLuoEr",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: ["幸运大转盘", "兵工厂商店", "通用碎片兑换"],
		data: ["17826", "17826", "178266", "1451.16", "1451.16"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "破晓冲锋", desc: "踏着破晓晨光铺就的胜利之路发动冲锋, 对前方敌人造成攻击力*280%范围伤害。骑枪将破坏目标的甲胄, 使其防御力降低25%, 持续2秒。" },
			tx_2: { label: "强袭突刺", desc: "接连不断发起迅猛的突刺, 对一定区域内的目标造成攻击力*140%的伤害。" },
			tx_3: { label: "乘胜追击", desc: "胜利的滋味让勇者甘之如饴、让他们越战越勇。每击倒一位敌方英雄, 加罗尔的攻击力将提升12%, 同时也将恢复相当于生命值上限10%的生命值。" },
			yz_1: { label: "守护之翼", desc: "加罗尔轻骑扰敌的战术为战友提供掩护, 使我军全体部队受到的伤害降低20%。" },
			yz_2: { label: "破阵之矛", desc: "加罗尔对步兵阵型的弱点了如指掌, 在他的指挥下, 我军全体部队对矛兵的伤害提升30%, 对盾兵的伤害提升25%。" },
			yz_3: { label: "荣耀战旗", desc: "加罗尔运用历代传承, 赢得过无数荣耀的战术, 使我军全体部队攻击力提升15%, 防御力提升10%。" },
		},
		weapon: {
			name: "凛风之枪",
			data: ["3613", "3613", "36135", "1204", "1204", "12045", "362.50", "362.50"],
			tx: {
				name: "翼之战歌",
				desc: "羽翼麾动的震响有如鼓舞人心的战歌。每次发起破晓冲锋后, 我军全体攻击速度提升14%, 移动速度提升100%, 持续5秒。",
			},
			yz: {
				name: "集群猛攻",
				desc: "作为一名老练的指挥官, 加罗尔深谙大兵团进攻之道, 他的战术将让集结部队的攻击力提升15%。",
			},
		},
	},
	{
		level: "S12",
		name: "丽姬娅",
		addr: "lore/S12/LiJiYa",
		width: "200",
		height: "250",
		as: 3,
		type: 1,
		story: [],
		source: ["最强领主", "冻土之王", "最强王国", "每日特惠", "英雄集结", "兵工厂商店", "通用碎片兑换"],
		data: ["21656", "17826", "133698", "1451.16", "1451.16"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "酸蚀蛛群", desc: "召唤三只携有酸液炸弹的机械蜘蛛冲向对手, 造成攻击力*98%的范围伤害。同时, 喷溅的酸液将溶解目标的武器, 使其攻击力降低25%, 持续2秒。" },
			tx_2: { label: "织命之网", desc: "用锋利的钢丝蛛丝切割对手, 造成攻击力*70%的伤害。蛛丝有100%几率缠绕对手, 使之进入“共振”状态, 持续5秒, 其间丽姬娅受到的伤害将由该目标部分分担。" },
			tx_3: { label: "伴生蛛", desc: "伴生蛛如同守护女王一般保卫着丽姬娅。每当丽姬娅遭受减益效果, 将牺牲一只伴生蛛, 抵消减益, 并使丽姬娅的攻击力提升24%, 持续10秒。每10秒生成1只伴生蛛, 最多存在3只。" },
			yz_1: { label: "钢牙啃噬", desc: "丽姬娅释放出蜘蛛群, 用钢铁铸就的牙齿破坏敌人的甲胄, 使敌军全体部队的防御力降低25%。" },
			yz_2: { label: "瓦解之毒", desc: "在部队射击的间隙, 派遣机械蜘蛛穿插侵袭。射手每2次攻击, 对目标造成100%额外伤害; 蜘蛛喷射的酸液将溶解护甲, 使目标受到的伤害提升25%, 持续1回合。" },
			yz_3: { label: "毒牙侵袭", desc: "将蜘蛛的毒液涂抹于矢石之上, 麾下的射手每2次攻击可使目标进入中毒状态, 额外造成100%的伤害, 并使目标造成的伤害降低20%, 持续1回合。" },
		},
		weapon: {
			name: "织命者",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "蛛巢女王",
				desc: "丽姬娅编制蛛网和操纵蛛群的技巧炉火纯青, 每场战斗开始时, 将自带2只半伴生蛛; 此外, 在释放织命之网时有100%的几率命中1个额外目标。",
			},
			yz: {
				name: "蜘蛛巢城",
				desc: "丽姬娅布置的战术, 让城墙化身为捕猎的巨网, 使守城部队杀伤力提升15%。",
			},
		},
	},
	{
		level: "S13",
		name: "吉塞拉",
		addr: "lore/S13/JiSaiLa",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: ["最强领主", "冻土之王", "最强王国", "每日特惠", "英雄集结", "兵工厂商店", "通用碎片兑换"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "过载猛攻", desc: "吉塞拉使机械臂进入过载模式, 发起迅猛攻击, 并获得50点能量。过载持续5秒, 其间攻速提升60%; 同时机械臂提供的掩护警示防御力提升150%。" },
			tx_2: { label: "钢铁重拳", desc: "用粗壮的铁臂发动沉重的一击, 造成攻击力*140%的范围伤害, 并获得25点能量。" },
			tx_3: { label: "便携式护盾", desc: "吉塞拉将城镇的防护罩微缩化改造后用于自身。每次普通攻击可获得15点能量, 能量达到100时即可激活, 获得相当于攻击力*190%的护盾, 持续3秒。" },
			yz_1: { label: "合金盾牌", desc: "用奥斯特曼工艺改良盾牌, 使我方盾兵的防御力提升30%。" },
			yz_2: { label: "临时工事", desc: "吉塞拉擅长用战场上遗落的材料搭建简易工事。她麾下的盾兵攻击时有40%的几率使我方全体部队防御力提升50%, 持续1回合。" },
			yz_3: { label: "试作护盾", desc: "为我军全体部队装备军团护盾试作性, 有40%几率使其受到的伤害降低50%。" },
		},
		weapon: {
			name: "",
			data: [],
			tx: {
				name: "",
				desc: "",
			},
			yz: {
				name: "",
				desc: "",
			},
		},
	},
	{
		level: "S13",
		name: "弗洛拉",
		addr: "lore/S13/FuLuoLa",
		width: "200",
		height: "250",
		as: 2,
		type: 1,
		story: [],
		source: ["兵工厂商店"],
		data: ["21400", "21400", "214008", "1621.29", "1621.29"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "藤蔓缠绕", desc: "召唤出强有力的藤蔓缠绕敌人, 造成攻击力*140%的范围伤害, 并使目标眩晕2秒。" },
			tx_2: { label: "猛烈绽放", desc: "投掷出花种, 造成攻击力*40%的范围伤害。如果命中英雄, 就会迅速绽放出一朵肉食性的艾多莉雅玫瑰。这朵花具备弗洛拉30%的属性, 能够攻击周围的敌人。" },
			tx_3: { label: "自然之力", desc: "精心的培育使植物无比坚韧, 而培育者自己也在历练中获得了同样坚韧的品质。弗洛拉及其召唤的植物生命值提升10%, 防御力提升20%。" },
			yz_1: { label: "刺疼曼舞", desc: "召唤长有锋利棘刺的藤蔓与战士们共舞, 使我军全体部队攻击时有50%的几率让敌方受到的伤害提升50%。" },
			yz_2: { label: "荆棘花丛", desc: "用强劲的根茎筑起防线, 使我方盾兵受到的伤害降低25%；此外, 艾多莉雅玫瑰喷射的毒刺将协同我方矛兵共同攻击, 使他们造成的伤害提升25%。" },
			yz_3: { label: "芳香迷雾", desc: "以扰乱心智的奇异花香削弱敌人的战意。每4回合使敌方盾兵受到的伤害提升30%, 使敌方射手造成的伤害降低30%, 持续2回合。" },
		},
		weapon: {
			name: "",
			data: [],
			tx: {
				name: "",
				desc: "",
			},
			yz: {
				name: "",
				desc: "",
			},
		},
	},
	{
		level: "S13",
		name: "乌尔卡努斯",
		addr: "lore/S13/WuErKaNuSi",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: ["幸运大转盘", "兵工厂商店"],
		data: ["25998", "21400", "160506", "1621.29", "1621.29"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "破城之箭", desc: "用重弩射出三支足以洞穿城墙的利箭, 造成攻击力*280%的伤害, 并使目标流血。流血效果: 每0.5秒受到的攻击力*10%的伤害, 持续3秒。" },
			tx_2: { label: "禁锢之矢", desc: "朝一个敌方英雄射出附带锁链的飞矢, 对其造成攻击力*140%的伤害, 锁链的缠绕将使其无法行动, 眩晕2秒。" },
			tx_3: { label: "炬火之光", desc: "乌尔卡努斯像驱散黑暗的烈火般鼓舞士气, 使麾下的护卫攻击力提升30%, 防御力提升30%。" },
			yz_1: { label: "枭雄之怒", desc: "乌尔卡努斯善于运用恐惧震慑对手, 他的怒火使敌方全体部队攻击力降低20%。" },
			yz_2: { label: "磔裂之刃", desc: "在武器上附加削铁如泥的钢刃, 使我军全体部队每5次攻击后, 下次攻击对目标造成100%的额外伤害；里人损坏了甲胄, 使目标在下次被攻击时受到15%额外伤害。" },
			yz_3: { label: "破碎之镝", desc: "改良箭矢, 使其拥有更强的威力和破甲性能。每3回合降低敌方盾兵和矛兵60%的防御力；同时提升我方射手60%的攻击力, 持续1回合。" },
		},
		weapon: {
			name: "",
			data: [],
			tx: {
				name: "",
				desc: "",
			},
			yz: {
				name: "",
				desc: "",
			},
		},
	},
];

const handleUpdateValue = (key, item) => {
	activeKey.value = key;
	showHeros.value = allHeroDatum.filter(item => item.level === activeKey.value);
	// showHeros.value = allHeroDatum[activeKey.value]
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

const renderAvatar = obj => {
	const imgUrl = `/images/heros/${obj.addr}/avatar.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderPortrait = obj => {
	const imgUrl = `/images/heros/${obj.addr}/portrait.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderTalent = () => {
	const imgUrl = `/images/heros/${showModalInfo.value.addr}/tf.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderTxImg = () => {
	const imgUrl = `/images/heros/${showModalInfo.value.addr}/tx.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderYzImg = () => {
	const imgUrl = `/images/heros/${showModalInfo.value.addr}/yz.png`;
	console.log("renderYzImg: " + imgUrl);
	return new URL(imgUrl, import.meta.url).href;
};

const renderZwImg = () => {
	const imgUrl = `/images/heros/${showModalInfo.value.addr}/zw.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderZwTxImg = () => {
	const imgUrl = `/images/heros/${showModalInfo.value.addr}/zw-tx.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderZwYzImg = () => {
	const imgUrl = `/images/heros/${showModalInfo.value.addr}/zw-yz.png`;
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
	showHeros.value = allHeroDatum.filter(item => item.level === activeKey.value);
});
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
