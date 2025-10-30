<template>
  <div class="main">
    <div class="left">
      <canvas ref="seatCanvas" :width="canvasWidth" :height="canvasHeight"></canvas>
    </div>
    <div class="right"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const seatCanvas = ref(null)
const canvasWidth = 1820
const canvasHeight = 1070

// 网格参数
const gridSize = 40             // 每个格子的宽高（像素）
const gridColor = '#ddd'        // 网格线颜色
const lineWidth = 1             // 网格线宽度

// 3x3 方框参数
const boxGridWidth = 3
const boxGridHeight = 3
const boxBorderColor = '#000'         // 边框颜色
const boxBorderWidth = 2              // 边框宽度
const boxBackgroundColor = '#e3f2fd'  // 浅蓝色背景（可自定义，如 '#f0f0f0'、'#cce7ff' 等）
const boxText = '🐻'                  // 你想要显示的文字，比如 "A1", "座位1", "🪑"
const boxTextColor = '#000'           // 文字颜色
const boxTextSize = 64                // 文字字号（像素）

// 小方格参数
const smallBoxSize = 1      // 1 格
const smallBoxColor = '#ffeb3b' // 小方格背景色（比如黄色，可自定义）
const smallBoxBorderColor = '#fbc02d' // 可选：小方框边框颜色
const smallBoxBorderWidth = 1

// 绘制网格函数
const drawGrid = (ctx, width, height, gridSize, color, lineWidth) => {
  ctx.strokeStyle = color
  ctx.lineWidth = lineWidth

  // 绘制垂直线
  for (let x = 0; x <= width; x += gridSize) {
    ctx.beginPath()
    ctx.moveTo(x, 0)
    ctx.lineTo(x, height)
    ctx.stroke()
  }

  // 绘制水平线
  for (let y = 0; y <= height; y += gridSize) {
    ctx.beginPath()
    ctx.moveTo(0, y)
    ctx.lineTo(width, y)
    ctx.stroke()
  }
}

// 在组件挂载后绘制
onMounted(() => {
  const canvas = seatCanvas.value
  if (!canvas) return

  const ctx = canvas.getContext('2d')
  if (!ctx) return

  ctx.clearRect(0, 0, canvas.width, canvas.height)

  // 绘制网格
  drawGrid(ctx, canvas.width, canvas.height, gridSize, gridColor, lineWidth)

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
  for(let i = 0; i < 3; i++) {
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
  for(let i = 0; i < 3; i++) {
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
  for(let i = 0; i < 3; i++) {
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
  for(let i = 0; i < 3; i++) {
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
}
</style>