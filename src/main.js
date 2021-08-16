import Vue from 'vue'
import App from './App.vue'

import VueVideoPlayer from 'vue-video-player'

Vue.use(VueVideoPlayer)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
