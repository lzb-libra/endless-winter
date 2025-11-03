<template>
  <div class="main">
    <div class="left">
      <canvas ref="seatCanvas" :width="canvasWidth" :height="canvasHeight"></canvas>
    </div>
    <div class="right">
      <div style="display: flex; margin-bottom: 10px;">
        <n-upload :default-upload="false" :multiple="false" :show-retry-button="true" :show-file-list="false"
          v-model:file-list="fileList" @change="handleUploadChange">
          <n-button>上传文件</n-button>
        </n-upload>
        <n-button @click="showModal = !showModal">玩家数据</n-button>
      </div>
      <div>
        <n-input placeholder="搜索" style="margin-bottom: 8px;" @input="inputChange" clearable />
        <div v-if="fileList.length > 0" style="display: flex; align-items: center; margin-bottom: 10px; display: none;">
          <n-progress style="flex: 1;" type="line" :percentage="percentage" indicator-placement="inside" />
          <span style="padding-left: 10px;">{{ count }} / {{ fileList.length }}</span>
        </div>
        <n-list hoverable clickable>
          <n-list-item v-for="obj in seatDatum" @click="locatePlayerPosition(obj)">
            <div style="display: flex;">
              <div v-if="selectedPlayer && selectedPlayer.name === obj.name" style="padding-right: 10px;">✅</div>
              <div>{{ obj.name }}</div>
            </div>
          </n-list-item>
        </n-list>
      </div>
    </div>
  </div>
  <n-modal v-model:show="showModal">
    <n-card style="width: 80vw; height: 83vh;" title="玩家数据" :bordered="false" size="huge" role="dialog"
      aria-modal="true">
      <n-data-table :style="{ height: `${height}px` }" :columns="columns" :data="tableData" :pagination="false"
        @update:sorter="handleSorterChange" :key="row => row.key" :bordered="false" flex-height striped />
    </n-card>
  </n-modal>

</template>

<script setup>
import { ref, onMounted, onUnmounted, defineComponent, h } from 'vue';
import { createWorker } from 'tesseract.js';

const columns = [
  {
    title: '名称',
    key: "name",
    render(row) {
      const index = getDataIndex(row.key);
      return h(ShowOrEdit, {
        value: row.name,
        onUpdateValue(v) {
          tableData.value[index].name = v;
        }
      });
    }
  },
  {
    title: '盾兵攻击力',
    key: "dbgjl",
    sorter: 'default',
    render(row) {
      const index = getDataIndex(row.key);
      return h(ShowOrEdit, {
        value: row.dbgjl,
        onUpdateValue(v) {
          tableData.value[index].dbgjl = v;
        }
      });
    }
  },
  {
    title: '盾兵防御力',
    key: "dbfyl",
    sorter: 'default',
    render(row) {
      const index = getDataIndex(row.key);
      return h(ShowOrEdit, {
        value: row.dbfyl,
        onUpdateValue(v) {
          tableData.value[index].dbfyl = v;
        }
      });
    }
  },
  {
    title: '盾兵穿透力',
    key: "dbctl",
    sorter: 'default',
    render(row) {
      const index = getDataIndex(row.key);
      return h(ShowOrEdit, {
        value: row.dbctl,
        onUpdateValue(v) {
          tableData.value[index].dbctl = v;
        }
      });
    }
  },
  {
    title: '盾兵生命力',
    key: "dbsml",
    sorter: 'default',
    render(row) {
      const index = getDataIndex(row.key);
      return h(ShowOrEdit, {
        value: row.dbsml,
        onUpdateValue(v) {
          tableData.value[index].dbsml = v;
        }
      });
    }
  },
  {
    title: '矛兵攻击力',
    key: "mbgjl",
    sorter: 'default',
    render(row) {
      const index = getDataIndex(row.key);
      return h(ShowOrEdit, {
        value: row.mbgjl,
        onUpdateValue(v) {
          tableData.value[index].mbgjl = v;
        }
      });
    }
  },
  {
    title: '矛兵防御力',
    key: "mbfyl",
    sorter: 'default',
    render(row) {
      const index = getDataIndex(row.key);
      return h(ShowOrEdit, {
        value: row.mbfyl,
        onUpdateValue(v) {
          tableData.value[index].mbfyl = v;
        }
      });
    }
  },
  {
    title: '矛兵穿透力',
    key: "mbctl",
    sorter: 'default',
    render(row) {
      const index = getDataIndex(row.key);
      return h(ShowOrEdit, {
        value: row.mbctl,
        onUpdateValue(v) {
          tableData.value[index].mbctl = v;
        }
      });
    }
  },
  {
    title: '矛兵生命力',
    key: "mbsml",
    sorter: 'default',
    render(row) {
      const index = getDataIndex(row.key);
      return h(ShowOrEdit, {
        value: row.mbsml,
        onUpdateValue(v) {
          tableData.value[index].mbsml = v;
        }
      });
    }
  },
  {
    title: '射手攻击力',
    key: "ssgjl",
    sorter: 'default',
    render(row) {
      const index = getDataIndex(row.key);
      return h(ShowOrEdit, {
        value: row.ssgjl,
        onUpdateValue(v) {
          tableData.value[index].ssgjl = v;
        }
      });
    }
  },
  {
    title: '射手防御力',
    key: "ssfyl",
    sorter: 'default',
    render(row) {
      const index = getDataIndex(row.key);
      return h(ShowOrEdit, {
        value: row.ssfyl,
        onUpdateValue(v) {
          tableData.value[index].ssfyl = v;
        }
      });
    }
  },
  {
    title: '射手穿透力',
    key: "ssctl",
    sorter: 'default',
    render(row) {
      const index = getDataIndex(row.key);
      return h(ShowOrEdit, {
        value: row.ssctl,
        onUpdateValue(v) {
          tableData.value[index].ssctl = v;
        }
      });
    }
  },
  {
    title: '射手生命力',
    key: "sssml",
    sorter: 'default',
    render(row) {
      const index = getDataIndex(row.key);
      return h(ShowOrEdit, {
        value: row.sssml,
        onUpdateValue(v) {
          tableData.value[index].sssml = v;
        }
      });
    }
  }
]

const seatKey = new Map([
  ['north', new Map([
    ['0', [5, 1, 9, 25, 45, 61]],
    ['1', [17, 13, 21, 29, 53, 65]],
    ['2', [37, 33, 41, 49, 57, 69]],
  ])],
  ['east', new Map([
    ['0', [6, 2, 10, 26, 46, 62]],
    ['1', [18, 14, 22, 30, 54, 66]],
    ['2', [38, 34, 42, 50, 58, 70]],
  ])],
  ['south', new Map([
    ['0', [7, 3, 11, 27, 47, 63]],
    ['1', [19, 15, 23, 31, 55, 67]],
    ['2', [39, 35, 43, 51, 59, 71]],
  ])],
  ['west', new Map([
    ['0', [8, 4, 12, 28, 48, 64]],
    ['1', [20, 16, 24, 32, 56, 68]],
    ['2', [40, 36, 44, 52, 60, 72]],
  ])],
]);

const font = '12px Arial';

// 画布大小
const canvasWidth = 1800;
const canvasHeight = 1065;

let scale = 1.0;          // 当前缩放比例
let originX = 0;          // 当前平移偏移X
let originY = 0;          // 当前平移偏移Y
const scaleStep = 0.1;    // 每次滚轮缩放步长
const minScale = 0.5;     // 最小缩放倍数
const maxScale = 3;       // 最大缩放倍数

// 网格参数
const gridSize = 50;           // 每个格子的宽高（像素）
const gridColor = '#ddd';        // 网格线颜色
const lineWidth = 1;          // 网格线宽度

// 3x3 方框参数
const boxGridWidth = 3;
const boxGridHeight = 3;
const boxBackgroundColor = '#e3f2fd';  // 浅蓝色背景（可自定义，如 '#f0f0f0'、'#cce7ff' 等）
const boxText = '🐻';                 // 你想要显示的文字，比如 "A1", "座位1", "🪑"
const boxTextColor = '#000';           // 文字颜色
const boxTextSize = 64;                 // 文字字号（像素）

// 作为数据
const seatCanvas = ref(null);

// 玩家数据
const count = ref(0);
const fileList = ref([]);
const percentage = ref(0);
const showModal = ref(false);
const selectedPlayer = ref(null);
const height = ref(window.innerHeight * 0.7);
const tableData = ref([]);
const seatDatum = ref([]);

const pendingStatus = ref(false)
const pendingDatum = ref(new Map());

const ShowOrEdit = defineComponent({
  props: {
    value: [String, Number],
    onUpdateValue: [Function, Array]
  },
  setup(props) {
    const isEdit = ref(false);
    const inputRef = ref(null);
    const inputValue = ref(props.value);
    function handleOnClick() {
      isEdit.value = true;
      nextTick(() => {
        inputRef.value?.focus();
      });
    }
    function handleChange() {
      props.onUpdateValue?.(String(inputValue.value));
      isEdit.value = false;
    }
    return () => h(
      "div",
      {
        style: "min-height: 22px",
        onClick: handleOnClick
      },
      isEdit.value ? h(NInput, {
        ref: inputRef,
        value: String(inputValue.value),
        onUpdateValue: (v) => {
          inputValue.value = v;
        },
        onChange: handleChange,
        onBlur: handleChange
      }) : props.value
    );
  }
});

const inputChange = (val) => {
  console.log(val)
}

const locatePlayerPosition = (obj) => {
  if(!selectedPlayer.value || (selectedPlayer.value && selectedPlayer.value.name !== obj.name)) {
    selectedPlayer.value = obj;
  } else if(selectedPlayer.value && selectedPlayer.value.name === obj.name) {
    selectedPlayer.value = null;
  }
  
  drawSeat();
}

// 排序
const handleSorterChange = (sorter) => {
  if (sorter.order === false) {
    seatDatum.value = [...tableData.value];
  } else {
    seatDatum.value = [...tableData.value].sort((a, b) => {
      const valA = Number(a[sorter.columnKey]);
      const valB = Number(b[sorter.columnKey]);

      if (isNaN(valA)) return 1;
      if (isNaN(valB)) return -1;

      return sorter.order === 'descend' ? valB - valA : valA - valB;
    });
  }

  drawSeat();
};

const getDataIndex = (key) => {
  return tableData.value.findIndex((item) => item.key === key);
};

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

    const info = new Map();
    info.set('canvas', offCanvas);
    info.set('file', imgFile);
    pendingDatum.value.set(fielInfo.file.id, info);
  }
}

const drawSeat = () => {
  const canvas = seatCanvas.value
  if (!canvas) return

  const ctx = canvas.getContext('2d')
  if (!ctx) return

  ctx.clearRect(0, 0, canvas.width, canvas.height)

  // ============================
  // 绘制网格
  // ============================
  ctx.strokeStyle = gridColor
  ctx.lineWidth = lineWidth

  // 绘制垂直线
  for (let x = 0; x <= canvas.width; x += gridSize) {
    ctx.beginPath()
    ctx.moveTo(x, 0)
    ctx.lineTo(x, canvas.height)
    ctx.stroke()
  }

  // 绘制水平线
  for (let y = 0; y <= canvas.height; y += gridSize) {
    ctx.beginPath()
    ctx.moveTo(0, y)
    ctx.lineTo(canvas.width, y)
    ctx.stroke()
  }

  // ============================
  // 绘制 3x3 的方框（精准对齐网格）
  // ============================
  const boxWidth = boxGridWidth * gridSize     // 3 * 40 = 120
  const boxHeight = boxGridHeight * gridSize   // 3 * 40 = 120

  // 画布中心点坐标
  const canvasCenterX = canvas.width / 2
  const canvasCenterY = canvas.height / 2

  const gridStepX = gridSize
  const gridStepY = gridSize

  const desiredCenterX = canvasCenterX
  const desiredCenterY = canvasCenterY

  const desiredLeft = desiredCenterX - boxWidth / 2
  const desiredTop = desiredCenterY - boxHeight / 2

  const alignedLeft = Math.round(desiredLeft / gridStepX) * gridStepX
  const alignedTop = Math.round(desiredTop / gridStepY) * gridStepY

  const boxLeft = alignedLeft
  const boxTop = alignedTop

  // 1. 填充方框背景色
  ctx.fillStyle = boxBackgroundColor
  ctx.fillRect(boxLeft, boxTop, boxWidth, boxHeight)

  // 2. 在方框内部居中绘制文字
  ctx.fillStyle = boxTextColor
  ctx.font = `${boxTextSize}px Arial` // 字体大小与类型
  ctx.textAlign = 'center'           // 水平居中
  ctx.textBaseline = 'middle'        // 垂直居中
  const textX = boxLeft + boxWidth / 2
  const textY = boxTop + boxHeight / 2

  ctx.fillText(boxText, textX, textY + 5)

  // ============================
  // 绘制 1x1 的方框（精准对齐网格）
  // ============================
  const startGridX = Math.floor(boxLeft / gridSize)
  const startGridY = Math.floor(boxTop / gridSize)

  const smallBoxes = [
    { x: startGridX - 1, y: startGridY - 1 }, // 左上
    { x: startGridX + 3, y: startGridY - 1 }, // 右上
    { x: startGridX - 1, y: startGridY + 3 }, // 左下
    { x: startGridX + 3, y: startGridY + 3 }, // 右下
  ]

  smallBoxes.forEach(({ x, y }) => {
    const pixelX = x * gridSize
    const pixelY = y * gridSize

    // 背景
    ctx.fillStyle = "#66bb6a"
    ctx.fillRect(pixelX, pixelY, gridSize, gridSize)

    const text = '🚩'
    ctx.font = '32px Arial' // 字号和字体（可调整，如 '14px sans-serif'）
    ctx.textAlign = 'center' // 水平居中
    ctx.textBaseline = 'middle' // 垂直居中
    const textX = pixelX + gridSize / 2
    const textY = pixelY + gridSize / 2

    ctx.fillText(text, textX, textY)
  })

  // ============================
  // 绘制 2x2 的方框
  // ============================
  // 北环
  const oneRingNorthSeat = [-1, 1, 3, 5, 7, 9];
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < oneRingNorthSeat.length; j++) {
      const value = oneRingNorthSeat[j]
      let seatX = (startGridX + value) * gridSize;
      let seatY = (startGridY - (3 + (i * 2))) * gridSize;

      drawPlayerSeat(ctx, 'north', seatX, seatY, i, j)
    }
  }

  // 东环
  const oneRingEastSeat = [-1, 1, 3, 5, 7, 9];
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < oneRingEastSeat.length; j++) {
      const value = oneRingEastSeat[j]
      let seatX = (startGridX + (4 + (i * 2))) * gridSize;
      let seatY = (startGridY + value) * gridSize;

      drawPlayerSeat(ctx, 'east', seatX, seatY, i, j)
    }
  }

  // 南环
  const oneRingSouthSeat = [2, 0, -2, -4, -6, -8];
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < oneRingSouthSeat.length; j++) {
      const value = oneRingSouthSeat[j]
      let seatX = (startGridX + value) * gridSize;
      let seatY = (startGridY + (4 + (i * 2))) * gridSize;

      drawPlayerSeat(ctx, 'south', seatX, seatY, i, j)
    }
  }

  // 西环
  const oneRingWestSeat = [2, 0, -2, -4, -6, -8];
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < oneRingWestSeat.length; j++) {
      const value = oneRingWestSeat[j]
      let seatX = (startGridX - (3 + (i * 2))) * gridSize;
      let seatY = (startGridY + value) * gridSize;

      drawPlayerSeat(ctx, 'west', seatX, seatY, i, j)
    }
  }
}

const drawPlayerSeat = (ctx, key, seatX, seatY, i, j) => {
  const keys = seatKey.get(key);
  let label = keys.get(i + "")[j];

  if (seatDatum.value.length >= label) {
    label = seatDatum.value[label - 1].name
  }

  ctx.fillStyle = label === selectedPlayer.value?.name ? "#f00": "#fff"
  ctx.fillRect(seatX, seatY, gridSize * 2, gridSize * 2)

  ctx.lineWidth = 1
  ctx.strokeStyle = label === selectedPlayer.value?.name ? "#f00" : "#000"
  ctx.strokeRect(seatX, seatY, gridSize * 2, gridSize * 2)

  ctx.font = font
  ctx.textAlign = 'center'
  ctx.textBaseline = 'middle'
  ctx.fillStyle = 'black'
  let labelX = seatX + gridSize
  let labelY = seatY + gridSize

  label = label.length > 6 ? label.substring(0, 6) + "..." : label;
  ctx.fillText(label, labelX, labelY)
}

// 在组件挂载后绘制
onMounted(async () => {
  drawSeat();

  seatCanvas.value.addEventListener('wheel', (event) => {
    event.preventDefault();

    const canvas = seatCanvas.value
    if (!canvas) return

    const ctx = canvas.getContext('2d')
    if (!ctx) return

    // 计算鼠标相对 canvas 的坐标
    const rect = canvas.getBoundingClientRect();
    const mouseX = event.clientX - rect.left;
    const mouseY = event.clientY - rect.top;

    // 滚轮方向
    const delta = event.deltaY < 0 ? 1 : -1;

    // 新的缩放比例
    const newScale = Math.min(Math.max(scale + delta * scaleStep, minScale), maxScale);

    // 保持鼠标位置在缩放后仍指向相同内容
    originX = mouseX - ((mouseX - originX) * (newScale / scale));
    originY = mouseY - ((mouseY - originY) * (newScale / scale));

    scale = newScale;

    // 清空画布
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // 应用缩放和平移
    ctx.save();
    ctx.setTransform(scale, 0, 0, scale, originX, originY);

    drawSeat(); // 重新绘制

    ctx.restore();
  })
});

// OCR识图 - 1
const recognizeImg = async () => {
  pendingStatus.value = true;

  const firstKey = pendingDatum.value.keys().next().value;
  const obj = pendingDatum.value.get(firstKey);

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
    tableData.value.push(playerData);
    seatDatum.value = [...tableData.value];

    count.value++;
    percentage.value = ((count.value / fileList.value.length) * 100).toFixed(0);

    drawSeat();
  }

  pendingDatum.value.delete(firstKey)

  pendingStatus.value = false;
}

// OCR识图 - 2
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

  // console.log(playerData);
  return playerData;
}

const timerId = setInterval(() => {
  if(pendingDatum.value.size > 0 && !pendingStatus.value) recognizeImg();
}, 1000);

onUnmounted(async () => { 
  clearInterval(timerId);
});
</script>

<style scoped>
.main {
  height: calc(100vh - 125px);
  display: flex;
}

.left {
  width: 80%;
  height: 100%;
}

.right {
  width: 20%;
  height: 100%;
  display: flex;
  flex-direction: column;
}
</style>