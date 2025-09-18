/**
 * 设备检测工具模块
 * 提供设备检测功能
 */

// 定义设备类型常量
const DEVICE_TYPE = {
  MOBILE: 'mobile',
  TABLET: 'tablet',
  DESKTOP: 'desktop'
}

// 定义断点常量
const BREAKPOINTS = {
  MOBILE: 768,
  TABLET: 1024
}

// 响应式状态管理（使用Vue的响应式系统）
let deviceType = DEVICE_TYPE.DESKTOP
let isMobile = false
let isTablet = false
let isDesktop = true
let isMobileView = false
let isTableView = false
let isDesktopView = true
let isTouchDevice = false
let screenWidth = window.innerWidth
let screenHeight = window.innerHeight

/**
 * 检测是否为移动设备
 */
const checkIsMobile = () => {
  const userAgent = navigator.userAgent
  return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|Mobile/i.test(userAgent)
}

/**
 * 检测是否为平板设备
 */
const checkIsTablet = () => {
  const userAgent = navigator.userAgent
  return /iPad|Tablet|PlayBook|Silk|(android(?!.*mobi))/i.test(userAgent)
}

/**
 * 检测是否为桌面设备
 */
const checkIsDesktop = () => {
  return !checkIsMobile() && !checkIsTablet()
}

/**
 * 检测是否为移动视图（基于屏幕宽度）
 */
const checkIsMobileView = (breakpoint = BREAKPOINTS.MOBILE) => {
  return screenWidth < breakpoint
}

/**
 * 检测是否为平板视图（基于屏幕宽度）
 */
const checkIsTableView = (mobileBreakpoint = BREAKPOINTS.MOBILE, desktopBreakpoint = BREAKPOINTS.TABLET) => {
  return screenWidth >= mobileBreakpoint && screenWidth < desktopBreakpoint
}

/**
 * 检测是否为桌面视图（基于屏幕宽度）
 */
const checkIsDesktopView = (breakpoint = BREAKPOINTS.TABLET) => {
  return screenWidth >= breakpoint
}

/**
 * 检测是否支持触摸
 */
const checkIsTouchDevice = () => {
  return 'ontouchstart' in window || navigator.maxTouchPoints > 0 || navigator.msMaxTouchPoints > 0
}

/**
 * 综合检测设备类型
 */
const detectDeviceType = () => {
  const userAgent = navigator.userAgent
  const width = screenWidth
  
  // 移动设备关键词检测
  const mobileKeywords = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|Mobile/i
  
  // 平板关键词
  const tabletKeywords = /iPad|Tablet|PlayBook|Silk/i
  
  // 检测触摸支持
  const touchSupport = 'ontouchstart' in window || navigator.maxTouchPoints > 0
  
  // 检测屏幕尺寸
  const isSmallScreen = width < BREAKPOINTS.MOBILE
  
  if (tabletKeywords.test(userAgent) || (isSmallScreen === false && width < BREAKPOINTS.TABLET && touchSupport)) {
    return DEVICE_TYPE.TABLET
  } else if (mobileKeywords.test(userAgent) || (isSmallScreen && touchSupport)) {
    return DEVICE_TYPE.MOBILE
  } else {
    return DEVICE_TYPE.DESKTOP
  }
}

/**
 * 更新所有设备检测相关状态
 */
const updateDeviceStatus = () => {
  const width = window.innerWidth
  const height = window.innerHeight
  
  screenWidth = width
  screenHeight = height
  
  isMobileView = checkIsMobileView()
  isTableView = checkIsTableView()
  isDesktopView = checkIsDesktopView()
  isTouchDevice = checkIsTouchDevice()
  
  // 根据综合检测设置设备类型
  deviceType = detectDeviceType()
  
  // 设置布尔值状态
  isMobile = deviceType === DEVICE_TYPE.MOBILE
  isTablet = deviceType === DEVICE_TYPE.TABLET
  isDesktop = deviceType === DEVICE_TYPE.DESKTOP
}

/**
 * 初始化设备检测
 */
const initDeviceDetection = () => {
  updateDeviceStatus()
  
  let resizeTimer = null
  window.addEventListener('resize', () => {
    if (resizeTimer) {
      clearTimeout(resizeTimer)
    }
    
    // 使用防抖，避免频繁触发
    resizeTimer = window.setTimeout(() => {
      updateDeviceStatus()
      resizeTimer = null
    }, 100)
  })
}

/**
 * 获取设备检测状态
 */
const getDeviceStatus = () => {
  return {
    deviceType,
    isMobile,
    isTablet,
    isDesktop,
    isMobileView,
    isTableView,
    isDesktopView,
    isTouchDevice,
    screenWidth,
    screenHeight,
    
    // 方法
    checkIsMobile,
    checkIsTablet,
    checkIsDesktop,
    checkIsMobileView,
    checkIsTableView,
    checkIsDesktopView,
    checkIsTouchDevice,
    detectDeviceType
  }
}

// 页面加载完成后初始化
initDeviceDetection()

// 导出方法和状态获取函数
export {
  getDeviceStatus,
  checkIsMobile,
  checkIsTablet,
  checkIsDesktop,
  checkIsMobileView,
  checkIsTableView,
  checkIsDesktopView,
  checkIsTouchDevice,
  detectDeviceType,
  DEVICE_TYPE,
  BREAKPOINTS
}