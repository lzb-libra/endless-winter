<template>
    <n-layout has-sider>
        <n-layout-sider content-style="padding: 24px;">
          <n-menu :options="menuOptions" @update:value="handleUpdateValue" default-value="shuang_long_ba_zhu" />
        </n-layout-sider>
        <n-layout-content content-style="padding-left: 24px;">
			<h1>规则说明</h1>
			<div>
				<h2>背景故事</h2>
				<p>一个遥远的失落古国都城被发现，改古国以冰龙为标志，其统治者也被民众神化为巨龙的化身。都城中埋藏着无数宝藏，各王国最强大的领主们都前往争夺。这些不速之客的来犯，也唤醒了沉睡已久的古老守护者。</p>
				<h2>玩法介绍</h2>
				<p>战场开启后，被委派参战的领主可进入战场，争夺战场中央霜龙王成的归属权(争夺共持续5小时)。争夺结束后，累计占领王成时间最长的领主将成为本赛区至高无上的霜龙霸主(注: 占领霜龙王城的队伍中仅队长计算占领时长，队伍中其他成员不计算)。</p>
				<h2>流程概要</h2>
				<p>
					<strong>第一阶段: 联名报名(48小时)</strong>
				</p>
				<p>可由盟主及4阶以上成员报名。报名阶段结束时，本赛区内排名靠前的若干联盟可获得联盟参战资格。(赛区内王国越多，可获得参战资格的联盟越多，具体情况以赛区界面说明展示为准)。赛区根据王国的英雄代数及火晶等级开放进度划分，以保证同赛区内的王国进度相同。</p>
				<p style="padding-top: 20px;">
					<strong>第二阶段: 参战委派(48小时)</strong>
				</p>
				<p>获得参战资格的联盟，可由盟主及4阶以上成员委派联盟成员参战。在报名阶段结束后才加入联盟的成员，无法被委派参战。该阶段还将开启竞猜玩法，参与有机会获得大量奖励。</p>
				<p style="padding-top: 20px;">
					<strong>第三阶段: 战场开启前夕(59小时)</strong>
				</p>
				<p>所有获得参战资格的联盟已完成参战人员委派，静待战场开放。</p>
				<p style="padding-top: 20px;">
					<strong>第四阶段: 战场开启(7小时)</strong>
				</p>
				<p>战场开启后，被委派参战的领主可以进入战场</p>
				<p>战场开启后1小时，霜龙王城将开放争夺，争夺持续5小时。首个占领王城的联盟，所有成员将获得一份首占奖励。占领霜龙王城的队伍中仅队长计算占领时长，队伍中其他成员均不计算。</p>
				<p>王城周围的4座石塔，将与王城同时开放争夺。石塔争夺每轮持续30分钟，争夺结束后，进入30分钟的守护状态，等待下一轮开启。每一轮争夺期间，累计占领石塔时间最长的联盟，成员将获得对应石塔所提供的强大联盟特殊加成(持续30分钟)。</p>
				<p>霜龙王城争夺期间，战场中将定期刷新龙髓水晶矿和霜龙护卫，采集龙髓水晶矿和击败霜龙护卫均可获得联盟龙髓水晶，联盟盟主及4阶以上成员可消耗联盟龙髓水晶释放强力的水晶技能，助力王城争夺。</p>
				<p>当王城争夺结束后，累计占领王城时间最长的领主，将成为本赛区至高无上的霜龙霸主，尊享30天的霸主特权，且能获得丰厚的奖励。若有多名领主的占领时间并列最长，则先达到该时长的领主成为霸主。</p>
				<p style="padding-top: 20px;">
					<strong>第五阶段: 战后恢复(55小时)</strong>
				</p>
				<p>霜龙王城争夺结束后，参与争夺的王国将开启战后恢复增益: 治疗速度+500%，治疗资源消耗-30%。</p>
				<p>成为霜龙霸主的领主，可以在所在王国举办一场盛大的霸主宴礼。</p>
				<p>处于该阶段时，赛区内的每位领主可在霸主特权界面为本赛区的霜龙霸主点赞(每日可点赞5次), 每次点赞可获得一份奖励。</p>
			</div>
			<h1>建筑介绍</h1>
			<div></div>
			<h1>水晶技能</h1>
			<div></div>
			<h1>其他</h1>
			<div></div>
		</n-layout-content>
    </n-layout>
</template>

<script setup>
import { ref, h, onMounted } from "vue";

import allActivities from "../data/activitys.json";

const menuOptions = ref([]);

onMounted(() => {
	allActivities.forEach(item => {
		console.log(item)
		menuOptions.value.push({label: item.name, key: item.key})
	})
})
</script>

<style scoped></style>