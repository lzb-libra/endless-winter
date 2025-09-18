<template>
	<n-layout>
		<n-layout-header style="padding: 10px 0;">
			<n-select v-model:value="selectValue" :options="selectOptions" @update:value="handleUpdateValue" />
		</n-layout-header>
		<n-layout-content>
			<div v-show="selectValue === 'shuang_long_ba_zhu'">
				<n-tabs type="line" animated>
					<n-tab-pane name="规则说明" tab="规则说明">
						<h2>背景故事</h2>
						<p>一个遥远的失落古国都城被发现，改古国以冰龙为标志，其统治者也被民众神化为巨龙的化身。都城中埋藏着无数宝藏，各王国最强大的领主们都前往争夺。这些不速之客的来犯，也唤醒了沉睡已久的古老守护者。</p>

						<h2>玩法介绍</h2>
						<p>战场开启后，被委派参战的领主可进入战场，争夺战场中央霜龙王成的归属权(争夺共持续5小时)。争夺结束后，累计占领王成时间最长的领主将成为本赛区至高无上的霜龙霸主(注:
							占领霜龙王城的队伍中仅队长计算占领时长，队伍中其他成员不计算)。</p>

						<h2>流程概要</h2>
						<p>
							<strong>第一阶段: 联名报名(48小时)</strong>
						</p>
						<p>可由盟主及4阶以上成员报名。报名阶段结束时，本赛区内排名靠前的若干联盟可获得联盟参战资格。(赛区内王国越多，可获得参战资格的联盟越多，具体情况以赛区界面说明展示为准)。赛区根据王国的英雄代数及火晶等级开放进度划分，以保证同赛区内的王国进度相同。
						</p>
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
						<p>王城周围的4座石塔，将与王城同时开放争夺。石塔争夺每轮持续30分钟，争夺结束后，进入30分钟的守护状态，等待下一轮开启。每一轮争夺期间，累计占领石塔时间最长的联盟，成员将获得对应石塔所提供的强大联盟特殊加成(持续30分钟)。
						</p>
						<p>霜龙王城争夺期间，战场中将定期刷新龙髓水晶矿和霜龙护卫，采集龙髓水晶矿和击败霜龙护卫均可获得联盟龙髓水晶，联盟盟主及4阶以上成员可消耗联盟龙髓水晶释放强力的水晶技能，助力王城争夺。</p>
						<p>当王城争夺结束后，累计占领王城时间最长的领主，将成为本赛区至高无上的霜龙霸主，尊享30天的霸主特权，且能获得丰厚的奖励。若有多名领主的占领时间并列最长，则先达到该时长的领主成为霸主。</p>
						<p style="padding-top: 20px;">
							<strong>第五阶段: 战后恢复(55小时)</strong>
						</p>
						<p>霜龙王城争夺结束后，参与争夺的王国将开启战后恢复增益: 治疗速度+500%，治疗资源消耗-30%。</p>
						<p>成为霜龙霸主的领主，可以在所在王国举办一场盛大的霸主宴礼。</p>
						<p>处于该阶段时，赛区内的每位领主可在霸主特权界面为本赛区的霜龙霸主点赞(每日可点赞5次), 每次点赞可获得一份奖励。</p>
					</n-tab-pane>
					<n-tab-pane name="建筑介绍" tab="建筑介绍">
						<div style="display: flex; margin-top: 20px;">
							<n-image preview-disabled style="width: 100px; height: 100px;" :src="renderSLBZActivityImg('shuangLongWangCheng')" />
							<div style="padding-left: 15px;">
								<div style="font-weight: bold; font-size: 1.25em;">霜龙王城</div>
								<p>坐落于战场中央的古老王城，栖息着传说中的冰霜巨龙，内有旧都近卫的守护，外有四座蕴含强大能量的石塔庇护。王城将于战场开启1小时后开放争夺，占领王城时间最长的领主，将成为至高无上的霜龙霸主。</p>
							</div>
						</div>
						<n-divider />
						<div style="display: flex;">
							<n-image preview-disabled style="width: 100px; height: 100px;" :src="renderSLBZActivityImg('shengMingShiTa')" />
							<div style="padding-left: 15px;">
								<div style="font-weight: bold; font-size: 1.25em;">生命石塔</div>
								<p>象征着生命之力的石塔，蕴含强大的能量。每一轮争夺期间，累计占领该石塔时间最长的联盟，所有成员可获得持续30分钟的强大特殊加成：生命值+50%。</p>
							</div>
						</div>
						<n-divider />
						<div style="display: flex;">
							<n-image preview-disabled style="width: 100px; height: 100px;" :src="renderSLBZActivityImg('longXiShiTa')" />
							<div style="padding-left: 15px;">
								<div style="font-weight: bold; font-size: 1.25em;">龙息石塔</div>
								<p>象征着巨龙之力的石塔，蕴含强大的能量。每一轮争夺期间，累计占领该石塔时间最长的联盟，所有成员可获得持续30分钟的强大特殊加成：杀伤力+50%。</p>
							</div>
						</div>
						<n-divider />
						<div style="display: flex;">
							<n-image preview-disabled style="width: 100px; height: 100px;" :src="renderSLBZActivityImg('biHuShiTa')" />
							<div style="padding-left: 15px;">
								<div style="font-weight: bold; font-size: 1.25em;">庇护石塔</div>
								<p>象征着庇护之力的石塔，蕴含强大的能量。每一轮争夺期间，累计占领该石塔时间最长的联盟，所有成员可获得持续30分钟的强大特殊加成：防御力+50%。</p>
							</div>
						</div>
						<n-divider />
						<div style="display: flex;">
							<n-image preview-disabled style="width: 100px; height: 100px;" :src="renderSLBZActivityImg('fengRenShiTa')" />
							<div style="padding-left: 15px;">
								<div style="font-weight: bold; font-size: 1.25em;">锋刃石塔</div>
								<p>象征着征服之力的石塔，蕴含强大的能量。每一轮争夺期间，累计占领该石塔时间最长的联盟，所有成员可获得持续30分钟的强大特殊加成：攻击力+50%。</p>
							</div>
						</div>
					</n-tab-pane>
					<n-tab-pane name="水晶技能" tab="水晶技能">
						<h2>技能规则</h2>
						<ol>
							<li>参战联盟中进入战场的4阶、5阶成员可以消耗联盟龙髓水晶施放联盟水晶技能，使战场内的联盟成员获得对应的战场增益属性。</li>
							<li>龙髓水晶可通过采集龙髓水晶矿以及击败霜龙护卫获得。</li>
							<li>不同技能使用消耗的龙髓水晶数量不同。</li>
							<li>每个技能都有独立的冷却时间，冷却期间无法再次使用技能。</li>
							<li>霜龙王城争夺结束后，将无法使用技能。技能详情</li>
						</ol>

						<h2>技能详情</h2>
						<div style="display: flex;">
							<n-image preview-disabled style="width: 70px; height: 70px;" :src="renderSLBZActivityImg('longXueBiYou')" />
							<div style="padding-left: 15px;">
								<div style="font-weight: bold; font-size: 1.25em;">龙血庇佑</div>
								<p>10分钟内，联盟成员在霜龙王城与石塔建筑战斗并获胜时，治愈本次战斗受伤士兵的50%，使之可以立即投入新的战斗。</p>
							</div>
						</div>
						<n-divider />
						<div style="display: flex;">
							<n-image preview-disabled style="width: 70px; height: 70px;" :src="renderSLBZActivityImg('longYiSuSheng')" />
							<div style="padding-left: 15px;">
								<div style="font-weight: bold; font-size: 1.25em;">龙裔苏生</div>
								<p>10分钟内，联盟成员在战场中进攻其他领主城镇时，损失士兵的50%将转化为受伤士兵进入军医所。</p>
							</div>
						</div>
						<n-divider />
						<div style="display: flex;">
							<n-image preview-disabled style="width: 70px; height: 70px;" :src="renderSLBZActivityImg('longGuJinGu')" />
							<div style="padding-left: 15px;">
								<div style="font-weight: bold; font-size: 1.25em;">龙骨禁锢</div>
								<p>10分钟内，联盟成员进攻其他领主城镇获胜后，会迫使敌方城镇迁移至边域，并使对方在10分钟内无法进行迁城。</p>
							</div>
						</div>
						<n-divider />
						<div style="display: flex;">
							<n-image preview-disabled style="width: 70px; height: 70px;" :src="renderSLBZActivityImg('longXiJianCheng')" />
							<div style="padding-left: 15px;">
								<div style="font-weight: bold; font-size: 1.25em;">龙息坚城</div>
								<p>10分钟内，联盟成员在城镇进行防守战斗时，使敌方士兵的损失率提高50%，我方士兵的受伤率降低50%。</p>
							</div>
						</div>
						<n-divider />
						<div style="display: flex;">
							<n-image preview-disabled style="width: 70px; height: 70px;" :src="renderSLBZActivityImg('longLinShouHu')" />
							<div style="padding-left: 15px;">
								<div style="font-weight: bold; font-size: 1.25em;">龙鳞守护</div>
								<p>30分钟内，联盟成员在箱龙王城和石塔建筑进行防守战斗时，守城部队攻击力和防御力提升15%。</p>
							</div>
						</div>
						<n-divider />
						<div style="display: flex;">
							<n-image preview-disabled style="width: 70px; height: 70px;" :src="renderSLBZActivityImg('longTouZhanQi')" />
							<div style="padding-left: 15px;">
								<div style="font-weight: bold; font-size: 1.25em;">龙头战旗</div>
								<p>30分钟内，联盟成员的集结容量提升30%。</p>
							</div>
						</div>
						<n-divider />
						<div style="display: flex;">
							<n-image preview-disabled style="width: 70px; height: 70px;" :src="renderSLBZActivityImg('longYiJiXing')" />
							<div style="padding-left: 15px;">
								<div style="font-weight: bold; font-size: 1.25em;">龙翼疾行</div>
								<p>10分钟内，联盟成员单人行军速度提升100%。（只作用于技能生效期间出征的队伍）。</p>
							</div>
						</div>
						<n-divider />
						<div style="display: flex;">
							<n-image preview-disabled style="width: 70px; height: 70px;" :src="renderSLBZActivityImg('longZhuaShenJue')" />
							<div style="padding-left: 15px;">
								<div style="font-weight: bold; font-size: 1.25em;">龙爪深掘</div>
								<p>10分钟内，联盟成员采集龙髓水晶的速度提升50%。（技能生效时，已处于行军/采集中的队伍也会获得增益。技能效果结束后，采集队伍的增益立即消失）。</p>
							</div>
						</div>
					</n-tab-pane>
					<n-tab-pane name="其他" tab="其他">
						<h2>参与条件</h2>
						<p>联盟：赛区内所有联盟均可报名。报名阶段结束时，赛区内排名靠前的若干联盟将获得参战资格。获得参战资格的联盟数量由本赛区内的王国数量决定，王国越多，可获得参战资格的联盟越多，具体以对应赛区活动界面展示为准。获得参战资格的联盟，可在参战委派阶段选择60个联盟成员参战。</p>
						<p>个人：在报名阶段结束时所在的联盟获得了联盟参战资格，则可在委派参战阶段在该联盟申请参战。申请参战需满足个人熔炉等级条件（根据赛区分组决定）。</p>

						<h2>进入战场</h2>
						<p>进入战场后，领主城镇将出现在边域地区的随机位置。战场开启后5分钟为战场准备期，期间领主无法进行迁城、攻击、侦查、驻扎。</p>

						<h2>战斗规则</h2>
						<ol>
							<li>进入战场需要满足条件：没有部队处于侦察或出征状态、城墙不处于燃烧状态、大使馆中也没有其他领主的援军。</li>
							<li>战场中的战斗使用领主自身的士兵，可出征队列数量为领主已解锁的出征列队数量。</li>
							<li>战场中，军医所容量无上限，但治疗伤兵需正常消耗时间和资源。离开战场后，军医所将恢复原本容量，超出容量部分的伤兵保持超出状态，依旧存在于军医所中。当超出军医所容量后，新的重伤士兵将会直接死亡。</li>
							<li>进入战场后，可攻击所有非盟友的其他领主，在战场中攻击其他领主的城镇，士兵会重伤和阵亡，而攻击霜龙王城和石塔，士兵只会重伤。</li>
							<li>领主同一时间只能有一支部队参与霜龙王城和石塔的战斗。若已有部队驻守在霜龙王城或石塔中，则可继续派遣部队驻守该建筑。</li>
							<li>战场中，集结队伍出发后，参与集结队伍的所有成员均可使用集结加速道具，减少队伍行军时间。7.战场中攻击其他领主城镇获胜后不会掠夺对方资源。</li>
							<li>在战场中，城镇的燃烧速度将大幅提升。如果城镇防守失败且没有及时灭火，城镇将会强制迁移至边域的随机位置。如果城镇位于龙冢区域，防守失败将直接迁移至边域随机位置。</li>
							<li>霜龙战场允许中途离开，但完全退出战场后，需等待10分钟才能重返战场。</li>
							<li>战场中，执政官系列头衔增益、至高执政官系列头衔增益、执政官技能增益、宠物增益、城镇增益、VIP属性、个人科技属性、联盟科技属性和装扮加成属性均会正常生效。</li>
						</ol>
					</n-tab-pane>
				</n-tabs>
			</div>
			<div v-show="selectValue === 'xue_yu_bing_qi_lian_sai'">
				<n-tabs type="line" animated>
					<n-tab-pane name="赛事简介" tab="赛事简介">
						<h2>赛事背景</h2>
						<p>谁掌握了武器，谁就掌握了力量！64支劲旅，齐聚旧王朝的兵工厂之上，只为争夺至高无上的冠军奖杯！只有兼具勇气与谋略的最强者，才能获得最后的胜利。</p>

						<h2>赛事简介</h2>
						<ol>
							<li>雪域兵器联赛开启时，根据各个王国的历史进程天数，将不同的王国分配到不同的赛区，以保证赛事公平。</li>
							<li>每个赛区至多有64个军团参与赛事，赛程包括淘汰赛、争霸赛，在所有赛程结束后，将决出每个赛区的冠军军团。冠军、亚军、季军军团将永久记录在荣耀殿堂中。</li>
							<li>每个赛区报名军团数量如果少于16个，则将无法举办联赛，请积极参与报名。</li>
						</ol>

						<h2>玩法介绍</h2>
						<ol>
							<li>在【雪域兵器联赛】中，士兵不会阵亡，战场结束时，伤兵将自动痊愈。</li>
							<li>战斗打响时，配对的两个军团将进入战场，展开角逐。军团首次控制一座建筑（指一直占领直至建筑转为己方颜色）或者持续控制建筑，都可以获得联盟和个人的【军工积分】。倒计时归零时，战斗结束。拥有更多【联盟军工积分】的一方获胜。届时将有丰厚奖励，根据整体战绩和个人表现发放。</li>
							<li>若军团正在参与【雪域兵器联赛】，则该军团和该军团参赛人员无法参与【兵工厂争夺战】，从【雪域兵器联赛】中被淘汰后，可参与下一期的【兵工厂争夺战】。</li>
							<li>每轮比赛的比赛当天 UTC 0点和次日 UTC 0点，参与该轮比赛的军团，参赛人员的"战斗类"宠物技能的冷却时间将自动清空，请领主尽情享受战斗的乐趣。</li>
							<li>军团参与的每场联赛比赛，不会影响该军团所属联盟的【兵工厂争夺战】评级。</li>
							<li>开启联赛活动的王国的领主，可以观看所有赛区的比赛。</li>
							<li>报名阶段结束后，军团参赛人员名单将固定，此后退盟不影响参与联赛，但请在战场开始前回到原来的联盟，避免错过比赛。若是参赛人员，退盟后仍可收到所属军团的奖励，但无法收到原来联盟的联盟奖励。</li>
							<li>报名阶段结束到联赛活动结束期间，入围联赛的联盟无法解散。</li>
						</ol>

						<h2>流程概要</h2>
						<ol>
							<li style="margin-bottom: 30px;">
								<span>报名</span>
								<ol>
									<li>联盟盟主及4阶成员可进行联赛报名，每个联盟可以报名两个军团，报名截止后，参战名单将被锁定，无法更改。报名截止后才加入联盟的成员无法参战，且无法获得联盟参战奖励。</li>
									<li>请战：4阶以下成员可以向任意军团请战，并在报名截止前可以任意切换请战军团，但同时只能请战一个军团。</li>
									<li>根据本联赛赛区报名军团的配对分值进行排名，前64名的军团有资格参赛。</li>
									<li>配对分值由报名名单中部队战力最高的20位领主的部队战力决定。</li>
									<li>部队战力主要来源为领主装备战力、英雄装备战力、战斗类科技战力。</li>
								</ol>
							</li>
							<li style="margin-bottom: 30px;">
								<span>参战人员</span>
								<ol>
									<li>名单由盟主及4阶以上成员决定，最多可选30名参战人员和20名替补人员。每个成员只能参与一个军团（包括替补和参战）。</li>
									<li>报名阶段结束后，整个联赛期间无法再次更换参战和替补人员，请谨慎做出选择。</li>
								</ol>
							</li>
							<li style="margin-bottom: 30px;">
								<span>参赛时间</span>
								<ol>
									<li>参赛军团必须从 UTC 2点，7点，12点，14点，19点中任选3个时间作为比赛时间。</li>
									<li>报名阶段结束后，整个联赛期间无法再次修改参赛时间，请谨慎做出选择。3.3匹配到比赛对手后，系统将自动根据双方选择的比赛时间优先顺序确定本次比赛时间。</li>
								</ol>
							</li>
							<li style="margin-bottom: 30px;">
								<span>进入战场</span>
								<div>战场开启后即可进入，但须确认没有部队处于侦察或出征状态、军医所中没有伤兵、城墙不处于燃烧状态、自动狩猎不处于开启状态，且大使馆中也没有其他领主的援军。</div>
							</li>
							<li style="margin-bottom: 30px;">
								<span>战斗开始</span>
								<div>进入战场后，我方为蓝，敌方为红。</div>
							</li>
							<li style="margin-bottom: 30px;">
								<span>战斗阶段</span>
								<div>阶段1: 开放武器试验场、武器维修厂、蒸汽锅炉和中转站。</div>
								<div>阶段2: 开放皇家兵工厂、军火库和雇佣兵营地。</div>
								<div>阶段3: 地图上会随机出现武器车间。</div>
							</li>
						</ol>
						<p>战斗结束时，获得【联盟军工积分】多的一方获胜。</p>
					</n-tab-pane>
					<n-tab-pane name="赛程说明" tab="赛程说明">
						<span style="display: none;">持续23天</span>
						<h2>淘汰赛</h2>
						<ol>
							<li>淘汰赛为单败赛制，每16个参赛军团分成一个小组。小组内的军团胜者晋级下一轮，失败者会被淘汰，经过4轮比赛后，小组第1名晋级争霸赛。</li>
							<li>淘汰赛累积净胜分排行榜：根据淘汰赛期间军团累积净胜分进行排序，淘汰赛最终晋级的4个军团，前2名军团晋级争霸赛黄金组，后2名军团晋级争霸赛白银组（累积净胜分排行榜只统计淘汰赛比赛的数据，争霸赛比赛的数据不纳入统计）。</li>
							<li>军团累积净胜分为军团每场比赛的净胜分之和，以蓝方军团为例，每场比赛蓝方军团的净胜分＝本场比赛蓝方军团的联盟军工积分﹣本场比赛红方军团的联盟军工积分。</li>
							<li>比赛轮空的军团本轮获得的净胜分，为所属赛区本轮获得净胜分最高的军团的本轮净胜分。</li>
						</ol>

						<h2>争霸赛</h2>
						<ol>
							<li>争霸赛共3轮比赛，黄金组的军团，胜利后继续留在黄金组，失败后进入白银组；白银组的军团，胜利后留在白银组，失败后淘汰。</li>
							<li>最终，黄金组的第一和白银组的第一争夺联赛总冠军！</li>
						</ol>
					</n-tab-pane>
					<n-tab-pane name="建筑介绍" tab="建筑介绍">
						<n-card style="margin-bottom: 10px;">
							<div style="display: flex; padding-bottom: 10px;">
								<n-image style="width: 50px; height: 50px;" :src="renderBuildingImg('huang_jia_bing_gong_chang')" preview-disabled />
								<div style="padding-left: 10px;">
									<div style="font-size: large; font-weight: bold;">皇家兵工厂</div>
									<div>旧王朝已没落，但兵工厂仍在运转。占据了它就意味着拥有武器，以及源源不断的军工积分。</div>
								</div>
							</div>
							<n-table :bordered="false" :single-line="false">
								<thead>
									<tr>
										<th></th>
										<th>首次控制</th>
										<th>持续占领</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>联盟军工积分</td>
										<td>9000</td>
										<td>+1800/分钟</td>
									</tr>
									<tr>
										<td>个人军工积分</td>
										<td>4500</td>
										<td>+900/分钟</td>
									</tr>
								</tbody>
							</n-table>
						</n-card>
						<n-card style="margin-bottom: 10px;">
							<div style="display: flex; padding-bottom: 10px;">
								<n-image style="width: 50px; height: 50px;" :src="renderBuildingImg('wu_qi_shi_yan_chang')" preview-disabled />
								<div style="padding-left: 10px;">
									<div style="font-size: large; font-weight: bold;">1号武器试验场</div>
									<div>兵工厂生产的武器在这里接受新能检验。试验场供油量做，分别坐落于西南角和东南角</div>
								</div>
							</div>
							<n-table :bordered="false" :single-line="false">
								<thead>
									<tr>
										<th></th>
										<th>首次控制</th>
										<th>持续占领</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>联盟军工积分</td>
										<td>6000</td>
										<td>+1200/分钟</td>
									</tr>
									<tr>
										<td>个人军工积分</td>
										<td>3000</td>
										<td>+600/分钟</td>
									</tr>
								</tbody>
							</n-table>
						</n-card>
						<n-card style="margin-bottom: 10px;">
							<div style="display: flex; padding-bottom: 10px;">
								<n-image style="width: 50px; height: 50px;" :src="renderBuildingImg('wu_qi_shi_yan_chang')" preview-disabled />
								<div style="padding-left: 10px;">
									<div style="font-size: large; font-weight: bold;">2号武器试验场</div>
									<div>兵工厂生产的武器在这里接受新能检验。试验场供油量做，分别坐落于西南角和东南角</div>
								</div>
							</div>
							<n-table :bordered="false" :single-line="false">
								<thead>
									<tr>
										<th></th>
										<th>首次控制</th>
										<th>持续占领</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>联盟军工积分</td>
										<td>6000</td>
										<td>+1200/分钟</td>
									</tr>
									<tr>
										<td>个人军工积分</td>
										<td>3000</td>
										<td>+600/分钟</td>
									</tr>
								</tbody>
							</n-table>
						</n-card>
						<n-card style="margin-bottom: 10px;">
							<div style="display: flex; padding-bottom: 10px;">
								<n-image style="width: 50px; height: 50px;" :src="renderBuildingImg('wu_qi_wei_xiu_chang')" preview-disabled />
								<div style="padding-left: 10px;">
									<div style="font-size: large; font-weight: bold;">1号武器维修厂</div>
									<div>用于维修武器装备的小型工厂，共有四座，分别位于四个角落。</div>
								</div>
							</div>
							<n-table :bordered="false" :single-line="false">
								<thead>
									<tr>
										<th></th>
										<th>首次控制</th>
										<th>持续占领</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>联盟军工积分</td>
										<td>3000</td>
										<td>+600/分钟</td>
									</tr>
									<tr>
										<td>个人军工积分</td>
										<td>1500</td>
										<td>+300/分钟</td>
									</tr>
								</tbody>
							</n-table>
						</n-card>
						<n-card style="margin-bottom: 10px;">
							<div style="display: flex; padding-bottom: 10px;">
								<n-image style="width: 50px; height: 50px;" :src="renderBuildingImg('wu_qi_wei_xiu_chang')" preview-disabled />
								<div style="padding-left: 10px;">
									<div style="font-size: large; font-weight: bold;">2号武器维修厂</div>
									<div>用于维修武器装备的小型工厂，共有四座，分别位于四个角落。</div>
								</div>
							</div>
							<n-table :bordered="false" :single-line="false">
								<thead>
									<tr>
										<th></th>
										<th>首次控制</th>
										<th>持续占领</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>联盟军工积分</td>
										<td>3000</td>
										<td>+600/分钟</td>
									</tr>
									<tr>
										<td>个人军工积分</td>
										<td>1500</td>
										<td>+300/分钟</td>
									</tr>
								</tbody>
							</n-table>
						</n-card>
						<n-card style="margin-bottom: 10px;">
							<div style="display: flex; padding-bottom: 10px;">
								<n-image style="width: 50px; height: 50px;" :src="renderBuildingImg('wu_qi_wei_xiu_chang')" preview-disabled />
								<div style="padding-left: 10px;">
									<div style="font-size: large; font-weight: bold;">3号武器维修厂</div>
									<div>用于维修武器装备的小型工厂，共有四座，分别位于四个角落。</div>
								</div>
							</div>
							<n-table :bordered="false" :single-line="false">
								<thead>
									<tr>
										<th></th>
										<th>首次控制</th>
										<th>持续占领</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>联盟军工积分</td>
										<td>3000</td>
										<td>+600/分钟</td>
									</tr>
									<tr>
										<td>个人军工积分</td>
										<td>1500</td>
										<td>+300/分钟</td>
									</tr>
								</tbody>
							</n-table>
						</n-card>
						<n-card style="margin-bottom: 10px;">
							<div style="display: flex; padding-bottom: 10px;">
								<n-image style="width: 50px; height: 50px;" :src="renderBuildingImg('wu_qi_wei_xiu_chang')" preview-disabled />
								<div style="padding-left: 10px;">
									<div style="font-size: large; font-weight: bold;">4号武器维修厂</div>
									<div>用于维修武器装备的小型工厂，共有四座，分别位于四个角落。</div>
								</div>
							</div>
							<n-table :bordered="false" :single-line="false">
								<thead>
									<tr>
										<th></th>
										<th>首次控制</th>
										<th>持续占领</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>联盟军工积分</td>
										<td>3000</td>
										<td>+600/分钟</td>
									</tr>
									<tr>
										<td>个人军工积分</td>
										<td>1500</td>
										<td>+300/分钟</td>
									</tr>
								</tbody>
							</n-table>
						</n-card>
						<!-- 军火库 -->
						<n-card style="margin-bottom: 10px;">
							<div style="display: flex; padding-bottom: 10px;">
								<n-image style="width: 50px; height: 50px;" :src="renderBuildingImg('jun_huo_ku')" preview-disabled />
								<div style="padding-left: 10px;">
									<div style="font-size: large; font-weight: bold;">军火库</div>
									<div>存放各类武器装备之处，库存包括火炮和战车等，据说还保存得十分完好。控制军火库，就能提升部队的实力。</div>
								</div>
							</div>
							<n-table :bordered="false" :single-line="false">
								<thead>
									<tr>
										<th></th>
										<th>首次控制</th>
										<th>持续占领</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>联盟军工积分</td>
										<td>120</td>
										<td>+240/分钟</td>
									</tr>
									<tr>
										<td>个人军工积分</td>
										<td>600</td>
										<td>+120/分钟</td>
									</tr>
								</tbody>
							</n-table>
							<div style="padding: 5px 8px; background-color: #a6c0f0; border-radius: 8px; color: black; display: flex;">
								<div style="padding-right: 20px;">额外效果</div>
								<div>部队伤害值提高: +15%、部队受到的伤害值降低: -15%</div>
							</div>
						</n-card>
						<!-- 雇佣兵营地 -->
						<n-card style="margin-bottom: 10px;">
							<div style="display: flex; padding-bottom: 10px;">
								<n-image style="width: 50px; height: 50px;" :src="renderBuildingImg('gu_yong_bing_ying_di')" preview-disabled />
								<div style="padding-left: 10px;">
									<div style="font-size: large; font-weight: bold;">雇佣兵营地</div>
									<div>嗅到战争与财富气息的佣兵驻扎于此。控制营地后，可派遣强有力的佣兵攻打敌方占领的建筑，降低敌方攻击力和防御力。佣兵的攻势一波更胜一波，强度最多可提升4次。</div>
								</div>
							</div>
							<n-table :bordered="false" :single-line="false">
								<thead>
									<tr>
										<th></th>
										<th>首次控制</th>
										<th>持续占领</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>联盟军工积分</td>
										<td>1200</td>
										<td>+240/分钟</td>
									</tr>
									<tr>
										<td>个人军工积分</td>
										<td>600</td>
										<td>+120/分钟</td>
									</tr>
								</tbody>
							</n-table>
						</n-card>
						<!-- 中转站 -->
						<n-card style="margin-bottom: 10px;">
							<div style="display: flex; padding-bottom: 10px;">
								<n-image style="width: 50px; height: 50px;" :src="renderBuildingImg('zhong_zhuan_zhan')" preview-disabled />
								<div style="padding-left: 10px;">
									<div style="font-size: large; font-weight: bold;">中转站</div>
									<div>兵工厂及其周边区域的枢纽。控制中转站可以缩短免费高级迁城次数的恢复时间。</div>
								</div>
							</div>
							<n-table :bordered="false" :single-line="false">
								<thead>
									<tr>
										<th></th>
										<th>首次控制</th>
										<th>持续占领</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>联盟军工积分</td>
										<td>1200</td>
										<td>+240/分钟</td>
									</tr>
									<tr>
										<td>个人军工积分</td>
										<td>600</td>
										<td>+120/分钟</td>
									</tr>
								</tbody>
							</n-table>
							<div style="padding: 5px 8px; background-color: #a6c0f0; border-radius: 8px; color: black; display: flex;">
								<div style="padding-right: 20px;">额外效果</div>
								<div>缩短迁城冷却时间: -50%</div>
							</div>
						</n-card>
						<!-- 蒸汽锅炉 -->
						<n-card style="margin-bottom: 10px;">
							<div style="display: flex; padding-bottom: 10px;">
								<n-image style="width: 50px; height: 50px;" :src="renderBuildingImg('zheng_qi_guo_lu')" preview-disabled />
								<div style="padding-left: 10px;">
									<div style="font-size: large; font-weight: bold;">蒸汽锅炉</div>
									<div>运转中的蒸汽锅炉，能提升军工积分的产出效率。控制蒸汽锅炉，可获得额外的增益。</div>
								</div>
							</div>
							<n-table :bordered="false" :single-line="false">
								<thead>
									<tr>
										<th></th>
										<th>首次控制</th>
										<th>持续占领</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>联盟军工积分</td>
										<td>1200</td>
										<td>+240/分钟</td>
									</tr>
									<tr>
										<td>个人军工积分</td>
										<td>600</td>
										<td>+120/分钟</td>
									</tr>
								</tbody>
							</n-table>
							<div style="padding: 5px 8px; background-color: #a6c0f0; border-radius: 8px; color: black; display: flex;">
								<div style="padding-right: 20px;">额外效果</div>
								<div>减少控制所需时间: -50%</div>
							</div>
						</n-card>
					</n-tab-pane>
					<n-tab-pane name="其他" tab="其他">
						<h2>参战条件</h2>
						<ol>
							<li>
								<span>联盟</span>
								<ol>
									<li>所有联盟均可报名雪域兵器联赛。</li>
									<li>第一军团默认解锁，解锁第二军团需要联盟6级及以上，且本周联盟成员累计登录达到40人，成员退出联盟会影响计数。</li>
									<li>军团报名参战者和替补的总人数需要达到15人，才能进入匹配。两个军团报名人数各自独立计算。</li>
								</ol>
							</li>
							<li>
								<span>个人</span>
								<ol>
									<li>联盟报名阶段截止前已加入，且大熔炉等级不低于16级。</li>
									<li>成员离线5天及以上将无法被委派，若委派后离线超过规定时间则不影响该成员参与。</li>
								</ol>
							</li>
						</ol>

						<h2>战斗</h2>
						<p>在【雪域兵器联赛】中占领或控制建筑，能够获得联盟和个人的【军工积分】，部分建筑还能提供不同的增益。</p>
						<p>在防守建筑时每击败士兵实力总和为10,000的部队，将获得40点【个人军工积分】，但不获得【联盟军工积分】；在进攻建筑时，每击败士兵实力总和为10,000的部队，将获得80点【个人军工积分】，同样不获得【联盟军工积分】。</p>
						<p>战斗开始，参战者将获得1次免费的【高级迁城】,使用后进入冷却，冷却结束后恢复次数。此外，也可以消耗【高级迁城】道具进行迁城。</p>
						<p>战场中的部队不会阵亡，只会进入战场军医所。战场军医所容量无上限，治疗伤兵也不消耗资源。离开战场时，战场军医所中的所有伤兵都将恢复。</p>
						<p>在战场中，建筑燃烧的速度将大幅提升。如果城镇防守失败且没有及时灭火，城镇会被强制移至安全区。如果在战斗过程中离开战场，将进入冷却状态，12分钟后才能重返战场。</p>
						<p>科技、联盟科技、 VIP 、领主装备、城市增益道具、装扮加成效果、宠物技能、王国官职加成都能够战场中生效。</p>

						<h2>联赛排名规则</h2>
						<ol>
							<li>冠军军团：争霸赛第3轮获胜军团。</li>
							<li>亚军军团：争霸赛第3轮落败军团。</li>
							<li>季军军团：争霸赛第2轮落败军团。</li>
							<li>殿军军团：争霸赛第1轮﹣白银组落败军团。</li>
							<li>第5-8名军团：淘汰赛第4轮落败军团，按照淘汰赛期间军团累积净胜分从高到低进行排名；若累积净胜分相同，按照报名时军团部队战力从高到低进行排名。</li>
							<li>第9-16名军团：淘汰赛第3轮落败军团，按照淘汰赛期间军团累积净胜分从高到低进行排名；若累积净胜分相同，按照报名时军团部队战力从高到低进行排名。</li>
							<li>第17-32名军团：淘汰赛第2轮落败军团，按照淘汰赛期间军团累积净胜分从高到低进行排名；若累积净胜分相同，按照报名时军团部队战力从高到低进行排名。</li>
							<li>第33-64名军团：淘汰赛第1轮落败军团，按照淘汰赛期间军团累积净胜分从高到低进行排名；若累积净胜分相同，按照报名时军团部队战力从高到低进行排名。</li>
						</ol>

						<h2>重赛章程</h2>
						<ol>
							<li>若非服务器或游戏发生严重事故，比赛结果将被视为最终结果。</li>
							<li>受严重事故所影响的比赛，赛事单位有权在比赛结束后24小时之内安排重赛，并通过游戏内邮件发出重赛通知，重赛时间预设在该轮比赛次日的原本比赛时段进行，原本比赛的成绩将被清除。</li>
							<li>当赛事单位发出重赛通知后，军团需要在指定时间参与重赛。无法全员到场的情况下，赛事单位不另外提供重赛机会。</li>
							<li>
								<span>重赛相关处理：</span>
								<ol>
									<li>领主参与竞猜事故比赛所消耗的比赛竞猜券，将全部返还给领主，同时竞猜历史、竞猜排行榜将不会统计事故比赛的竞猜数据。</li>
									<li>淘汰赛﹣累积净胜分排行榜、联赛战绩、荣耀殿堂不会统计事故比赛的数据。</li>
									<li>返还参与事故比赛消耗的全部道具和资源，包括：高级迁城、行军加速器、出征召回、侦察消耗的资源、城墙灭火消耗的钻石、治疗伤兵消耗的加速道具和钻石。</li>
									<li>返还事故比赛的双方参赛人员，在战场开始前1小时﹣战场结束期间消耗的全部"战争类"增益道具。</li>
									<li>事故比赛结束后，获胜军团新解锁的联赛联盟荣耀将被回收，包括联盟总部外观、联盟旗帜外观、联赛荣誉建筑、联赛旗帜。</li>
									<li>因事故比赛产生的奖励，不会回收。</li>
								</ol>
							</li>
						</ol>
					</n-tab-pane>
				</n-tabs>
			</div>
		</n-layout-content>
	</n-layout>
</template>

<script setup>
import { ref, onMounted } from "vue";

import allActivities from "@/data/activitys.json";

const selectOptions = ref([]);
const selectValue = ref();

const handleUpdateValue = (value, option) => {
	selectValue.value = value;
}

const renderBuildingImg = (name) => {
	const imgUrl = `${import.meta.env.BASE_URL}images/${name}.png`;
    return new URL(imgUrl, import.meta.url).href;
}

const renderActivityImg = (name) => {
	const imgUrl = `${import.meta.env.BASE_URL}images/activity/xueYuBingQiLianSai/${name}.png`;
    return new URL(imgUrl, import.meta.url).href;
}

const renderSLBZActivityImg = (name) => {
	const imgUrl = `${import.meta.env.BASE_URL}images/activity/shuangLongBaZhu/${name}.png`;
    return new URL(imgUrl, import.meta.url).href;
}

onMounted(() => {
	allActivities.forEach(item => selectOptions.value.push({ label: item.name, value: item.key }));
	selectValue.value = selectOptions.value.at(0).value;
})
</script>

<style scoped>
/* 重置默认列表样式 */
ol {
	list-style: none;
	counter-reset: item;
	padding-left: 0;
}

ol > li {
	counter-increment: item;
	margin-bottom: 0.5em;
}

/* 主序号：1, 2, 3... */
ol > li::before {
	content: counters(item, ".") "、";
	font-weight: bold;
}

/* 嵌套的 ol，用于实现 1.1, 1.2... */
ol ol {
	counter-reset: subitem;
	margin-left: 1em;
}

ol ol > li {
	counter-increment: subitem;
}

/* 嵌套项的编号：1.1, 1.2... */
ol ol > li::before {
	content: counters(item, ".") "." counters(subitem, "") "、";
}
</style>