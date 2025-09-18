<template>
    <div class="hero_detail_main">
        <div style="display: flex; justify-content: center;">
            <img :src="renderPortrait()" class="hero_portrait_img" />
            <div style="padding-left: 20px;">
                <div class="hero_base_info">
                    <div style="padding-right: 10px;">{{ detail.name }}</div>
                    <div style="padding-bottom: 10px;">
                        <n-tag v-if="detail.level === 'rare'" size="small" :color="{ textColor: '#4d99b9', borderColor: '#4d99b9', fontSize: '0.8em' }">稀有</n-tag>
                        <n-tag v-else-if="detail.level === 'epic'" size="small" :color="{ textColor: '#db8efe', borderColor: '#db8efe', fontSize: '0.8em' }">史诗</n-tag>
                        <n-tag v-else size="small" :color="{ textColor: '#f7cb50',  borderColor: '#f7cb50', fontSize: '0.8em' }">{{ detail.level }}</n-tag>
                    </div>
                </div>
                <div>
                    <img v-if="detail.as === 1" src="/images/as-hypaspist.png" style="width: 30px" />
                    <img v-else-if="detail.as === 2" src="/images/as-spearman.png" style="width: 30px" />
                    <img v-else="detail.as === 3" src="/images/as-archers.png" style="width: 30px" />
                    <img v-if="detail.type == 1" src="/images/type-output.png" style="width: 30px" />
                    <img v-else="detail.type == 1" src="/images/type-develop.png" style="width: 30px" />
                </div>
            </div>
        </div>
        <n-card title="英雄来源" style="margin-top: 10px;" v-if="detail.source">
            <n-space>
                <n-tag v-for="(item, index) in detail.source" :key="index" type="success" style="font-size: 0.8em;">{{ item }}</n-tag>
            </n-space>
        </n-card>
        <n-card title="英雄故事" style="margin-top: 10px;" v-if="detail.story">
            <n-ellipsis expand-trigger="click" line-clamp="3" :tooltip="false">
                <p v-html="detail.story"></p>
            </n-ellipsis>
        </n-card>
        <n-card title="英雄天赋" style="margin-top: 10px;" v-if="detail.talent">
            <div style="display: flex; align-items: center;">
                <img :src="renderTalent()" style="width: 30px;" />
                <div style="font-weight: bold; font-size: 1.25em; padding-top: 3px; padding-left: 5px;">{{ detail.talent.name }}</div>
            </div>
            <div>
                <p style="font-weight: bold; font-size: 1.25em"></p>
                <p>{{ detail.talent.desc }}</p>
            </div>
        </n-card>
        <n-card title="英雄技能" style="margin-top: 10px;" v-if="detail.skill">
            <div>
                <p class="hero_skill_label">探险</p>
                <div v-if="detail.skill.data">英雄攻击: {{ detail.skill.data[0] || 0 }}</div>
                <div v-if="detail.skill.data">英雄防御: {{ detail.skill.data[1] || 0 }}</div>
                <div v-if="detail.skill.data">英雄生命: {{ detail.skill.data[2] || 0 }}</div>
                <div class="hero_skill_item" v-if="detail.skill.tx_1">
                    <img :src="renderTxSkillImg(1)" class="hero_skill_item_img" />
                    <div class="hero_skill_item_body">
                        <div class="hero_skill_item_body_label">{{ detail.skill.tx_1.label }}</div>
                        <div>{{ detail.skill.tx_1.desc }}</div>
                    </div>
                </div>
                <div class="hero_skill_item" v-if="detail.skill.tx_2">
                    <img :src="renderTxSkillImg(2)" class="hero_skill_item_img" />
                    <div class="hero_skill_item_body">
                        <div class="hero_skill_item_body_label">{{ detail.skill.tx_2.label }}</div>
                        <div>{{ detail.skill.tx_2.desc }}</div>
                    </div>
                </div>
                <div class="hero_skill_item"  v-if="detail.skill.tx_3">
                    <img :src="renderTxSkillImg(3)" class="hero_skill_item_img" />
                    <div class="hero_skill_item_body">
                        <div class="hero_skill_item_body_label">{{ detail.skill.tx_3.label }}</div>
                        <div>{{ detail.skill.tx_3.desc }}</div>
                    </div>
                </div>
            </div>
            <div style="padding-top: 25px;">
                <p class="hero_skill_label">远征</p>
                <div v-if="detail.skill.data">{{`${detail.as === 1 ? "盾" : detail.as === 2 ? "矛" : "弓"}兵攻击力: +${detail.skill.data[3] || 0}%` }}</div>
                <div v-if="detail.skill.data">{{ `${detail.as === 1 ? "盾" : detail.as === 2 ? "矛" : "弓"}兵防御力: +${detail.skill.data[4] || 0}%` }}</div>
                <div class="hero_skill_item" v-if="detail.skill.yz_1">
                    <img :src="renderYzSkillImg(1)" class="hero_skill_item_img" />
                    <div class="hero_skill_item_body">
                        <div class="hero_skill_item_body_label">{{ detail.skill.yz_1.label }}</div>
                        <div>{{ detail.skill.yz_1.desc }}</div>
                    </div>
                </div>
                <div class="hero_skill_item" v-if="detail.skill.yz_2">
                    <img :src="renderYzSkillImg(2)" class="hero_skill_item_img" />
                    <div class="hero_skill_item_body">
                        <div class="hero_skill_item_body_label">{{ detail.skill.yz_2.label }}</div>
                        <div>{{ detail.skill.yz_2.desc }}</div>
                    </div>
                </div>
                <div class="hero_skill_item" v-if="detail.skill.yz_3">
                    <img :src="renderYzSkillImg(3)" class="hero_skill_item_img" />
                    <div class="hero_skill_item_body">
                        <div class="hero_skill_item_body_label">{{ detail.skill.yz_3.label }}</div>
                        <div>{{ detail.skill.yz_3.desc }}</div>
                    </div>
                </div>
            </div>
        </n-card>
        <n-card title="英雄专武" style="margin-top: 10px;" v-if="detail.weapon">
            <div style="display: flex; align-items: center;">
                <img class="hero_wwapon_img" :src="renderZwImg()" />
                <div style="padding-left: 20px;">
                    <div style="font-size: 1.3em; font-weight: bold;">{{ detail.weapon.name }}</div>
                    <div style="display: flex; align-items: center;">
                        <img src="/images/strength.png" style="width: 15px; height: 15px;" />
                        <span style="padding-left: 3px;">{{ detail.weapon.strength }}</span>
                    </div>
                </div>
            </div>
            <div style="padding-top: 10px;">
                <div class="hero_weapon_datum">
                    <div>
                        <div>英雄攻击: {{ detail.weapon.data[0] }}</div>
                        <div>英雄防御: {{ detail.weapon.data[1] }}</div>
                        <div>英雄生命: {{ detail.weapon.data[2] }}</div>
                    </div>
                    <div>
                        <div>护卫攻击: {{ detail.weapon.data[3] }}</div>
                        <div>护卫防御: {{ detail.weapon.data[4] }}</div>
                        <div>护卫生命: {{ detail.weapon.data[5] }}</div>
                    </div>
                </div>
                <div>{{ detail.as === 1 ? "盾兵" : detail.as === 2 ? "矛兵" : "射手" }}杀伤力: +{{ detail.weapon.data[6] }}%</div>
                <div>{{ detail.as === 1 ? "盾兵" : detail.as === 2 ? "矛兵" : "射手" }}生命值: +{{ detail.weapon.data[7] }}%</div>
            </div>
            <div style="margin-top: 10px;">
                <div class="hero_skill_item" v-if="detail.skill.tx_1">
                    <div>
                        <img :src="renderZwTxImg()" class="hero_skill_item_img" />
                        <div style="text-align: center">探险</div>
                    </div>
                    <div class="hero_skill_item_body">
                        <div class="hero_skill_item_body_label">{{ detail.weapon.tx.name }} Lv5</div>
                        <div>{{ detail.weapon.tx.desc }}</div>
                    </div>
                </div>
                <div class="hero_skill_item" v-if="detail.skill.tx_1">
                    <div>
                        <img :src="renderZwYzImg()" class="hero_skill_item_img" />
                        <div style="text-align: center">远征</div>
                    </div>
                    <div class="hero_skill_item_body">
                        <div class="hero_skill_item_body_label">{{ detail.weapon.yz.name }} Lv5</div>
                        <div>{{ detail.weapon.yz.desc }}</div>
                    </div>
                </div>
            </div>
        </n-card>
    </div>
</template>

<script setup>
import { onBeforeMount, onMounted, ref } from "vue";
import { useRoute } from 'vue-router';

import allHeroDatum from "@/data/heros.json";
import { color } from "echarts";

const route = useRoute();

const detail = ref({});

const renderPortrait = () => {
	const imgUrl = `${import.meta.env.BASE_URL}images/heros/${detail.value.addr}/portrait.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderTalent = () => {
	const imgUrl = `${import.meta.env.BASE_URL}images/heros/${detail.value.addr}/tf.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderTxSkillImg = (index) => {
    const imgUrl = `${import.meta.env.BASE_URL}images/heros/${detail.value.addr}/tx_${index}.png`;
	return new URL(imgUrl, import.meta.url).href;
}

const renderYzSkillImg = (index) => {
    const imgUrl = `${import.meta.env.BASE_URL}images/heros/${detail.value.addr}/yz_${index}.png`;
	return new URL(imgUrl, import.meta.url).href;
}

const renderZwImg = () => {
	const imgUrl = `${import.meta.env.BASE_URL}images/heros/${detail.value.addr}/zw.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderZwTxImg = () => {
	const imgUrl = `${import.meta.env.BASE_URL}images/heros/${detail.value.addr}/zw-tx.png`;
	return new URL(imgUrl, import.meta.url).href;
};

const renderZwYzImg = () => {
	const imgUrl = `${import.meta.env.BASE_URL}images/heros/${detail.value.addr}/zw-yz.png`;
	return new URL(imgUrl, import.meta.url).href;
};

onBeforeMount(() => {
    detail.value = allHeroDatum.find(item => item.id === Number(route.params.id));
})

onMounted(() => {
    
});
</script>

<style scoped>
.hero_detail_main {
    width: 100%;
    padding-top: 2vh;
}

.hero_portrait {
    display: flex;
    justify-content: center;
}

.hero_base_info {
    font-size: 1.5em; 
    display: flex; 
    align-items: center;
}

.hero_portrait_img {
    width: 35%;
    height: 35%;
}

.hero_skill_label {
    font-size: 1.2em;
}

.hero_skill_item {
    display: flex; 
    padding-top: 10px;
}

.hero_skill_item_img {
    width: 50px; 
    height: 50px;
}

.hero_skill_item_body {
    flex: 1; 
    padding-left: 10px;
}

.hero_skill_item_body_label {
    font-size: 1.25em; 
    font-weight: bold
}

.hero_wwapon_img {
    width: 20vw; 
    height: 20vw;
}

.hero_weapon_datum {
    display: flex; 
    justify-content: space-between; 
    margin-bottom: 10px;
}

/* 中等屏幕（平板等） */
@media (min-width: 1024px) {
  	.hero-card-main {
		width: calc(20vw - 35px); 
		cursor: pointer;
	}

    .hero_wwapon_img {
        width: 5vw; 
        height: 5vw;
    }
}

/* 大屏幕（桌面等） */
@media (min-width: 1900px) {
  	.hero-card-main {
		width: calc(10vw - 14.6px); 
		cursor: pointer;
	}

    .hero_base_info {
        font-size: 2em;
    }

    .hero_portrait_img {
        width: 20%;
        height: 20%;
    }

    .hero_wwapon_img {
        width: 3vw; 
        height: 3vw;
    }

    .hero_weapon_datum {
        display: flex; 
        justify-content: unset;
        margin-bottom: 10px;
    }

    .hero_weapon_datum > div:last-of-type {
        padding-left: 100px;
    }
}
</style>