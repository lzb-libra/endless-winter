<template>
  <div class="main">
    <div class="left">
      <canvas ref="seatCanvas" :width="canvasWidth" :height="canvasHeight"></canvas>
    </div>
    <div class="right">
      <n-upload :default-upload="false" :multiple="true" :show-retry-button="true" :show-file-list="false"
        @change="handleUploadChange">
        <n-button>上传文件</n-button>
      </n-upload>
      <n-button @click="showModal = !showModal">玩家数据</n-button>
      <canvas ref="canvas" style="max-width: 100%; border: 1px solid #ccc; display: none;"></canvas>
    </div>
  </div>
  <n-modal v-model:show="showModal">
    <n-card style="width: 80vw; height: 80vh;" title="玩家数据" :bordered="false" size="huge" role="dialog"
      aria-modal="true">
      <n-data-table :style="{ height: `${height}px` }" :columns="columns" :data="tableData" :pagination="pagination"
        :bordered="false" flex-height />
    </n-card>
  </n-modal>

</template>

<script setup>
import { ref, onMounted } from 'vue'
import { createWorker } from 'tesseract.js'

const seatCanvas = ref(null)
const canvas = ref(null)
const showModal = ref(false)
const height = ref(window.innerHeight * 0.7)

const columns = [
  { title: '名称', key: "name" },
  { title: '盾兵攻击力', key: "dbgjl" },
  { title: '盾兵防御力', key: "dbfyl" },
  { title: '盾兵穿透力', key: "dbctl" },
  { title: '盾兵生命力', key: "dbsml" },
  { title: '矛兵攻击力', key: "mbgjl" },
  { title: '矛兵防御力', key: "mbfyl" },
  { title: '矛兵穿透力', key: "mbctl" },
  { title: '矛兵生命力', key: "mbsml" },
  { title: '射手攻击力', key: "ssgjl" },
  { title: '射手防御力', key: "ssfyl" },
  { title: '射手穿透力', key: "ssctl" },
  { title: '射手生命力', key: "sssml" }
]

const tableData = ref([]);

const pagination = false

const canvasWidth = 1820
const canvasHeight = 1070

// 网格参数
const gridSize = 40             // 每个格子的宽高（像素）
const gridColor = '#ddd'        // 网格线颜色
const lineWidth = 1             // 网格线宽度

// 3x3 方框参数
const boxGridWidth = 3
const boxGridHeight = 3
const boxBackgroundColor = '#e3f2fd'  // 浅蓝色背景（可自定义，如 '#f0f0f0'、'#cce7ff' 等）
const boxText = '🐻'                  // 你想要显示的文字，比如 "A1", "座位1", "🪑"
const boxTextColor = '#000'           // 文字颜色
const boxTextSize = 64                // 文字字号（像素）

const handleUploadChange = async (fielInfo) => {
  showModal.value = true;

  console.log(fielInfo)

  const img = new Image()
  img.src = URL.createObjectURL(fielInfo.file.file)

  img.onload = async () => {
    const ctx = canvas.value.getContext('2d')
    canvas.value.width = img.width
    canvas.value.height = img.height

    // 绘制原图
    ctx.drawImage(img, 0, 0)

    // 取像素数据
    const imageData = ctx.getImageData(0, 0, img.width, img.height)
    const data = imageData.data

    // 灰度化处理（平均值算法）
    for (let i = 0; i < data.length; i += 4) {
      const r = data[i]
      const g = data[i + 1]
      const b = data[i + 2]
      // 灰度值计算公式（加权平均）
      const gray = 0.299 * r + 0.587 * g + 0.114 * b
      data[i] = data[i + 1] = data[i + 2] = gray
    }

    // 更新画布
    ctx.putImageData(imageData, 0, 0);

    // OCR 识别灰度图
    const worker = await createWorker({
      langPath: window.location.origin + import.meta.env.BASE_URL + '/lang-data',
      gzip: false,
    });
    await worker.loadLanguage('chi_sim_fast');
    await worker.initialize('chi_sim_fast');
    const { data: result } = await worker.recognize(fielInfo.file.file)

    // 释放资源
    await worker.terminate();

    const playerData = {};

    const lines = result.text.split(/\r?\n/)
    for (const item of lines) {
      console.log(item)

      if (item.includes('[QGD]')) {
        const cleaned = item.split(' ').filter(item => item.trim() !== '')
        playerData['name'] = cleaned[0].replace('[QGD]', '')
      }

      if (item.includes('盾兵攻击')) {
        const cleaned = item.split(' ').filter(item => item.trim() !== '')
        playerData['dbgjl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
      }
      if (item.includes('盾兵防御')) {
        const cleaned = item.split(' ').filter(item => item.trim() !== '')
        playerData['dbfyl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
      }
      if (item.includes('盾兵穿透')) {
        const cleaned = item.split(' ').filter(item => item.trim() !== '')
        playerData['dbctl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
      }
      if (item.includes('盾兵生命')) {
        const cleaned = item.split(' ').filter(item => item.trim() !== '')
        playerData['dbsml'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
      }

      if (item.includes('矛兵攻击')) {
        const cleaned = item.split(' ').filter(item => item.trim() !== '')
        playerData['mbgjl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
      }
      if (item.includes('矛兵防御')) {
        const cleaned = item.split(' ').filter(item => item.trim() !== '')
        playerData['mbfyl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
      }
      if (item.includes('矛兵穿透')) {
        const cleaned = item.split(' ').filter(item => item.trim() !== '')
        playerData['mbctl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
      }
      if (item.includes('矛兵生命')) {
        const cleaned = item.split(' ').filter(item => item.trim() !== '')
        playerData['mbsml'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
      }

      if (item.includes('射手攻击')) {
        const cleaned = item.split(' ').filter(item => item.trim() !== '')
        playerData['ssgjl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
      }
      if (item.includes('射手防御')) {
        const cleaned = item.split(' ').filter(item => item.trim() !== '')
        playerData['ssfyl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
      }
      if (item.includes('射手穿透')) {
        const cleaned = item.split(' ').filter(item => item.trim() !== '')
        playerData['ssctl'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
      }
      if (item.includes('射手生命')) {
        const cleaned = item.split(' ').filter(item => item.trim() !== '')
        playerData['sssml'] = Math.trunc(Number(cleaned[1].replace("%", "").replace("+", "")) * 10) / 10
      }
    }

    console.log(playerData);
    tableData.value.push(playerData)
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

      ctx.fillStyle = "#fff"
      ctx.fillRect(seatX, seatY, 80, 80)

      const label = '🚗'
      ctx.font = '32px Arial'
      ctx.textAlign = 'center'
      ctx.textBaseline = 'middle'
      let labelX = seatX + gridSize
      let labelY = seatY + gridSize
      ctx.fillText(label, labelX, labelY)
    }
  }

  // 东环
  const oneRingEastSeat = [-1, 1, 3, 5, 7, 9];
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < oneRingEastSeat.length; j++) {
      const value = oneRingEastSeat[j]
      let seatX = (startGridX + (4 + (i * 2))) * gridSize;
      let seatY = (startGridY + value) * gridSize;

      ctx.fillStyle = "#fff"
      ctx.fillRect(seatX, seatY, 80, 80)

      const label = '🚗'
      ctx.font = '32px Arial'
      ctx.textAlign = 'center'
      ctx.textBaseline = 'middle'
      let labelX = seatX + gridSize
      let labelY = seatY + gridSize
      ctx.fillText(label, labelX, labelY)
    }
  }

  // 南环
  const oneRingSouthSeat = [2, 0, -2, -4, -6, -8];
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < oneRingSouthSeat.length; j++) {
      const value = oneRingSouthSeat[j]
      let seatX = (startGridX + value) * gridSize;
      let seatY = (startGridY + (4 + (i * 2))) * gridSize;

      ctx.fillStyle = "#fff"
      ctx.fillRect(seatX, seatY, 80, 80)

      const label = '🚗'
      ctx.font = '32px Arial'
      ctx.textAlign = 'center'
      ctx.textBaseline = 'middle'
      let labelX = seatX + gridSize
      let labelY = seatY + gridSize
      ctx.fillText(label, labelX, labelY)
    }
  }

  // 西环
  const oneRingWestSeat = [2, 0, -2, -4, -6, -8];
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < oneRingWestSeat.length; j++) {
      const value = oneRingWestSeat[j]
      let seatX = (startGridX - (3 + (i * 2))) * gridSize;
      let seatY = (startGridY + value) * gridSize;

      ctx.fillStyle = "#fff"
      ctx.fillRect(seatX, seatY, 80, 80)

      const label = '🚗'
      ctx.font = '32px Arial'
      ctx.textAlign = 'center'
      ctx.textBaseline = 'middle'
      let labelX = seatX + gridSize
      let labelY = seatY + gridSize
      ctx.fillText(label, labelX, labelY)
    }
  }
}

// 在组件挂载后绘制
onMounted(() => {
  // drawSeat();
})
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
}
</style>