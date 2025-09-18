<template>
    <n-layout>
        <n-layout-header style="padding: 10px 0;">
			<n-select v-model:value="selectValue" :options="selectOptions" @update:value="handleUpdateValue" />
		</n-layout-header>
        <n-grid x-gap="10" y-gap="10" cols="1 xl:2" responsive="screen">
            <n-gi>
                <div style="display: flex;">
                    <n-image class="expert_portrait_img" :src="renderPortrait()" preview-disabled />
                </div>
                <div>
                    <n-card style="margin-bottom: 12px; height: 100%;">
                        <div style="display: flex;">
                            <div>
                                <n-image class="expert_avatar_img" :src="renderAvatar()" preview-disabled />
                            </div>
                            <div style="padding-left: 20px;">
                                <div class="expert_name">{{ showExpertDetail.name }}</div>
                                <div style="display: flex; align-items: center; padding-top: 10px;">
                                    <n-image width="25" :src="renderType()" preview-disabled />
                                    <span style="font-size: large; padding-left: 10px;">{{ showExpertDetail.type }}</span>
                                </div>
                            </div>
                        </div>
                        <n-divider />
                        <div style="padding-top: 20px;">
                            <div style="font-size: 1.5em; font-weight: bolder;">远征</div>
                            <div style="padding-top: 12px;">
                                <div style="display: flex; justify-content: space-between; width: 100%;" v-for="(item, index) in showExpertDetail.yz" :key="index">
                                    <div>{{item.desc}}</div>
                                    <div>{{ item.effect }}</div>
                                </div>
                            </div>
                        </div>
                        <n-divider />
                        <div style="padding-top: 20px;">
                            <div>
                                <div style="font-size: 1.5em; font-weight: bolder;">天赋</div>
                                <div></div>
                            </div>
                            <div style="display: flex; padding-top: 12px;">
                                <n-image style="width: 80px; height: 80px;" :src="renderTalent()" preview-disabled />
                                <div style="padding-left: 20px;">
                                    <div style="font-size: 1.3em; font-weight: bold;">
                                        {{ showExpertDetail.talent?.name }}
                                    </div>
                                    <div>{{ showExpertDetail.talent?.desc }}</div>
                                </div>
                            </div>
                        </div>
                        <n-divider />
                        <div style="padding-top: 20px;">
                            <div style="font-size: 1.5em; font-weight: bolder;">技能</div>
                            <div style="display: flex; margin-top: 35px;" v-for="(item2, index2) in showExpertDetail.skill" :key="index2">
                                <n-image style="width: 80px; height: 80px;" :src="renderSkill(index2)" preview-disabled />
                                <div style="padding-left: 12px;">
                                    <div style="font-size: 1.3em;">{{ item2.name }}</div>
                                    <div>{{ item2.desc }}</div>
                                </div>
                            </div>
                        </div>
                        <n-divider v-if="showExpertDetail.treasureChest" />
                        <div v-if="showExpertDetail.treasureChest" style="padding-top: 20px;">
                            <div style="font-size: 1.5em; font-weight: bolder;">{{ showExpertDetail.treasureChest.name }}</div>
                            <div  v-for="(item, index) in showExpertDetail.treasureChest.reward" :key="index" style="display: flex; justify-content: space-between;">
                                <div>{{ item.article }}</div>
                                <div>{{ item.probability }}</div>
                            </div>
                        </div>
                    </n-card>
                </div>
            </n-gi>
            <n-gi>
                <n-card title="好感度">
                    <n-timeline>
                        <n-timeline-item v-for="(item3, index3) in showExpertDetail.likability" :key="index3" type="warning">
                            <template #header>
                                <div style="font-size: large; font-weight: bold;">Lv {{ item3.level }} {{ item3.desc }}</div>
                            </template>
                            <template #default>
                                <div style="display: flex; margin-top: 20px; border-radius: 10px;">
                                    <div style="background: linear-gradient(to right, #ff7e5f, #feb47b); padding: 15px; border-top-left-radius: 9px; border-bottom-left-radius: 9px;">
                                        <n-image class="expert_likability_img" :src="renderLikabilityIcon(item3)" preview-disabled />
                                    </div>
                                    <div style="padding-left: 10px; display: flex; flex-direction: column; justify-content: center; font-size: large; padding-left: 20px; background-color: bisque; width: 100%; color: black; border-top-right-radius: 9px; border-bottom-right-radius: 9px;">
                                        <div v-html="item3.effect"></div>
                                        <div style="padding-top: 16px;">天赋等级提升</div>
                                    </div>
                                </div>
                            </template>
                        </n-timeline-item>
                    </n-timeline>
                </n-card>
            </n-gi>
        </n-grid>
    </n-layout>
</template>

<script setup>
import { onMounted, ref } from "vue";
import allExpertDatum from "@/data/expert.json";

const selectValue = ref('');
const selectOptions = ref([]);
const showExpertDetail = ref({});

const handleUpdateValue = (value, option) => {
    selectValue.value = value;
    showExpertDetail.value = allExpertDatum.find(item => item.key == value);
}

const renderPortrait = () => {
    if(!showExpertDetail.value) return;

    const imgUrl = `${import.meta.env.BASE_URL}images/expert/${showExpertDetail.value.key}/portrait.png`;
    return new URL(imgUrl, import.meta.url).href;
}

const renderAvatar = () => {
    if(!showExpertDetail.value) return;

    const imgUrl = `${import.meta.env.BASE_URL}images/expert/${showExpertDetail.value.key}/avatar.png`;
    return new URL(imgUrl, import.meta.url).href;
}

const renderType = () => {
    if(!showExpertDetail.value) return;

    const imgUrl = `${import.meta.env.BASE_URL}images/expert/${showExpertDetail.value.key}/type.png`;
    return new URL(imgUrl, import.meta.url).href;
}

const renderTalent = () => {
    if(!showExpertDetail.value) return;

    const imgUrl = `${import.meta.env.BASE_URL}images/expert/${showExpertDetail.value.key}/talent.png`;
    return new URL(imgUrl, import.meta.url).href;
}

const renderSkill = (index) => {
    if(!showExpertDetail.value) return;

    const imgUrl = `${import.meta.env.BASE_URL}images/expert/${showExpertDetail.value.key}/skill_${index + 1}.png`;
    return new URL(imgUrl, import.meta.url).href;
}

const renderLikabilityIcon = (item) => {
    if(!showExpertDetail.value) return;

    if(item.level === '1' || item.level === '10' || item.level === '20' || item.level === '30' || item.level === '40') {
        const imgUrl = `${import.meta.env.BASE_URL}images/expert/likability_${item.level}_icon.png`;
        return new URL(imgUrl, import.meta.url).href;
    } else {
        const imgUrl = `${import.meta.env.BASE_URL}images/expert/likability_1_icon.png`;
        return new URL(imgUrl, import.meta.url).href;
    }
}

onMounted(() => {
    allExpertDatum.forEach(item => selectOptions.value.push({ label: item.name, value: item.key }));
    selectValue.value = selectOptions.value[0].value;
    showExpertDetail.value = allExpertDatum.find(item => item.key == selectValue.value);
});
</script>

<style scoped>
.expert_portrait_img {
    height: 200px;
    margin: 20px auto;
}

.expert_avatar_img {
    width: 80px;
    height: 80px;
}

.expert_name {
    font-size: 1.5em;
    font-weight: bolder;
}

.expert_likability_img {
    width: 50px;
    height: 50px;
}

@media (min-width: 640px) { 
	
}

@media (min-width: 1024px) {
  	
}

@media (min-width: 2048px) {
    .expert_portrait_img {
        height: 400px;
        margin: 20px auto;
    }

    .expert_avatar_img {
        width: 120px;
        height: 120px;
    }

    .expert_name {
        font-size: 2.5em;
    }

  	.expert_likability_img {
        width: 80px;
        height: 80px;
    }
}
</style>