# Vue 3 + Vite

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about IDE Support for Vue in the [Vue Docs Scaling up Guide](https://vuejs.org/guide/scaling-up/tooling.html#ide-support).


// const allHeros = [
//   {
//     key: 'rare',
//     name: '稀有',
//     items: [
//       { key: 'ShiMiSi', name: '史密斯', width: '100', height: '150', as: 1, type: 2 },
//       { key: 'YouJin', name: '尤金', width: '100', height: '150', as: 1, type: 3 },
//       { key: 'ChaLi', name: '查理', width: '100', height: '150', as: 2, type: 3 },
//       { key: 'KeLaoRuiSi', name: '克劳瑞斯', width: '100', height: '150', as: 3, type: 2 }
      
//     ]
//   },
//   {
//     key: 'epic',
//     name: '史诗',
//     items: [
//       { key: 'XieErGai', name: '谢尔盖', width: '100', height: '150', as: 1, type: 1 },
//       { key: 'PaTeLiKe', name: '帕特里克', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'LingXue', name: '凌雪', width: '100', height: '150', as: 2, type: 2 },
//       { key: 'LuMuBoGen', name: '卢姆·波根', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'JieXi', name: '杰西', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'BaXiTi', name: '巴希提', width: '100', height: '150', as: 3, type: 1 },
//       { key: 'JieSaiEr', name: '杰塞尔', width: '100', height: '150', as: 3, type: 2 },
//       { key: 'JiNa', name: '吉娜', width: '100', height: '150', as: 3, type: 1 },
//       { key: 'ShuYun', name: '书允', width: '100', height: '150', as: 3, type: 2 }
//     ]
//   },
//   {
//     key: 'S1',
//     name: 'S1',
//     items: [
//       { key: 'HeLuoNiMo', name: '赫罗尼莫', width: '100', height: '150', as: 1, type: 1 },
//       { key: 'NaTaLiYa', name: '娜塔莉娅', width: '100', height: '150', as: 1, type: 1 },
//       { key: 'MoLi', name: '茉莉', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'JingMan', name: '津曼', width: '100', height: '150', as: 3, type: 2 }
//     ]
//   },
//   {
//     key: 'S2',
//     name: 'S2',
//     items: [
//       { key: 'FuLinTe', name: '弗林特', width: '100', height: '150', as: 1, type: 1 },
//       { key: 'FeiLanDe', name: '菲兰德', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'ASuoLong', name: '阿索隆', width: '100', height: '150', as: 3, type: 1 }
//     ]
//   },
//   {
//     key: 'S3',
//     name: 'S3',
//     items: [
      
//       { key: 'LuoGen', name: '罗根', width: '100', height: '150', as: 1, type: 1 },
//       { key: 'MiYa', name: '米娅', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'GeLeiGe', name: '格雷格', width: '100', height: '150', as: 3, type: 1 }
//     ]
//   },
//   {
//     key: 'S4',
//     name: 'S4',
//     items: [
//       { key: 'AHeMoSi', name: '阿赫摩斯', width: '100', height: '150', as: 1, type: 1 },
//       { key: 'LingNai', name: '玲奈', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'LinEn', name: '琳恩', width: '100', height: '150', as: 3, type: 1 }
//     ]
//   },
//   {
//     key: 'S5',
//     name: 'S5',
//     items: [
      
//       { key: 'HeKeTuo', name: '赫克托', width: '100', height: '150', as: 1, type: 1 },
//       { key: 'NuoLa', name: '诺拉', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'GeWen', name: '格温', width: '100', height: '150', as: 3, type: 1 }
//     ]
//   },
//   {
//     key: 'S6',
//     name: 'S6',
//     items: [
//       { key: 'WuMing', name: '无名', width: '100', height: '150', as: 1, type: 1 },
//       { key: 'RuiNi', name: '芮妮', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'WeiEn', name: '韦恩', width: '100', height: '150', as: 3, type: 1 }
      
//     ]
//   },
//   {
//     key: 'S7',
//     name: 'S7',
//     items: [
//       { key: 'AiDiSi', name: '艾迪丝', width: '100', height: '150', as: 1, type: 1 },
//       { key: 'GeDun', name: '哥顿', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'BuLaDeLi', name: '布拉德利', width: '100', height: '150', as: 3, type: 1 }
//     ]
//   },
//   {
//     key: 'S8',
//     name: 'S8',
//     items: [
      
//       { key: 'JiaTuo', name: '加托', width: '100', height: '150', as: 1, type: 1 },
//       { key: 'SuoNiYa', name: '索尼娅', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'HengDeLiKe', name: '亨德里克', width: '100', height: '150', as: 3, type: 1 }
//     ]
//   },
//   {
//     key: 'S9',
//     name: 'S9',
//     items: [
//       { key: 'MaGeNuSi', name: '马格努斯', width: '100', height: '150', as: 1, type: 1 },
//       { key: 'FuLeiDe', name: '弗雷德', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'XiuLa', name: '修拉', width: '100', height: '150', as: 3, type: 1 }
//     ]
//   },
//   {
//     key: 'S10',
//     name: 'S10',
//     items: [
//       { key: 'GeLiGaoLi', name: '格里高利', width: '100', height: '150', as: 1, type: 1 },
//       { key: 'FuLeiYa', name: '芙蕾雅', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'BuLanQi', name: '布兰琪', width: '100', height: '150', as: 3, type: 1 }
//     ]
//   },
//   {
//     key: 'S11',
//     name: 'S11',
//     items: [
//       { key: 'AiLaiAoNuoLa', name: '埃莱奥诺拉', width: '100', height: '150', as: 1, type: 1 },
//       { key: 'LaoAiDe', name: '劳埃德', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'LuFuSi', name: '鲁弗斯', width: '100', height: '150', as: 3, type: 1 }
//     ]
//   },
//   {
//     key: 'S12',
//     name: 'S12',
//     items: [
//       { key: 'HeErWeiEr', name: '赫尔薇尔', width: '100', height: '150', as: 1, type: 1 },
//       { key: 'JiaLuoEr', name: '加罗尔', width: '100', height: '150', as: 2, type: 1 },
//       { key: 'LiJiYa', name: '丽姬娅', width: '100', height: '150', as: 3, type: 1 }
//     ]
//   },
//   {
//     key: 'S13',
//     name: 'S13',
//     items: [
//       { key: 'JiSaiLa', name: '吉塞拉', width: '100', height: '150', as: 1, type: 1 }
//     ]
//   }
// ]