<template>
    <n-layout has-sider>
        <n-layout-sider content-style="padding: 24px;">
          <n-menu :options="menuOptions" @update:value="handleUpdateValue" default-value="shuang_long_ba_zhu" />
        </n-layout-sider>
        <n-layout-content content-style="padding-left: 24px;">
            <div style="display: flex;" v-for="(item, index) in allExpertDatum" :key="index">
                <div>
                    <n-image
                        width="200"
                        src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
                    />
                    <div style="text-align: center;">
                        {{ item.name }}
                    </div>
                    <n-card title="天赋" style="margin-top: 10px;">
                        <div style="display: flex;">
                            <n-image
                                width="50"
                                src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
                            />
                            <div>
                                <div style="font-size: 1.5em;">{{ item.talent.name }}</div>
                                <div>{{ item.talent.desc }}</div>
                            </div>
                        </div>
                    </n-card>
                    <n-card title="技能" style="margin-top: 10px;">
                        <div style="display: flex; margin-top: 20px;" v-for="(item2, index2) in item.skill" :key="index2">
                            <n-image
                                width="50"
                                src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
                            />
                            <div>
                                <div style="font-size: 1.5em;">{{ item2.name }}</div>
                                <div>{{ item2.desc }}</div>
                            </div>
                        </div>
                    </n-card>
                </div>
                <n-card title="好感度" style="margin-left: 10px; width: 35%;">
                    <n-timeline>
                        <n-timeline-item
                            v-for="(item3, index3) in item.likability"
                            :key="index3"
                            :title="item3.level"
                            type="warning">
                            <template #default>
                                <div style="display: flex;">
                                    <n-image
                                        width="50"
                                        src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
                                    />
                                    <div style="padding-left: 10px;">
                                        <div>{{ item3.effect }}</div>
                                        <div>天赋等级提升</div>
                                    </div>
                                </div>
                            </template>
                        </n-timeline-item>
                    </n-timeline>
                </n-card>
            </div>
        </n-layout-content>
    </n-layout>
</template>

<script setup>
import allExpertDatum from "../data/expert.json";

const menuOptions = ref([]);
for (const item of allExpertDatum) {
  menuOptions.value.push({label: item.name, key: item.key})
}
</script>