<template>
	<div style="padding: 0 15px">
		<n-flex>
			<n-card v-for="(obj, index) in allHeroDatum" :key="index" :title="renderCardTitle(obj)" :hoverable="true" :embedded="true" size="small" header-style="text-align: center" footer-style="text-align: center" style="width: 169px; cursor: pointer" @click="clictItem(obj)">
				<template #cover>
					<n-image object-fit="contain" :width="120" :height="120" :src="renderAvatar(obj)" style="display: flex; justify-content: center; margin-top: 20px; margin-bottom: 10px" preview-disabled />
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
	</div>

	<n-modal v-model:show="showModal" transform-origin="center" @after-leave="onAfterLeave">
		<n-card style="width: 1000px" :bordered="false" size="huge" role="dialog" aria-modal="true">
			<div style="display: flex">
				<div style="width: 30%; margin-right: 20px">
					<n-image object-fit="contain" :height="showModalInfo.height" :src="renderPortrait(showModalInfo)" style="display: flex; justify-content: center; margin-top: 20px; margin-bottom: 10px" preview-disabled />
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
import { ref, h } from "vue";

const showModal = ref(false);
const showModalInfo = ref({});

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
			tx_1: { label: "火焰大锤", desc: "挥舞重锤，对前方扇形区域敌人造成攻击*280%的伤害。" },
			tx_2: { label: "护甲强化", desc: "强化护甲，受到的伤害降低30%。" },
			yz_1: { label: "趁热打铁", desc: "史密斯将对锻造的热忱传递给大家，使城镇内铁矿厂的产量提升25%。" },
			yz_2: { label: "铁匠精神", desc: "史密斯与铁矿之间存在着某种神奇的“亲和关系”，出征时铁矿采集速度提升25%。" },
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
			tx_1: { label: "飞斧旋风", desc: "快速旋转，每0.5秒对周围敌人造成攻击*100%的伤害，技能持续3秒。" },
			tx_2: { label: "利刃", desc: "强化斧头，造成伤害增加30%。" },
			yz_1: { label: "祖传技艺", desc: "尤金凭借精湛的伐木技巧，使城镇内伐木场的产量提升25%。" },
			yz_2: { label: "伐木大师", desc: "尤金总能专注于木材的砍伐和采集工作；出征时木材采集速度提升25%。" },
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
			tx_1: { label: "狂轰滥炸", desc: "丢出自制超级炸药，对攻击目标及其周围敌人造成攻击力*196%的伤害。" },
			tx_2: { label: "高爆手雷", desc: "投掷出的手雷有20%概率炸晕目标，造成1.5秒晕眩。" },
			yz_1: { label: "爆破专精", desc: "查理凭借丰富的经验对矿区进行精准爆破，使城镇内煤矿厂的产量提升25%。" },
			yz_2: { label: "煤矿开采", desc: "查理开采煤矿的技术早已炉火纯青，出征时煤矿采集速度提升25%。" },
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
			tx_1: { label: "散射箭", desc: "射出大量箭矢，造成攻击*252%的范围伤害。" },
			tx_2: { label: "狩猎标记", desc: "对目标进行标记，本次攻击对其造成伤害提升30%。" },
			yz_1: { label: "王牌猎人", desc: "克劳瑞斯是冰原上最好的猎人，凭借她的技艺，城镇猎人小屋的产量提升25%。" },
			yz_2: { label: "肉食者", desc: "克劳瑞斯对冰原动物的习性了如指掌，出征时能使生肉采集速度提升25%。" },
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
			tx_1: { label: "盾牌冲击", desc: "用沉重的盾牌撞击敌人，造成280%攻击的范围伤害，并击退对方。" },
			tx_2: { label: "联合防御", desc: "谢尔盖带领大家筑起防线，提升我方所有英雄单位15%防御。" },
			tx_3: { label: "盾牌抵抗", desc: "强化盾牌，自身受到伤害降低30%。" },
			yz_1: { label: "守护之力", desc: "谢尔盖用盾牌守护我方军队，使我军全体部队受到伤害减少20%。" },
			yz_2: { label: "虚弱打击", desc: "谢尔盖能够使敌军全体部队攻击力降低20%。" },
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
			tx_1: { label: "烧烤盛宴", desc: "用丰盛大餐恢复我方全体相当于帕特里克攻击力*280%的生命值，并让我方全体攻击力提升7%。持续4秒。" },
			tx_2: { label: "厚脂肪", desc: "厨师的厚脂肪使自身受到的伤害降低30%。" },
			tx_3: { label: "应急食品", desc: "携带食物，每隔5秒恢复攻击*70%生命。" },
			yz_1: { label: "美食功效", desc: "帕特里克烹调出的美味佳肴激励全队，我军全体部队生命值提升25% 。" },
			yz_2: { label: "能量摄入", desc: "美食激发出斗志和潜能，使我军全体部队攻击力提升25%。" },
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
			tx_1: { label: "疾风突刺", desc: "用长槊锋刃快速猛刺，对前方矩形区域内的敌人造成攻击力*420%的伤害。" },
			tx_2: { label: "气势如虹", desc: "以严整军容高歌猛进，生命值高于50%时，攻击力提升48%。" },
			tx_3: { label: "背水一战", desc: "身经百战的良将不会向逆境屈服；生命值低于50%时，防御力提升150%。" },
			yz_1: { label: "威风八面", desc: "以摧枯拉朽的攻势瓦解敌人的意志，让敌军全体部队攻击力降低20%。" },
			yz_2: { label: "治兵振旅", desc: "向士兵传授祖传武艺，使训练速度提升20%。" },
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
			tx_1: { label: "群山咆哮", desc: "发出摇撼山岳的战吼，恫吓敌人，使全体敌军的攻击力降低5%，持续2秒。" },
			tx_2: { label: "战吼鼓舞", desc: "战吼不仅能威吓敌人，亦能鼓舞战友。施放”群山咆哮“后，使自身和周围我方单位攻击力提升35%，持续2秒。" },
			tx_3: { label: "林间战舞", desc: "常年在丛林与山地作战，赋予卢姆·波根敏捷的身手，使其攻击速度提升30%。" },
			yz_1: { label: "惑敌战术", desc: "卢姆·波根以精湛的游击策略迷惑敌人，使全体敌军部队的穿透力降低20%。" },
			yz_2: { label: "彩虹桥勇士", desc: "卢姆·波根将原住民的狩猎技巧传授给士兵们，使打怪部队的出征速度提升100%。" },
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
			tx_1: { label: "狂扫", desc: "手持机枪疯狂扫射，对扇形范围内敌人每0.5秒造成攻击*75%伤害，持续2秒。" },
			tx_2: { label: "防御改造", desc: "改造护甲，提升70%防御。" },
			tx_3: { label: "武器改造", desc: "改造武器，提升24%攻击。" },
			yz_1: { label: "全副武装", desc: "杰西为我军改进武器，使我军全体部队穿透力提升25%。" },
			yz_2: { label: "机械屏障", desc: "杰西为我军改进护甲，使我军全体部队受到的伤害减少20%。" },
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
			tx_1: { label: "弱点射击", desc: "探险家敏锐的眼神能找到目标弱点，造成攻击*560%伤害。" },
			tx_2: { label: "快速反应", desc: "野外生存经验丰富，攻击速度提升30%。" },
			tx_3: { label: "敏锐视野", desc: "巴希提的枪法精准，造成的伤害增加30%。" },
			yz_1: { label: "危险感知", desc: "巴希提能够感知前方的危险，并采取应对措施，使我军全体部队受到伤害减少20%。" },
			yz_2: { label: "不稳定力场", desc: "巴希提把握战机的能力，使我军全体部队攻击时有50%概率将伤害值提升50%。" },
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
			tx_1: { label: "多重射击", desc: "精确瞄准后，连续射出三发子弹，依次造成攻击力*100%、175%、210%的伤害，其中第三发将造成范围伤害。" },
			tx_2: { label: "火力压制", desc: "凭借精妙的枪法和强大的火力压制敌人，对目标造成攻击力*140%的伤害，并使其攻速降低50%，持续2秒。" },
			tx_3: { label: "射手本能", desc: "精湛的射术已经融入了杰塞尔的本能，使他的攻击力提升24%。" },
			yz_1: { label: "战术推演", desc: "杰塞尔胆识与智慧并存，他的战术素养和指挥才能使我军所有部队穿透力提升25%。" },
			yz_2: { label: "博学多闻", desc: "杰塞尔渊博的学识为城镇带来助益，使科技研究的速度提升15%。" },
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
			tx_1: { label: "爆裂箭", desc: "对一名敌人发射爆裂箭，造成攻击*290%伤害并对周围小范围敌人造成攻击*98%伤害。" },
			tx_2: { label: "风之引导", desc: "吉娜对狙击弩进行了改良，攻击速度提升30%。" },
			tx_3: { label: "鹰眼", desc: "敏锐捕捉敌方弱点，暴击率提升20%。" },
			yz_1: { label: "强劲体魄", desc: "吉娜对领主进行体能训练，使领主体力消耗减少20%。" },
			yz_2: { label: "迅捷行动", desc: "吉娜来去如风，打怪出征速度提升100%。" },
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
			tx_1: { label: "拂晓的鼓点", desc: "以振奋人心的鼓点唤起战意，使我方所有英雄和护卫攻击力提升3.5%，攻击速度提升4.5%，持续4秒。" },
			tx_2: { label: "当头猛击", desc: "瞄准目标的要害，卯足全力掷出鼓槌，对其造成攻击力210%的伤害。" },
			tx_3: { label: "烈风的节拍", desc: "踏着风一样的节拍，让攻势愈发凌厉；每进行3次普通攻击，可使自身攻击速度提升5%，持续至战斗结束。" },
			yz_1: { label: "征伐的战鼓", desc: "出征时，书允会击鼓提升大家的士气，使我军全体部队攻击力提升25%。" },
			yz_2: { label: "疗愈之舞", desc: "以古老的传统医术照顾伤兵，使军医所的治疗速度提升50%。" },
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
			desc: "以领袖气质感染全军, 无论赫罗尼莫是否出征, 都可以使我军全体部队穿透力和生命值提升15%。",
		},
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "三段斩", desc: "将一定范围内的敌人挑高，进行三次斩击，每次造成相当于攻击224%的伤害。" },
			tx_2: { label: "剑气", desc: "每次普攻都将释放剑气，对前方矩形范围内敌人造成攻击23%的伤害。" },
			tx_3: { label: "孤傲", desc: "心高气傲的赫罗尼莫在顺风局中总能表现得更神勇。生命值高于50%时，攻击力提升48% 。" },
			yz_1: { label: "战前宣言", desc: "赫罗尼莫发表战前演讲，使我军全体部队穿透力提升25%。" },
			yz_2: { label: "剑术指导", desc: "传授剑术奥义，使我军全体部队攻击力提升25%。" },
			yz_3: { label: "精湛剑术", desc: "赫罗尼莫传授的剑术使我军全体部队攻击时有20%概率让敌军晕眩，持续1回合。" },
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
		name: "娜塔莉亚",
		addr: "lore/S1/NaTaLiYa",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: [],
		talent: {
			name: "白熊之力",
			desc: "赋予全军白熊般的勇气和力量。无论娜塔莉亚是否出征, 均可使我军全体部队攻击力和防御力提升10%。",
		},
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "野兽怒击", desc: "北极熊立身站起，之后猛砸地面，造成攻击*224%范围伤害，击飞范围内所有敌人并造成1秒晕眩。" },
			tx_2: { label: "鞭笞", desc: "挥舞鞭子，对目标造成攻击*210%的伤害。" },
			tx_3: { label: "熊熊怒火", desc: "白熊和它的伙伴可不好惹。受到伤害时娜塔莉亚有10%机率提升12%攻击，持续3秒(最多叠加5层)。" },
			yz_1: { label: "野性咆哮", desc: "白熊的怒吼如同号角，使我军全体攻击时有20%机率让敌军晕眩。持续1回合。" },
			yz_2: { label: "兽群领袖", desc: "娜塔莉亚激励全队，使我军全体攻击力提升25%。" },
			yz_3: { label: "狂野呼唤", desc: "娜塔莉亚召唤野兽协助作战，使我军全体部队穿透力提升25%。" },
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
			tx_1: { label: "超大雪球", desc: "发射巨大的雪球，对圆形范围内的目标造成攻击*252%伤害，并使之冻结1.5秒。" },
			tx_2: { label: "雪地伏击", desc: "隐藏在雪地中，发动突然袭击，对目标造成攻击*210%的伤害。" },
			tx_3: { label: "少女的执著", desc: "逆境激发出茉莉无尽的潜力，生命值低于50%时，攻速提升60%。" },
			yz_1: { label: "雪之号令", desc: "茉莉带领大家发动势如雪崩的攻击，我军全体部队攻击时有20%的概率使敌军晕眩，持续1回合。" },
			yz_2: { label: "冰雪领域", desc: "雪地是茉莉的主场，她能让我军全体部队攻击时有50%概率使本次伤害提升50%。" },
			yz_3: { label: "少女之怒", desc: "茉莉的愤怒点燃了每一个人的战意，我军全体部队穿透力提升25%。" },
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
			tx_1: { label: "钉枪连射", desc: "对目标连续发射多枚钉子，每枚钉子造成攻击*75%伤害，并晕眩目标2秒。" },
			tx_2: { label: "紧急加固", desc: "生命值低于50%时，迅速搭建起简易的防御工事，使自身防御提升150%。" },
			tx_3: { label: "干劲", desc: "干劲十足，攻击速度提升30%。" },
			yz_1: { label: "固若金汤", desc: "津曼构筑的防线坚实可靠，使我军全体防御力提升10%，生命值提升10%。" },
			yz_2: { label: "建筑艺术", desc: "津曼可以合理控制施工流程，使建筑耗费的资源减少15%，使建筑升级速度提升15%。" },
			yz_3: { label: "阵地战强者", desc: "津曼能够巧妙利用地形创造进攻优势，使我军全体部队穿透力提升25%。" },
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
			tx_1: { label: "灼热之焰", desc: "喷射出熊熊燃烧的烈火灼烧敌人，每0.5秒造成相当于攻击力*84%的伤害，并使目标受到的伤害提升30%，持续2秒。" },
			tx_2: { label: "怒火中烧", desc: "伤痛将激发弗林特的潜力。生命值低于50%时，立即恢复当于自身生命上限40%的生命值。每场战斗只能生效1次。" },
			tx_3: { label: "热源扩散", desc: "火焰将为比肩作战的同伴们驱散寒意，使我方全体英雄攻击速度提升7%。" },
			yz_1: { label: "野火燎原", desc: "金石碰撞出的火星也能燃起燎原之火。我军全体部队攻击时有20%概率触发灼烧效果，使敌军每回合受到40%的伤害，持续3回合。" },
			yz_2: { label: "燃烧意志", desc: "火焰驱散了寒冷，也点燃了战斗的激情。使我军全体部队攻击力提升25%。" },
			yz_3: { label: "无尽烈火", desc: "火焰将吞噬一切——我军全体部队攻击有50%概率让敌军受到的伤害提升50%。" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			tx_1: { label: "紧急治疗", desc: "菲兰德凭借精湛的医术立即为我方所有英雄恢复相当于她攻击力*280%的生命值。" },
			tx_2: { label: "妙手回春", desc: "靠着与死神博弈的技巧，菲兰德为我方生命值百分比最低的英雄恢复相当于她攻击力*140%的生命值。" },
			tx_3: { label: "麻痹药剂", desc: "使敌方单体目标中毒，对其造成相当于菲兰德攻击*196%的伤害，并使目标1秒内无法行动。" },
			yz_1: { label: "劲健秘诀", desc: "菲兰德的调理让士兵们身强体健，使我军攻击力提升15%，防御力提升10%。" },
			yz_2: { label: "强化药剂", desc: "菲兰德用秘制的汤剂强化战士们的身体机能，使我军全体部队攻击时有25%概率造成200%伤害。" },
			yz_3: { label: "眩晕孢子", desc: "在武器上涂抹神秘菌类孢子的提取物，让我军全体部队攻击时有20%的概率使敌人晕眩，持续1回合。" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
		name: "阿隆索",
		addr: "lore/S2/ALongSuo",
		width: "200",
		height: "250",
		as: 3,
		type: 1,
		story: [],
		source: [],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "强力渔网", desc: "对目标区域抛撒捕鱼网，造成攻击*280%点范围伤害，并使敌方1.5秒内不可行动。" },
			tx_2: { label: "潮汐力量", desc: "对目标射出威力强劲，势如海啸的鱼叉，造成相当于攻击*70%的范围伤害。" },
			tx_3: { label: "鱼叉重击", desc: "阿隆索用沉重的鱼叉痛击对手。每8次普攻后，下次攻击使目标晕眩0.5秒。" },
			yz_1: { label: "惊涛骇浪", desc: "阿隆索的力量如同巨浪，令人慑服，让我军全体部队攻击时有20%的概率使敌军晕眩，持续1回合。" },
			yz_2: { label: "钢铁意志", desc: "阿隆索用坚不可摧的意志鼓舞大家，让我军全体部队攻击时有20%概率使敌军穿透力减少50%，持续2回合。" },
			yz_3: { label: "锋锐鱼叉", desc: "阿隆索在武器上涂抹剧毒，让我军全体部队攻击有50%概率使本次伤害提升50%。" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			tx_1: { label: "毁灭之拳", desc: "挥动万钧之力的铁拳猛砸向地面，造成的冲击波将前方目标造成攻击力*168%的伤害，并使目标攻击速度降低50%，持续4秒。" },
			tx_2: { label: "动力装甲", desc: "罗根的动力装甲有着惊人的防护性能，受到攻击时有16%机率提升20%防御，持续2秒，最多叠加5层。" },
			tx_3: { label: "怒风猛击", desc: "挥出带动凛冽怒风的重拳，对扇形范围内的目标造成攻击力*112%的伤害，且有30%的几率使目标晕眩1秒。" },
			yz_1: { label: "怒狮强袭", desc: "罗根改进过的武器能够更容易地撕裂敌人的伤口，使我军攻击时有20%几率让敌军每回合额外受到40%伤害，持续3回合。" },
			yz_2: { label: "猛狮恫吓", desc: "罗根用猛狮般的气势恫吓对手，从而使我军全体部队受到的伤害降低20%。" },
			yz_3: { label: "领袖鼓舞", desc: "罗根与生俱来的领袖气质鼓舞着大家，使我军全体部队生命值提升25%。" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			tx_1: { label: "华丽一击", desc: "投掷出卡牌，对目标造成攻击力*378%的伤害，并随机产生以下两种效果之一：使目标攻击力降低20%，持续2秒；或使目标晕眩1.5秒。" },
			tx_2: { label: "出其不意", desc: "向一个目标发动突然袭击，以米娅攻击力*70%为“基础值”，对其造成浮动伤害，最终伤害将是“基础值”的5%至600%间的随机数。" },
			tx_3: { label: "全力守护", desc: "守护我方剩余生命值百分比最低的英雄，以米娅攻击力*140%为“基础值”，为其恢复生命值。最终恢复值将是“基础值”的5%至400%间的随机数。" },
			yz_1: { label: "洞悉弱点", desc: "我军有50%概率使敌方暴露弱点，使其受到的伤害提升50%。" },
			yz_2: { label: "幸运加护", desc: "米娅带来了好运，使我军全体部队攻击时有50%概率使本次伤害提升50%。" },
			yz_3: { label: "战局解读", desc: "战前的分析让米娅预先发觉了潜在的危险，她的指引有40%概率使我军全体部队受到的伤害降低50%。" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			tx_1: { label: "天降正义", desc: "召唤一个从天而降的牢笼，对范围内的敌人造成相当于攻击力*224%的伤害，并使其眩晕2秒。" },
			tx_2: { label: "惩恶扬善", desc: "对敌方目标进行审判，施以惩戒或褒奖。惩戒将对目标造成相当于格雷格攻击力*300%的伤害；褒奖将为目标恢复相当于格雷格攻击力*50的生命值。" },
			tx_3: { label: "公正审判", desc: "让敌人为自己犯下的罪刑受到严惩，使之受到的伤害提升30%，持续3秒。" },
			yz_1: { label: "正义之剑", desc: "让士兵们化身为所向披靡的正义之剑，有20%概率使我军全体部队造成伤害提升40%，持续3回合。" },
			yz_2: { label: "律令震慑", desc: "用律法的威严震摄恶徒，使我军全体部队攻击时有20%几率使敌军穿透力降低50%，持续2回合。" },
			yz_3: { label: "秩序庇护", desc: "秩序与律法的信念鼓舞着每一个人，让我军全体部队生命值提高25%。" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			tx_1: { label: "克图格亚之佑", desc: "架起坚盾抵御敌人的猛攻，自身进入无敌状态(其间无法移动和施放技能且免疫控制)，周围友军受到的伤害降低70%，持续2秒。" },
			tx_2: { label: "破日之锋", desc: "用锐利的枪锋贯穿前方的敌人，造成攻击力*98%的伤害，并撕裂防线，使敌人在此后2秒内承受的伤害提升20%。" },
			tx_3: { label: "先祖的祝福", desc: "火晶的能量有如先祖的祝福，能治愈阿赫摩斯的伤痛。施放“克图格亚之佑”后，每秒恢复攻击力*42%的生命值，持续5秒。" },
			yz_1: { label: "蝮蛇方阵", desc: "让部队采用古时守护者的防御阵型，盾兵每4次攻击后，将放弃下次攻击，并使矛兵和射手受到的伤害降低30%，盾兵受到的伤害降低70%，持续2回合。" },
			yz_2: { label: "火之祝祷", desc: "用火晶的力量强化我方盾兵的战斗意志，使他们造成的伤害提升100%。" },
			yz_3: { label: "光铸之刃", desc: "将火晶的精华注入盾兵的武器，使他们每次攻击可对目标造成60%额外伤害，并使目标受到的伤害提升25%，持续1回合。" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			tx_1: { label: "幻影突袭", desc: "以迅疾如风的身手从敌人背后发起突袭，造成攻击力*420%的范围伤害。" },
			tx_2: { label: "影遁秘术", desc: "受到普通攻击时有25%几率以幻术骗过对手，从而免受伤害。" },
			tx_3: { label: "神秘之舞", desc: "对敌方目标(英雄优先)施加幻术，对其造成相当于攻击力*140%的伤害，并使其在1.5秒内无法行动。" },
			yz_1: { label: "忍者本能", desc: "玲奈知道如何最有效地猛击敌人的弱点，使我军全体部队普通攻击伤害提升30%。" },
			yz_2: { label: "迅影舞步", desc: "玲奈的指挥技艺轻巧灵动，使我军全体部队受到普通攻击时有20%几率躲避伤害。" },
			yz_3: { label: "影刃", desc: "玲奈的战术变幻莫测，使矛兵有25%几率额外攻击一次，造成200%的伤害。" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			tx_1: { label: "锡德拉克战歌", desc: "以战歌的旋律振奋人心，使我方全体摆脱异常状态(如冰冻、眩晕等)，并提升7%攻击力，持续5秒，其间不受任何异常状态影响." },
			tx_2: { label: "决胜终曲", desc: "抓住转瞬即逝的良机，发射出威力十足的子弹，对沿途敌人造成攻击*300%的伤害。" },
			tx_3: { label: "不协和音", desc: "用神秘且怪异的旋律迷惑对手，使敌方全体攻击速度降低3%，并使其受到的治疗效果降低60%。" },
			yz_1: { label: "雄狮之歌", desc: "琳恩用激昂的节拍与旋律鼓舞人心，有40%几率使我军全体部队穿透力提升50%。" },
			yz_2: { label: "迷惑之音", desc: "琳恩以奇异的琴音干扰敌人，使敌军全体部队穿透力降低20%" },
			yz_3: { label: "欧纳伊华彩", desc: "琳恩用音乐的力量提振士气，让士兵越战越勇;使射手每3次攻击可使自身攻击力提升5%，可叠加，持续至战斗结束。" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			tx_1: { label: "鋼刃戰舞", desc: "揮動戰刃，發起如舞蹈般的迺勁攻勢，4秒內攻擊速度提升120%，作用期間免疫冷凍、暈眩等控制效果。" },
			tx_2: { label: "殊死搏鬥", desc: "赫克托早已習慣與致命的危險共舞，生命值低於50%時，受到的傷害降低60%。" },
			tx_3: { label: "勇者不屈", desc: "身處逆境更能激發赫克托的戰鬥意志；生命值低於50%時，攻擊力提升48%。" },
			yz_1: { label: "生存本能", desc: "求生技巧早已融入赫克托成為本能，他的存在使我軍全體受到的傷害有40%機率減少50%。" },
			yz_2: { label: "雷霆突擊", desc: "赫克托擅長帶領小隊進行突襲，沖散對手的防禦陣型，同時為射手創造齊射的機會。發起攻擊時，盾兵傷害提升200%，射手造成的傷害提升50%；此後每次攻擊增益效果為上衣一次的80%。攻擊5次後效果消失。" },
			yz_3: { label: "疾風猛襲", desc: "赫克托深諳進攻的藝術，使我軍全體在攻擊時有25%機率造成200%的傷害。" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			tx_1: { label: "怒雷猛攻", desc: "同时掷出5枚威力强劲的手雷，对随机目标(英雄优先)造成攻击力*60%/66%/72%/78%/84%的范围伤害" },
			tx_2: { label: "闪光弹", desc: "投掷出闪光弹，对一定范围内的目标造成攻击力*50%/55%/60%/65%/70%的伤害，并使其量眩1.5秒" },
			tx_3: { label: "风驰电掣", desc: "在轰鸣的引擎声中发动凌厉的攻势，使我方全体攻击力提升3%/3.5%/4%/4.5%/5%" },
			yz_1: { label: "多兵种作战", desc: "诺拉擅长多兵种共同作战，他的指挥可以使盾兵和射手受到的伤害降低15%，造成的伤害提升15%" },
			yz_2: { label: "攻其不备", desc: "诺拉是奇袭高手，可使矛兵攻击时有20%几率对全体敌军造成20%/40%/60%/80%/100%额外伤害" },
			yz_3: { label: "乘势追击", desc: "诺拉的鼓舞下，矛兵每攻击5次，使我军全造成的伤害提升5%/10%/15%/20%/25%，受到的伤害降低5%/10%/15%/20%/25%" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			tx_1: { label: "炮火轰击", desc: "以强劲的火力轰击后排的敌军目标(英雄优先）造成攻击力*180%/198%/216%/234%/252%的范围伤害。爆炸产生的震波还将降低目标50 %的攻击速度，持续2秒" },
			tx_2: { label: "空中狙击", desc: "在空中利用广阔的视野精准射击目标(英雄优先）造成攻击力*100%/110%/120%/130%/140%的伤害，有50%的几率整中要害使伤害翻倍" },
			tx_3: { label: "天火降临", desc: "发射燃烧弹，每秒对燃烧范围内的敌方造成攻击力*35%/38.5%/42%/45.5%/49%的伤害，持续3秒" },
			yz_1: { label: "鹰之视野", desc: "善于飞行的格温能准确捕捉敌人的弱点，因此，我军全体部队攻击时可使目标受到的伤害提升25%。" },
			yz_2: { label: "空中压制", desc: "格温能利用制空权压制敌人，得益于此，使我军全每5次攻击后的下一次攻击可对目标造成20%/40%/60%/80%/100%的伤害，并使目标在下一次被攻击时额外受到5%/7.5%/10%/12.5%/15%的伤害" },
			yz_3: { label: "爆破小队", desc: "格温的士兵们装备的手榴弹，射手每四次后的下次攻击可对敌方全体造成10%/20%/30%/40%/50%额外伤害" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			tx_1: { label: "横贯八方", desc: "飞速旋转手中长棍，形成密不透风的屏障，使自身进入2秒的无敌状态;此后横扫前方，造成攻击力*100%的范围伤害。" },
			tx_2: { label: "凝神聚气", desc: "驱除杂念，一心应战，使自身攻击力提升8%，防御力提升16%持续4秒。" },
			tx_3: { label: "隔山打牛", desc: "深厚的内功使无名的每一击都充满力量，每次普通攻击都可对一个随机敌方目标造成攻击力*20%的伤害。" },
			yz_1: { label: "避风扑雨", desc: "无名深知如何躲避和化解敌人的锋芒，使盾兵受到普攻伤害减少25%，受到技能伤害减少30%。" },
			yz_2: { label: "半月冲霄", desc: "无名向士兵们传授精妙的招式，使我军全体部队造成的所有伤害提升20%。" },
			yz_3: { label: "四象分明", desc: "无名的点拨让大家对战斗技艺的理解更加深刻，使我军全体部队造成的技能伤害提升25%。" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			tx_1: { label: "幻觉云雾", desc: "彩球炸开，释放神秘云雾，对范围内敌人造成攻击力“100%的伤害，并使其混乱1秒。混乱状态的敌人会无差别普攻周围的目标，不分敌友。" },
			tx_2: { label: "星空彩绘", desc: "泼酒出梦幻般的颜料，对范围内目标造成攻击力*50%的伤害：并给目标加上星绘标记，使之受到的伤害提升2%，持续4秒。" },
			tx_3: { label: "梦之视界", desc: "带有星绘标记的目标在芮妮的视野中无处遁逃。标记的存在将使芮妮的攻击力提高提升8%，并使她对带有标记的目标伤害提升4%。" },
			yz_1: { label: "惊梦留痕", desc: "芮妮总是以不可思议的方式战斗，其所率部队每两回合可使目标带上梦之痕，并使其下回合额外受到一次200%的矛兵伤害。梦之痕存在1回合。" },
			yz_2: { label: "捕梦手", desc: "梦之痕使芮妮能更够精准地发现敌人的弱点，使矛兵对带有梦之痕的目标造成的伤害提升150%。" },
			yz_3: { label: "梦境切片", desc: "梦之痕使敌人更易暴露脆弱的一面。我军全体对带有梦之痕的目标造成的伤害提升75%。" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			tx_1: { label: "飓风回旋", desc: "投掷出回旋镖，对前方直线上的敌人造成攻击力*100%范围伤害回旋镖返回时，将再次对沿途目标造成相同伤害。" },
			tx_2: { label: "幻影闪击", desc: "韦恩能以常人难以看清的速度拔枪、开枪。普攻时，有15%的概率可快速再次进行普攻，对目标造成额外一次伤害。" },
			tx_3: { label: "正午时刻！", desc: "韦恩的枪法出神入化，造成伤害时有3%的概率暴击。" },
			yz_1: { label: "惊雷奇袭", desc: "韦恩制定的精妙奇袭计划，使我军全体每4回合可对目标发动一次额外打击，造成100%的伤害。" },
			yz_2: { label: "迂回打击", desc: "韦恩擅长利用战术绕开防线，击敌软肋，使射手每2次攻击对敌方矛兵造成40%额外伤害，对敌方射手造成20%额外伤害。" },
			yz_3: { label: "电光石火", desc: "凭借敏锐的洞察力，韦恩能抓住对手每个暴露弱点的瞬间，使我军全体部队普攻时有25%概率造成暴击。" },
		},
		weapon: {
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
		level: "S7",
		name: "艾迪丝",
		addr: "lore/S7/AiDiSi",
		width: "200",
		height: "250",
		as: 1,
		type: 1,
		story: [],
		source: ["最强领主", "冻土之王", "最强王国", "每日特惠", "英雄集结"],
		skill: {
			data: ["", "", "", "", ""],
			tx_1: { label: "愤怒铁拳", desc: "铁皮先生将猛击试图伤害艾迪丝的坏家伙！他挥动的铁拳将对前方扇形范围内的敌人造成攻击力*140%的伤害，并使之眩晕1秒；同时使自身攻击力提升100%，持续2秒。" },
			tx_2: { label: "紧急逃生", desc: "生命值归零时，铁皮先生将发射核心部件，护送艾迪丝逃生。身躯的剩余部件则会引爆，对周围敌人造成攻击力*280%的伤害。" },
			tx_3: { label: "危险预判", desc: "艾迪丝时刻观察战场，提醒铁皮先生及时抵御危险，使其受到的伤害有50%几率减免50%。" },
			yz_1: { label: "攻守兼备", desc: "铁皮先生庞大的身躯为远程部队提供掩护，使我方射手受到的伤害降低20%；此外，他的力量压制也为我方矛兵创造了更多发起进攻的机会，使他们造成的伤害提升20%。" },
			yz_2: { label: "铜头铁臂", desc: "用刀枪不入的身躯掩护共同搭建防线的战友，使盾兵受到的伤害降低20%。" },
			yz_3: { label: "钢甲护体", desc: "艾迪丝打造的便携式防御设备精密而可靠，使我军全体部队生命值提升25%。" },
		},
		weapon: {
			name: "爱心工具箱",
			data: ["", "", "", "", "", "", "", ""],
			tx: {
				name: "小小工程师",
				desc: "艾迪丝运用超乎年龄的工程学造诣为铁皮先生提供照料。生命值低于50%时, 立即恢复一定的生命值(相当于生命值上限的35%), 并提升30%防御力, 直至战斗结束。每场战斗只能触发1次。",
			},
			yz: {
				name: "坚固工事",
				desc: "艾迪丝与铁皮先生共同修建的防御工事为守城部队提供了更好的掩护, 使他们的生命值提升15%。",
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
			tx_1: { label: "酸蚀爆裂", desc: "发射出巨大的毒液罐，破碎后挥发的气体形成毒气区域，持续3秒，每0.5秒对区域内的目标造成攻击力*70%的伤害。" },
			tx_2: { label: "酸液瓶", desc: "精准投出毒液瓶子，使目标进入中毒状态，每0.5秒对其造成攻击力*35%的伤害，并使其受到的伤害提升25%，持续2秒。" },
			tx_3: { label: "强化体质", desc: "剧毒未能夺走哥顿的生命，反倒改变了他的体质，使他的防御力提升75%。。" },
			yz_1: { label: "淬炼锋刃", desc: "在矛兵的武器上涂抹毒液，使他们每2次攻击可造成100%的额外伤害，并致目标中毒，持续1回合。中毒期间，目标造成的伤害降低20%。" },
			yz_2: { label: "恐惧威慑", desc: "在长矛上涂抹毒液的战法令敌人胆寒，每3回合，士气便会此消彼长，我军矛兵造成的伤害提升150%，敌军全体部队造成的伤害降低30%，持续1回合。" },
			yz_3: { label: "腐蚀云雾", desc: "哥顿的特殊战法每4回合会产生毒气云雾，使冲在前头的敌方盾兵浑身无力，受到伤害提升30%；云雾还会遮蔽敌方射手的视线，使之造成的伤害降低30%，持续2回合。" },
		},
		weapon: {
			name: "蝕骨之毒",
			data: ["4384", "3613", "27101", "1461", "1204", "9033", "362.50", "362.50"],
			tx: {
				name: "1325号药剂",
				desc: " 哥顿精心调配的剧毒可使他造成的伤害提升25%, 并使中毒的目标攻击力降低15%。",
			},
			yz: {
				name: "酸液侵袭",
				desc: " 用特制的剧毒武装全体盟友, 使集结部队的穿透力提升15%。",
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
			tx_1: { label: "毁灭重炮", desc: "将重炮转化为毁灭模式，并发射威力惊人的炮弹，造成攻击力*420%的范围伤害。" },
			tx_2: { label: "燃烧弹", desc: "发射特殊的炮弹，对目标造成攻击力*84%的范围伤害，并留下一个燃烧弹坑。弹坑将存在2秒，每0.5秒对弹坑内的敌人造成攻击力*25%的伤害。" },
			tx_3: { label: "悍将不屈", desc: "身经百战的布拉德利从不会向危险屈服，攻击力提升26%。" },
			yz_1: { label: "老兵的骄傲", desc: "丰富的作战经验让布拉德利懂得如何最有效率地摧毁敌人，他的指挥素养使我军全体部队攻击力提升25%。" },
			yz_2: { label: "当头炮", desc: "布拉德利擅长用炮火打乱敌军前排阵型，使我军全体部队对矛兵的伤害提升30%，对盾兵的伤害提升25%。" },
			yz_3: { label: "洞悉战局", desc: "布拉德利不会放过敌军稍纵即逝的松懈，每4回合可使我军全体部队造成的伤害提升30%，持续2回合。" },
		},
		weapon: {
			name: "雷霆重炮",
			data: ["", "", "", "", "", "", "", ""],
			tx: {
				name: "总攻的炮火",
				desc: " 震耳欲聋的炮声不仅能震慑敌人, 也能提振我方士气！施放“毁灭重炮”后我方英雄和护卫攻击速度提升14%持续5秒。",
			},
			yz: {
				name: "精准布防",
				desc: " 作为攻城老手, 布拉德利同样也明白什么样的防线最令攻城者头疼。他针对性的防御部署, 可使守城部队的攻击力提升15%。",
			},
		},
	},
	{
		level: "S8",
		name: "加托",
		addr: "lore/S8/JiaTuo",
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
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			name: "",
			data: ["", "", "", "", "", "", "", ""],
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
			data: ["", "", "", "", "", "", "", ""],
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
