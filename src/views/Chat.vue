<template>
  <n-grid x-gap="10" y-gap="10" cols="1 xl:2" responsive="screen">
    <n-gi>
      <div ref="yzAttackRef" class="chat_main"></div>
    </n-gi>
    <n-gi>
      <div ref="yzDefenseRef" class="chat_main"></div>
    </n-gi>
    <n-gi>
      <div ref="attackRef" class="chat_main"></div>
    </n-gi>
    <n-gi>
      <div ref="defenseRef" class="chat_main"></div>
    </n-gi>
    <n-gi>
      <div ref="healthRef" class="chat_main"></div>
    </n-gi>
  </n-grid>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import * as echarts from 'echarts'

import allHero from "@/data/heros.json";

const yzAttackRef = ref(null);
let yzAttackInstance = null;

const yzDefenseRef = ref(null);
let yzDefenseInstance = null;

const attackRef = ref(null);
let attackInstance = null;

const defenseRef = ref(null);
let defenseInstance = null;

const healthRef = ref(null);
let healthInstance = null;

const loreHeros = allHero.filter(item => item.addr.startsWith('lore') && !item.addr.endsWith('HeLuoNiMo')).sort((a, b) => a.id - b.id);

const initYzAttackChart = () => {
  if (!yzAttackRef.value) return;

  const dun = loreHeros.filter(item => item.as === 1).map(item => item.skill.data[3]);
  const mao = loreHeros.filter(item => item.as === 2).map(item => item.skill.data[3]);
  const she = loreHeros.filter(item => item.as === 3).map(item => item.skill.data[3]);

  yzAttackInstance = echarts.init(yzAttackRef.value)
  const option = {
    title: {
      text: '各代兵种远征攻击趋势图',
    },
    tooltip: {
      trigger: 'axis',
    },
    legend: {
      data: ['盾兵', '矛兵', '弓兵'],
    },
    xAxis: {
      type: 'category',
      data: ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        name: '盾兵',
        type: 'line',
        data: dun,
      },
      {
        name: '矛兵',
        type: 'line',
        data: mao,
      },
      {
        name: '弓兵',
        type: 'line',
        data: she,
      }
    ],
  }

  yzAttackInstance.setOption(option)
}

const initYzDefenseChart = () => {
  if (!yzDefenseRef.value) return;

  const dun = loreHeros.filter(item => item.as === 1).map(item => item.skill.data[3]);
  const mao = loreHeros.filter(item => item.as === 2).map(item => item.skill.data[3]);
  const she = loreHeros.filter(item => item.as === 3).map(item => item.skill.data[3]);

  yzDefenseInstance = echarts.init(yzDefenseRef.value)
  const option = {
    title: {
      text: '各代兵种远征防御趋势图',
    },
    tooltip: {
      trigger: 'axis',
    },
    legend: {
      data: ['盾兵', '矛兵', '弓兵'],
    },
    xAxis: {
      type: 'category',
      data: ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        name: '盾兵',
        type: 'line',
        data: dun,
      },
      {
        name: '矛兵',
        type: 'line',
        data: mao,
      },
      {
        name: '弓兵',
        type: 'line',
        data: she,
      }
    ],
  }

  yzDefenseInstance.setOption(option)
}


const initAttackChart = () => {
  if (!attackRef.value) return;

  const dun = loreHeros.filter(item => item.as === 1).map(item => item.skill.data[0]);
  const mao = loreHeros.filter(item => item.as === 2).map(item => item.skill.data[0]);
  const she = loreHeros.filter(item => item.as === 3).map(item => item.skill.data[0]);

  attackInstance = echarts.init(attackRef.value)
  const option = {
    title: {
      text: '各代兵种探险攻击趋势图',
    },
    tooltip: {
      trigger: 'axis',
    },
    legend: {
      data: ['盾兵', '矛兵', '弓兵'],
    },
    xAxis: {
      type: 'category',
      data: ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        name: '盾兵',
        type: 'line',
        data: dun,
      },
      {
        name: '矛兵',
        type: 'line',
        data: mao,
      },
      {
        name: '弓兵',
        type: 'line',
        data: she,
      }
    ],
  }

  attackInstance.setOption(option)
}

const initDefenseChart = () => {
  if (!defenseRef.value) return;

  const dun = loreHeros.filter(item => item.as === 1).map(item => item.skill.data[1]);
  const mao = loreHeros.filter(item => item.as === 2).map(item => item.skill.data[1]);
  const she = loreHeros.filter(item => item.as === 3).map(item => item.skill.data[1]);

  defenseInstance = echarts.init(defenseRef.value)
  const option = {
    title: {
      text: '各代兵种远探险御趋势图',
    },
    tooltip: {
      trigger: 'axis',
    },
    legend: {
      data: ['盾兵', '矛兵', '弓兵'],
    },
    xAxis: {
      type: 'category',
      data: ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        name: '盾兵',
        type: 'line',
        data: dun,
      },
      {
        name: '矛兵',
        type: 'line',
        data: mao,
      },
      {
        name: '弓兵',
        type: 'line',
        data: she,
      }
    ],
  }

  defenseInstance.setOption(option)
}

const initHealthChart = () => {
  if (!healthRef.value) return;

  const dun = loreHeros.filter(item => item.as === 1).map(item => item.skill.data[2]);
  const mao = loreHeros.filter(item => item.as === 2).map(item => item.skill.data[2]);
  const she = loreHeros.filter(item => item.as === 3).map(item => item.skill.data[2]);

  healthInstance = echarts.init(healthRef.value)
  const option = {
    title: {
      text: '各代兵种探险生命趋势图',
    },
    tooltip: {
      trigger: 'axis',
    },
    legend: {
      data: ['盾兵', '矛兵', '弓兵'],
    },
    xAxis: {
      type: 'category',
      data: ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        name: '盾兵',
        type: 'line',
        data: dun,
      },
      {
        name: '矛兵',
        type: 'line',
        data: mao,
      },
      {
        name: '弓兵',
        type: 'line',
        data: she,
      }
    ],
  }

  healthInstance.setOption(option)
}

onMounted(() => {
  initYzAttackChart();
  initYzDefenseChart();
  initAttackChart();
  initDefenseChart();
  initHealthChart();
})

onUnmounted(() => {
  if (yzAttackInstance) {
    yzAttackInstance.dispose()
    yzAttackInstance = null
  }

  if (yzDefenseInstance) {
    yzDefenseInstance.dispose()
    yzDefenseInstance = null
  }

  if (attackInstance) {
    attackInstance.dispose()
    attackInstance = null
  }

  if (defenseInstance) {
    defenseInstance.dispose()
    defenseInstance = null
  }

  if (healthInstance) {
    healthInstance.dispose()
    healthInstance = null
  }
})

</script>

<style lang="css">
.chat_main {
  width: 100vw;
  height: 400px;
}

@media (min-width: 2048px) { 
  .chat_main {
    width: 50vw;
    height: 400px;
  }
}
</style>