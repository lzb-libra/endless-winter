<template>
  <div class="timeline-main">
    <n-timeline style="width: 100%;">
      <n-timeline-item v-for="(item, index) in uplogs" type="info" :content="item.content" :key="index" :time="item.time" line-type="dashed" style="width: 100%;" />
    </n-timeline>
  </div>
</template>

<script setup>
const uplogs = [
  { content: '增加西里尔、艾格妮丝、罗幕路斯、霍尔格四个专家的游戏数据', time: '2025-08-24' },
  { content: '增加鲁弗斯专武和专武技能的图片', time: '2025-08-10' },
  { content: '增加部分赫罗尼莫、娜塔莉亚、茉莉、津曼、阿隆索的CG动画', time: '2025-08-03' },
  { content: '增加部分英雄背景故事', time: '2025-08-01' },
  { content: '增加部分英雄数据', time: '2025-07-31' },
  { content: '调整英雄页面展示结构，增加部分英雄数据', time: '2025-07-27' },
  { content: '项目初始化', time: '2025-07-22' },
]
</script>

<style lang="css">
.timeline-main {
  width: 100%;
  margin-top: 100px;
  margin-bottom: 5%;
  margin-left: 20%;
  overflow-y: hidden;
}
</style>