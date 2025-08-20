<template>
    <n-layout has-sider>
        <n-layout-sider content-style="padding: 8px;">
            <n-menu v-model:value="menuDefaultValue" :options="menuOptions" @update:value="handleUpdateValue"
                responsive />
        </n-layout-sider>
        <n-layout-content content-style="padding-left: 24px;">
            <n-flex :vertical="false">
                <div style="width: 59%;">
                    <div style="display: flex;">
                        <div>
                            <n-image width="400" src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg" />
                            <div
                                style="text-align: center; display: flex; align-items: center; justify-content: center;">
                                <span style="padding-right: 5px;">{{ showExpertDetail.name }}</span>
                                <n-image width="10" src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
                                    preview-disabled />
                            </div>
                        </div>
                        <n-card title="天赋">
                            <div style="display: flex;">
                                <n-image width="50" src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
                                    preview-disabled />
                                <div>
                                    <div style="font-size: 1.3em;">
                                        {{ showExpertDetail.talent?.name }}
                                    </div>
                                    <div>{{ showExpertDetail.talent?.desc }}</div>
                                </div>
                            </div>
                        </n-card>
                    </div>

                    <n-card title="技能" style="margin-top: 10px;">
                        <div style="display: flex; margin-top: 20px;" v-for="(item2, index2) in showExpertDetail.skill"
                            :key="index2">
                            <n-image width="100" src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
                                preview-disabled />
                            <div>
                                <div style="font-size: 1.3em;">{{ item2.name }}</div>
                                <div>{{ item2.desc }}</div>
                            </div>
                        </div>
                    </n-card>
                </div>
                <n-card title="好感度" style="width: 40%;">
                    <n-timeline>
                        <n-timeline-item v-for="(item3, index3) in showExpertDetail.likability" :key="index3"
                            :title="item3.level" type="warning">
                            <template #default>
                                <div style="display: flex;">
                                    <n-image width="50" src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
                                        preview-disabled />
                                    <div style="padding-left: 10px;">
                                        <div>{{ item3.effect }}</div>
                                        <div>天赋等级提升</div>
                                    </div>
                                </div>
                            </template>
                        </n-timeline-item>
                    </n-timeline>
                </n-card>
            </n-flex>
        </n-layout-content>
    </n-layout>
</template>

<script setup>
import { onMounted, ref } from "vue";
import allExpertDatum from "@/data/expert.json";

const menuOptions = ref([]);
const menuDefaultValue = ref('');
const showExpertDetail = ref({});

const handleUpdateValue = (key) => {
    console.log(key)
}

onMounted(() => {
    allExpertDatum.forEach(item => menuOptions.value.push({ label: item.name, key: item.key }));

    menuDefaultValue.value = menuOptions.value.at(0).key;
    showExpertDetail.value = allExpertDatum[0];
});
</script>