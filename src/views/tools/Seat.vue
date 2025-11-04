<template>
  <div>
    <div style="display: flex; padding-bottom: 10px;">
      <n-upload :default-upload="false" :multiple="true" :show-retry-button="true" :show-file-list="false"
        accept="image/*" v-model:file-list="fileList" @change="handleUploadChange"
        style="margin-right: 10px; width: 85px;">
        <n-button>上传图片</n-button>
      </n-upload>
      <n-button @click="showPlayerSeatChart" style="margin-right: 10px; width: 85px;">座位地图</n-button>
      <n-upload :default-upload="false" :multiple="false" :show-retry-button="true" :show-file-list="false"
        accept=".json" v-model:file-list="fileList" @change="handleUploadChangeJson"
        style="margin-right: 10px; width: 85px;">
        <n-button>导入配置</n-button>
      </n-upload>
      <n-button @click="exportToJSON" style="margin-right: 10px; width: 85px;">导出配置</n-button>
      <n-button @click="exportToJSON" style="margin-right: 10px; width: 85px;">座次标识</n-button>
    </div>
    <div style="display: flex; align-items: center; padding-bottom: 10px;">
      <n-progress style="flex: 1;" type="line" :percentage="percentage" indicator-placement="inside" />
      <span style="padding-left: 10px;">{{ count }} / {{ fileList.length }}</span>
    </div>
    <n-data-table :columns="columns" :data="tableData" :pagination="pagination" style="height: 1030px;"
      :key="row => row.key" :bordered="false" flex-height striped />

    <n-modal v-model:show="showTableDetailModal" style="width: 800px;">
      <n-card>
        <div style="display: flex; justify-content: space-between;">
          <n-form ref="formRef" :model="showTableDetail" label-placement="left" label-width="auto"
            require-mark-placement="right-hanging" size="medium">
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
            <n-form-item label="射手穿透力" path="ssctl">
              <n-input v-model:value="showTableDetail.ssctl" type="number" />
            </n-form-item>
            <n-form-item label="射手生命力" path="sssml">
              <n-input v-model:value="showTableDetail.sssml" type="number" />
            </n-form-item>
          </n-form>
          <img :src="showTableDetail.imgUrl" style="width: 430px; height: 730px; margin-left: 20px;">
        </div>
      </n-card>
    </n-modal>

    <n-modal v-model:show="showSeatCanvasModal" style="width: 90vw; height: 100vh;">
      <n-card>
        <div style="display: flex; justify-content: space-between;">
          <div style="width: 300px;">
            <n-input placeholder="搜索" style="margin-bottom: 8px;" @input="inputChange" @clear="inputClear" clearable />
            <div style="overflow-y: auto; height: 92vh;">
              <n-list hoverable clickable>
                <n-list-item v-for="(obj, index) in seatCanvasDatum" @click="locatePlayerPosition(obj)" :key="index">
                  <div style="display: flex;">
                    <div v-if="selectedPlayer && selectedPlayer.name === obj.name" style="padding-right: 10px;">✅</div>
                    <div style="display: flex; justify-content: space-between; width: 100%;">
                      <div>{{ index + 1 }}、{{ obj.name }}</div>
                      <div>{{ obj[selectSortField] }}</div>
                    </div>
                  </div>
                </n-list-item>
              </n-list>
            </div>
          </div>
          <canvas ref="seatCanvas" :width="1900" :height="1150"></canvas>
        </div>
      </n-card>
    </n-modal>

    <n-modal v-model:show="showSelectSortFieldModal" preset="dialog" title="请选择一项进行排序" positive-text="确认"
      negative-text="取消" @positive-click="selectSortFieldPositive"
      @negative-click="showSelectSortFieldModal = !showSelectSortFieldModal">
      <n-select v-model:value="selectSortField" :options="selectSortFieldOptions" placeholder="请选择" />
    </n-modal>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, nextTick, h, reactive } from 'vue';
import { createWorker } from 'tesseract.js';
import { NButton, useMessage } from 'naive-ui';

const message = useMessage();

const timerId = setInterval(() => {
  if (pendingDatum.value.size > 0 && !pendingStatus.value) recognizeImg();
}, 1000);

const selectSortFieldOptions = [
  { label: '盾兵攻击力', value: 'dbgjl' },
  { label: '盾兵防御力', value: 'dbfyl' },
  { label: '盾兵穿透力', value: 'dbctl' },
  { label: '盾兵生命力', value: 'dbsml' },

  { label: '矛兵攻击力', value: 'mbgjl' },
  { label: '矛兵防御力', value: 'mbfyl' },
  { label: '矛兵穿透力', value: 'mbctl' },
  { label: '矛兵生命力', value: 'mbsml' },

  { label: '射手攻击力', value: 'ssgjl' },
  { label: '射手防御力', value: 'ssfyl' },
  { label: '射手穿透力', value: 'ssctl' },
  { label: '射手生命力', value: 'sssml' },
]

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
    sorter: (row1, row2) => row1.dbgjl - row2.dbgjl
  },
  {
    title: '盾兵防御力',
    key: "dbfyl",
    ssorter: (row1, row2) => row1.dbfyl - row2.dbfyl
  },
  {
    title: '盾兵穿透力',
    key: "dbctl",
    sorter: (row1, row2) => row1.dbctl - row2.dbctl
  },
  {
    title: '盾兵生命力',
    key: "dbsml",
    sorter: (row1, row2) => row1.dbsml - row2.dbsml
  },
  {
    title: '矛兵攻击力',
    key: "mbgjl",
    sorter: (row1, row2) => row1.mbgjl - row2.mbgjl
  },
  {
    title: '矛兵防御力',
    key: "mbfyl",
    sorter: (row1, row2) => row1.mbfyl - row2.mbfyl
  },
  {
    title: '矛兵穿透力',
    key: "mbctl",
    sorter: (row1, row2) => row1.mbctl - row2.mbctl
  },
  {
    title: '矛兵生命力',
    key: "mbsml",
    sorter: (row1, row2) => row1.mbsml - row2.mbsml
  },
  {
    title: '射手攻击力',
    key: "ssgjl",
    sorter: (row1, row2) => row1.ssgjl - row2.ssgjl
  },
  {
    title: '射手防御力',
    key: "ssfyl",
    sorter: (row1, row2) => row1.ssfyl - row2.ssfyl
  },
  {
    title: '射手穿透力',
    key: "ssctl",
    sorter: (row1, row2) => row1.ssctl - row2.ssctl
  },
  {
    title: '射手生命力',
    key: "sssml",
    sorter: (row1, row2) => row1.sssml - row2.sssml
  }
]

const seatKey = new Map([
  ['north', new Map([
    ['0', [5,   1,  9,  25, 45, 61]],
    ['1', [17,  13, 21, 29, 53, 65]],
    ['2', [37,  33, 41, 49, 57, 69]],
  ])],
  ['east', new Map([
    ['0', [6,   2,  10, 26, 46, 62]],
    ['1', [18,  14, 22, 30, 54, 66]],
    ['2', [38,  34, 42, 50, 58, 70]],
  ])],
  ['south', new Map([
    ['0', [7,   3,  11, 27, 47, 63]],
    ['1', [19,  15, 23, 31, 55, 67]],
    ['2', [39,  35, 43, 51, 59, 71]],
  ])],
  ['west', new Map([
    ['0', [8,   4,  12, 28, 48, 64]],
    ['1', [20,  16, 24, 32, 56, 68]],
    ['2', [40,  36, 44, 52, 60, 72]],
  ])],
]);

// 画布网格参数
const gridSize = 50;      // 每个格子的宽高（像素）
const gridColor = '#ddd'; // 网格线颜色
const lineWidth = 1;      // 网格线宽度

// 3x3 方框参数
const boxGridWidth = 3;
const boxGridHeight = 3;
const boxBackgroundColor = '#e3f2fd';  // 浅蓝色背景（可自定义，如 '#f0f0f0'、'#cce7ff' 等）
const boxText = '🐻';                 // 你想要显示的文字，比如 "A1", "座位1", "🪑"
const boxTextColor = '#000';           // 文字颜色
const boxTextSize = 64;                 // 文字字号（像素）

// 表格分页
const pagination = reactive({
  page: 1,
  pageSize: 20,
  showSizePicker: false,
  onChange: (page) => {
    pagination.page = page
  },
  onUpdatePageSize: (pageSize) => {
    pagination.pageSize = pageSize
    pagination.page = 1
  }
});
// 表格数据
const tableData = ref([]);
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
// 选择的排序方式
const selectSortField = ref('');
const showSelectSortFieldModal = ref(false);
// 是否显示座位图
const showSeatCanvasModal = ref(false);
// 排序后的数据
const seatCanvasDatum = ref({});
// 当前选中的玩家
const selectedPlayer = ref(null);
// canvas上的数据
const playerSeatDatum = ref({});
// 地图对象
const seatCanvas = ref(null);

// 图片上传
const handleUploadChange = async (fielInfo) => {
  console.log(fielInfo)

  const imgFile = fielInfo.file.file;

  const img = new Image()
  img.src = URL.createObjectURL(imgFile)

  img.onload = async () => {
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
  if (playerData) {
    const reader = new FileReader();
    reader.onload = (e) => {
      playerData['imgUrl'] = e.target.result;
      playerData['imgId'] = key;

      tableData.value.push(playerData);

      count.value++;
      percentage.value = ((count.value / fileList.value.length) * 100).toFixed(0);
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
    if (!playerData['name'] && (item.includes('QGD') || item.includes('FUN'))) {
      let cleaned = item.replace(/^.*?【QGD】/i, '').replace(/^.*?【FUN】/i, '');
      cleaned = cleaned.replace(/^.*?\[QGD\]/i, '').replace(/^.*?\[FUN\]/i, '');
      cleaned = cleaned.split(' ').filter(item => item.trim() !== '');
      playerData['name'] = cleaned[0];
    }
    if (!playerData['name']) playerData['name'] = file.name.replace('.png', '');

    if (item.includes('盾兵攻')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['dbgjl'] = cleanPercent(cleaned[1]);
    }
    if (item.includes('盾兵防')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['dbfyl'] = cleanPercent(cleaned[1]);
    }
    if (item.includes('盾兵穿')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['dbctl'] = cleanPercent(cleaned[1]);
    }
    if (item.includes('盾兵生')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['dbsml'] = cleanPercent(cleaned[1]);
    }

    if (item.includes('矛兵攻')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['mbgjl'] = cleanPercent(cleaned[1]);
    }
    if (item.includes('矛兵防')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['mbfyl'] = cleanPercent(cleaned[1]);
    }
    if (item.includes('矛兵穿')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['mbctl'] = cleanPercent(cleaned[1]);
    }
    if (item.includes('矛兵生')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['mbsml'] = cleanPercent(cleaned[1]);
    }

    if (item.includes('射手攻')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['ssgjl'] = cleanPercent(cleaned[1]);
    }
    if (item.includes('射手防')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['ssfyl'] = cleanPercent(cleaned[1]);
    }
    if (item.includes('射手穿')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['ssctl'] = cleanPercent(cleaned[1]);
    }
    if (item.includes('射手生')) {
      const cleaned = item.split(' ').filter(item => item.trim() !== '')
      playerData['sssml'] = cleanPercent(cleaned[1]);
    }
  }

  return playerData;
}

// 将数值处理成保留一位小数的数字字符串
const cleanPercent = (str) => {
  // 1. 去掉 "+" 和 "%" 符号
  const numStr = str.replace(/[+%]/g, "").trim();

  // 2. 转成数字
  const num = Number(numStr);

  // 3. 截断到一位小数（不四舍五入）
  const truncated = Math.trunc(num * 10) / 10;

  // 4. 转回字符串（保留 1 位小数）
  return truncated.toFixed(1).trim();
}

// 选择字段后的确认
const selectSortFieldPositive = async () => {
  seatCanvasDatum.value = [...tableData.value].sort((a, b) => {
    const x = Number(String(a[selectSortField.value]).trim());
    const y = Number(String(b[selectSortField.value]).trim());
    if (x === y) return 0;
    return x > y ? -1 : 1;
  });

  playerSeatDatum.value = [...seatCanvasDatum.value]

  showSeatCanvasModal.value = true;
  await nextTick();

  drawSeatMap();
}

// 展示座位布局图
const showPlayerSeatChart = () => {
  // if (tableData.value.length === 0) {
  //   message.warning("请先上传玩家数据!!!");
  //   return;
  // }

  showSelectSortFieldModal.value = true;
}

// 绘制座位地图
const drawSeatMap = () => {
  const canvas = seatCanvas.value
  if (!canvas) return

  const ctx = canvas.getContext('2d')
  if (!ctx) return

  ctx.clearRect(0, 0, canvas.width, canvas.height);

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

  // 画布中心点坐标
  const canvasCenterX = canvas.width / 2
  const canvasCenterY = canvas.height / 2

  // ============================
  // 绘制 3x3 的方框 - 中间熊坑
  // ============================
  const boxWidth = boxGridWidth * gridSize
  const boxHeight = boxGridHeight * gridSize

  const desiredCenterX = canvasCenterX
  const desiredCenterY = canvasCenterY

  const desiredLeft = desiredCenterX - boxWidth / 2
  const desiredTop = desiredCenterY - boxHeight / 2

  const alignedLeft = Math.round(desiredLeft / gridSize) * gridSize
  const alignedTop = Math.round(desiredTop / gridSize) * gridSize

  const boxLeft = alignedLeft
  const boxTop = alignedTop

  ctx.fillStyle = boxBackgroundColor
  ctx.fillRect(boxLeft, boxTop, boxWidth, boxHeight)

  ctx.fillStyle = boxTextColor
  ctx.font = `${boxTextSize}px Arial`
  ctx.textAlign = 'center'
  ctx.textBaseline = 'middle'
  const textX = boxLeft + boxWidth / 2
  const textY = boxTop + boxHeight / 2

  ctx.fillText(boxText, textX, textY + 5)

  // ============================
  // 绘制 1x1 的方框 - 四周的旗子
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
    ctx.font = '32px Arial'
    ctx.textAlign = 'center'
    ctx.textBaseline = 'middle'
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

// 绘制地图上的标志
const drawPlayerSeat = (ctx, key, seatX, seatY, i, j) => {
  const keys = seatKey.get(key);
  let label = keys.get(i + "")[j];

  if (playerSeatDatum.value.length >= label) {
    label = playerSeatDatum.value[label - 1].name
  }

  ctx.fillStyle = label === selectedPlayer.value?.name ? "#f00" : "#fff"
  ctx.fillRect(seatX, seatY, gridSize * 2, gridSize * 2)

  ctx.lineWidth = 1
  ctx.strokeStyle = label === selectedPlayer.value?.name ? "#f00" : "#000"
  ctx.strokeRect(seatX, seatY, gridSize * 2, gridSize * 2)

  ctx.font = '12px Arial'
  ctx.textAlign = 'center'
  ctx.textBaseline = 'middle'
  ctx.fillStyle = 'black'
  let labelX = seatX + gridSize
  let labelY = seatY + gridSize

  label = label.length > 6 ? label.substring(0, 6) + "..." : label;
  ctx.fillText(label, labelX, labelY)
}

// 导入数据
const handleUploadChangeJson = (fielInfo) => {
  const reader = new FileReader();
  reader.onload = function (e) {
    tableData.value = JSON.parse(e.target.result);
  };

  reader.onerror = function () {
    message.error("文件读取失败！");
  };

  reader.readAsText(fielInfo.file.file);
}

// 导出配置文件
const exportToJSON = () => {
  const jsonString = JSON.stringify(tableData.value, null, 2);
  const blob = new Blob([jsonString], { type: 'application/json' });
  const url = URL.createObjectURL(blob);

  const filename = `export-data-${Date.now()}.json`;

  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

// 检索玩家
const inputChange = (val) => {
  console.log(val);
  if (val) {
    seatCanvasDatum.value = seatCanvasDatum.value.filter(item => item.name.includes(val));
  } else {
    seatCanvasDatum.value = [...playerSeatDatum.value]
  }

  drawSeatMap()
}

// 清空检索条件
const inputClear = () => {
  selectedPlayer.value = null
  drawSeatMap()
}

// 选中玩家并定位
const locatePlayerPosition = (obj) => {
  if (!selectedPlayer.value || (selectedPlayer.value && selectedPlayer.value.name !== obj.name)) {
    selectedPlayer.value = obj;
  } else if (selectedPlayer.value && selectedPlayer.value.name === obj.name) {
    selectedPlayer.value = null;
  }

  drawSeatMap();
}

watch(tableData, () => {
  seatCanvasDatum.value = [...tableData.value]
}, { deep: true });

onMounted(async () => { });

onUnmounted(async () => {
  clearInterval(timerId);
});
</script>

<style scoped></style>