import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: sessionStorage.getItem('state') ? JSON.parse(sessionStorage.getItem('state')): {
    logined:false,
    username:'',
    playAudio(audio_src,audio_name,creator,index){
      let audio_infos = {
        'audio_src':audio_src,
        'audio_name':audio_name,
        'creator':creator,
        'index':index,
      }
      return audio_infos
    }
  },
  mutations: {
    login_in(state){
      state.logined = true
    },
    setUserName(state,n){
      state.username = n
    },
    login_out(state){
      state.logined = false
    }
  },
  actions: {

  }
})
