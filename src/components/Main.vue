<template>
  <video-player
    ref="videoPlayer"
    class="vjs-custom-skin"
    :options="playerOptions"/>
</template>

<script>
 import 'video.js/dist/video-js.css'
 import "vue-video-player/src/custom-theme.css";
 import { videoPlayer } from 'vue-video-player'

 export default {
   name: 'Main',
   components: {
     videoPlayer
   },
   computed: {
     player() {
       return this.$refs.videoPlayer.player
     }
   },
   props: {
   },
   watch: {
   },
   data() {
     return {
       playerOptions: {
         muted: false,
         playbackRates: [0.5, 0.7, 1.0, 1.5, 2.0, 3.0],
         sources: [],
         autoplay: true,
         controls: true,
         fluid: true,/* NOTE: keep this opiton, otherwise control bar is not show */
       }
     }
   },
   mounted() {
     window.init = this.init;
     window.togglePlay = this.togglePlay;
     window.forward = this.forward;
     window.backward = this.backward;
     window.restart = this.restart;
     window.increaseVolume = this.increaseVolume;
     window.decreaseVolume = this.decreaseVolume;
     window.getCurrentTime = this.getCurrentTime;
     window.setCurrentTime = this.setCurrentTime;
   },
   methods: {
     init(file) {
       this.playerOptions.sources = [{
         src: file
       }];
     },

     togglePlay() {
       if (this.player.paused()) {
         this.player.play();
       } else {
         this.player.pause();
       }
     },

     forward() {
       this.player.currentTime(this.player.currentTime() + 10);
     },

     backward() {
       this.player.currentTime(this.player.currentTime() - 10);
     },

     restart() {
       this.player.currentTime(0);
     },

     increaseVolume() {
       this.player.volume(this.player.volume() + 0.1);
     },

     decreaseVolume() {
       this.player.volume(this.player.volume() - 0.1);
     },

     getCurrentTime() {
       return this.player.currentTime();
     },

     setCurrentTime(time) {
       this.player.currentTime(parseInt(time));
     }
   }
 }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
 .video-player {
   width: 100%;
 }
</style>
