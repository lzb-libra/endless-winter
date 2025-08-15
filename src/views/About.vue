<template>
  <div class="timeline-main">
    <n-timeline>
      <n-timeline-item v-for="(item, index) in uplogs" type="info" :content="item.content" :key="index"
        :time="item.time" line-type="dashed" />
    </n-timeline>
  </div>
</template>

<script setup>
const uplogs = [
  { content: '增加专家页面', time: '2025-08-13' },
  { content: '增加鲁弗斯专武和专武技能的图片', time: '2025-08-10' },
  { content: '增加部分英雄的专武图片和CG动画', time: '2025-08-03' },
  { content: '增加部分英雄背景故事', time: '2025-08-01' },
  { content: '增加部分英雄数据', time: '2025-07-31' },
  { content: '调整英雄页面展示结构，增加部分英雄数据', time: '2025-07-27' },
  { content: '项目初始化', time: '2025-07-22' },
]
</script>

<style lang="css">
.timeline-main {
  margin-top: 100px;
  margin-left: 20%;
  margin-bottom: 5%;
  overflow-y: hidden;
}
</style>