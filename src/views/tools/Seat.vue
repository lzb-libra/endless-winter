<template>
  <div>
    <div style="display: flex; padding-bottom: 10px;">
      <n-upload :default-upload="false" :multiple="true" :show-retry-button="true" :show-file-list="false" accept="image/*"
        v-model:file-list="fileList" @change="handleUploadChange" style="width: 100px;">
        <n-button>上传图片</n-button>
      </n-upload>
      <n-button @click="showPlayerSeatChart">座位图</n-button>
      <n-upload :default-upload="false" :multiple="true" :show-retry-button="true" :show-file-list="false" accept=".json"
        v-model:file-list="fileList" @change="handleUploadChange" style="width: 100px;">
        <n-button>导入配置</n-button>
      </n-upload>
      <n-button @click="exportToJSON">导出配置</n-button>
    </div>
    <div style="display: flex; align-items: center; padding-bottom: 10px;">
      <n-progress style="flex: 1;" type="line" :percentage="percentage" indicator-placement="inside" />
      <span style="padding-left: 10px;">{{ count }} / {{ fileList.length }}</span>
    </div>
    <n-data-table :columns="columns" :data="tableData" :pagination="false" style="height: 1000px;"
          @update:sorter="handleSorterChange" :key="row => row.key" :bordered="false" flex-height striped />

    <n-modal v-model:show="showTableDetailModal" style="width: 800px;">
      <n-card>
        <div style="display: flex; justify-content: space-between;">
          <n-form
            ref="formRef"
            :model="showTableDetail"
            label-placement="left"
            label-width="auto"
            require-mark-placement="right-hanging"
            size="medium"
          >
            <n-form-item label="角色名称" path="name">
              <n-input v-model:value="showTableDetail.name" />
            </n-form-item>
            <n-form-item label="盾兵攻击力" path="dbgjl">
              <n-input v-model:value="showTableDetail.dbgjl" type="number" />
            </n-form-item>
            <n-form-item label="盾兵防御力" path="dbfyl">
              <n-input v-model:value="showTableDetail.dbfyl" type="number" />
            </n-form-item>
            <n-form-item label="盾兵穿透力" path="dbctl">
              <n-input v-model:value="showTableDetail.dbctl" type="number" />
            </n-form-item>
            <n-form-item label="盾兵生命力" path="dbsml">
              <n-input v-model:value="showTableDetail.dbsml" type="number" />
            </n-form-item>
            <n-form-item label="矛兵攻击力" path="mbgjl">
              <n-input v-model:value="showTableDetail.mbgjl" type="number" />
            </n-form-item>
            <n-form-item label="矛兵防御力" path="mbfyl">
              <n-input v-model:value="showTableDetail.mbfyl" type="number" />
            </n-form-item>
            <n-form-item label="矛兵穿透力" path="mbctl">
              <n-input v-model:value="showTableDetail.mbctl" type="number" />
            </n-form-item>
            <n-form-item label="矛兵生命力" path="mbsml">
              <n-input v-model:value="showTableDetail.mbsml" type="number" />
            </n-form-item>
            <n-form-item label="射手攻击力" path="ssgjl">
              <n-input v-model:value="showTableDetail.ssgjl" type="number" />
            </n-form-item>
            <n-form-item label="射手防御力" path="ssfyl">
              <n-input v-model:value="showTableDetail.ssfyl" type="number" />
            </n-form-item>
            <n-form-item label="射手穿透力" path="sssml">
              <n-input v-model:value="showTableDetail.sssml" type="number" />
            </n-form-item>
            <n-form-item label="射手生命力" path="sssml">
              <n-input v-model:value="showTableDetail.sssml" type="number" />
            </n-form-item>
          </n-form>
          <img :src="showTableDetail.imgUrl" style="width: 430px; height: 730px; margin-left: 20px;">
        </div>
      </n-card>
    </n-modal>

    <n-modal
      v-model:show="showSeatCanvasModal"
      style="width: 90vw; height: 100vh;"
    >
      <n-card>
        123
      </n-card>
    </n-modal>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, h } from 'vue';
import { createWorker } from 'tesseract.js';
import { NButton, useMessage } from 'naive-ui';

const message = useMessage();

const timerId = setInterval(() => {
  if(pendingDatum.value.size > 0 && !pendingStatus.value) recognizeImg();
}, 1000);

const columns = [
  {
    title: '名称',
    key: "name",
    render(row) {
      return h('a',
        {
          size: 'small',
          onClick: () => {
            showTableDetail.value = row;
            showTableDetailModal.value = true;
          },
          style: {
            cursor: 'pointer'
          }
        },
        row.name
      );
    }
  },
  {
    title: '盾兵攻击力',
    key: "dbgjl",
    sorter: 'default'
  },
  {
    title: '盾兵防御力',
    key: "dbfyl",
    sorter: 'default'
  },
  {
    title: '盾兵穿透力',
    key: "dbctl",
    sorter: 'default'
  },
  {
    title: '盾兵生命力',
    key: "dbsml",
    sorter: 'default'
  },
  {
    title: '矛兵攻击力',
    key: "mbgjl",
    sorter: 'default'
  },
  {
    title: '矛兵防御力',
    key: "mbfyl",
    sorter: 'default'
  },
  {
    title: '矛兵穿透力',
    key: "mbctl",
    sorter: 'default'
  },
  {
    title: '矛兵生命力',
    key: "mbsml",
    sorter: 'default'
  },
  {
    title: '射手攻击力',
    key: "ssgjl",
    sorter: 'default'
  },
  {
    title: '射手防御力',
    key: "ssfyl",
    sorter: 'default'
  },
  {
    title: '射手穿透力',
    key: "ssctl",
    sorter: 'default'
  },
  {
    title: '射手生命力',
    key: "sssml",
    sorter: 'default'
  }
]

// 表格数据
const tableData = ref([
  // {"name":"请","dbgjl":579.8,"dbfyl":583.9,"dbctl":382.6,"dbsml":343,"mbgjl":634.6,"mbfyl":648.1,"mbctl":512.2,"mbsml":445.9,"ssgjl":578.6,"ssfyl":577.8,"ssctl":333.3,"sssml":283.2,"fileId":"60763a05"}
]);
// 上传的文件对象
const fileList = ref([]);
// 识别数量
const count = ref(0);
// 识别进度
const percentage = ref(0);
// 当前是否正在OCR
const pendingStatus = ref(false);
// 待处理OCR识别的数据
const pendingDatum = ref(new Map());
// 玩家详情信息
const showTableDetail = ref({});
// 是否玩家详情信息弹窗
const showTableDetailModal = ref(false);
// 是否显示座位图
const showSeatCanvasModal = ref(false);

// 表格排序触发的函数
const handleSorterChange = (sorter) => {
  console.log(sorter);
  // if (sorter.order === false) {
  //   seatDatum.value = [...tableData.value];
  // } else {
  //   seatDatum.value = [...tableData.value].sort((a, b) => {
  //     const valA = Number(a[sorter.columnKey]);
  //     const valB = Number(b[sorter.columnKey]);

  //     if (isNaN(valA)) return 1;
  //     if (isNaN(valB)) return -1;

  //     return sorter.order === 'descend' ? valB - valA : valA - valB;
  //   });
  // }
};

// 图片上传
const handleUploadChange = async (fielInfo) => {
  console.log(fielInfo)

  // showModal.value = true;
  const imgFile = fielInfo.file.file;

  const img = new Image()
  img.src = URL.createObjectURL(imgFile)

  img.onload = async () => {
    // 创建离屏 Canvas
    const offCanvas = document.createElement('canvas');
    const ctx = offCanvas.getContext('2d');
    offCanvas.width = img.width;
    offCanvas.height = img.height;
    ctx.drawImage(img, 0, 0);

    // 灰度化处理
    const imageData = ctx.getImageData(0, 0, img.width, img.height);
    const data = imageData.data;
    for (let i = 0; i < data.length; i += 4) {
      const gray = 0.299 * data[i] + 0.587 * data[i + 1] + 0.114 * data[i + 2];
      data[i] = data[i + 1] = data[i + 2] = gray;
    }
    ctx.putImageData(imageData, 0, 0);

    // OCR识别
    const info = new Map();
    info.set('canvas', offCanvas);
    info.set('file', imgFile);
    pendingDatum.value.set(fielInfo.file.id, info);
  }
}

// OCR识图 - 识别文字
const recognizeImg = async () => {
  pendingStatus.value = true;

  const key = pendingDatum.value.keys().next().value;
  const obj = pendingDatum.value.get(key);

  console.log("正在识别: " + obj.get('file').name);

  const worker = await createWorker({
    workerPath: window.location.origin + import.meta.env.BASE_URL + '/tesseract/worker.min.js',
    langPath: window.location.origin + import.meta.env.BASE_URL + '/lang-data',
    gzip: false,
  });
  await worker.loadLanguage('chi_sim_fast');
  await worker.initialize('chi_sim_fast');
  const { data: result } = await worker.recognize(obj.get('canvas'))

  const playerData = parsePlayerData(result, obj.get('file'));
  if(playerData) {
    const reader = new FileReader();
    reader.onload = (e) => {
      playerData['imgUrl'] = e.target.result;
      playerData['imgId'] = key;
    
      tableData.value.push(playerData);
      // seatDatum.value = [...tableData.value];

      count.value++;
      percentage.value = ((count.value / fileList.value.length) * 100).toFixed(0);

      // drawSeat();
    }
    reader.readAsDataURL(obj.get('file'));
  }

  pendingDatum.value.delete(key)

  pendingStatus.value = false;
}

// OCR识图 - 解析文字
const parsePlayerData = (result, file) => {
  console.log(result)

  const playerData = {};
  const lines = result.text.split(/\r?\n/);
  for (const item of lines) {
    if(!playerData['name'] && (item.includes('QGD') || item.includes('FUN'))) {
      let cleaned = item.replace(/^.*?【QGD】/i, '').replace(/^.*?【FUN】/i, '');
      cleaned = cleaned.replace(/^.*?\[QGD\]/i, '').replace(/^.*?\[FUN\]/i, '');
      cleaned = cleaned.split(' ').filter(item => item.trim() !== '');
      playerData['name'] = cleaned[0];
    }
    if(!playerData['name']) playerData['name'] = file.name.replace('.png', '');

    if (item.includes('盾兵攻')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['dbgjl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
    }
    if (item.includes('盾兵防')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['dbfyl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
    }
    if (item.includes('盾兵穿')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['dbctl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
    }
    if (item.includes('盾兵生')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['dbsml'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
    }

    if (item.includes('矛兵攻')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['mbgjl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
    }
    if (item.includes('矛兵防')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['mbfyl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
    }
    if (item.includes('矛兵穿')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['mbctl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
    }
    if (item.includes('矛兵生')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['mbsml'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
    }

    if (item.includes('射手攻')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['ssgjl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
    }
    if (item.includes('射手防')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['ssfyl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
    }
    if (item.includes('射手穿')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['ssctl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
    }
    if (item.includes('射手生')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['sssml'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
    }
  }

  return playerData;
}

// 展示座位布局图
const showPlayerSeatChart = () => {
  if(tableData.value.length === 0) {
    message.warning("请先上传玩家数据!!!");
    return;
  }

  showSeatCanvasModal.value = true;
}

// 导出配置文件
const exportToJSON = () => {
  const jsonString = JSON.stringify(tableData.value, null, 2);
  const blob = new Blob([jsonString], { type: 'application/json' });
  const url = URL.createObjectURL(blob);

  const timestamp = new Date().toISOString().slice(0, 19).replace(/:/g, '-');
  const filename = `export-data-${timestamp}.json`;

  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

onMounted(async () => {});

onUnmounted(async () => { 
  clearInterval(timerId);
});
</script>

<style scoped></style>