<template>
  <div class="timeline-main">
    <n-timeline style="width: 100%;">
      <n-timeline-item v-for="(item, index) in uplogs" type="info" :content="item.content" :key="index" :time="item.time" line-type="dashed" style="width: 100%;" />
    </n-timeline>
  </div>
</template>

<script setup>
const uplogs = [
  { content: '增加S15英雄的信息。增加一个新专家“瓦莱莉亚”', time: '2026-01-05' },
  { content: '增加S14英雄的专武信息。增加两个新专家“法比安”和“巴尔德”', time: '2025-10-27' },
  { content: '增加S14英雄的信息', time: '2025-10-13' },
  { content: '修改英雄页面和宠物页面倒叙展示', time: '2025-09-14' },
  { content: '修改各个页面的部分布局使其能够在手机上能够正常访问', time: '2025-09-14' },
  { content: '修改英雄和宠物页面的布局，使其在手机端也可以正常浏览', time: '2025-09-06' },
  { content: '补充S8、S9英雄故事一和故事二。调整宠物布局', time: '2025-08-31' },
  { content: '补充S8、S9英雄专武技能图片和说明', time: '2025-08-30' },
  { content: '增加各代英雄一些数值的图表展示', time: '2025-08-26' },
  { content: '增加活动“霜龙霸主”和“雪域兵器联赛”的规则说明', time: '2025-08-25' },
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
  margin-top: 5vh;
}
</style>