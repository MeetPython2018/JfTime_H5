import axios from 'axios'
import qs from 'qs'
export function f1(audio_src,audio_name,creator,index) {
  let audio_infos = {
    'audio_src':audio_src,
    'audio_name':audio_name,
    'creator':creator,
    'index':index,
  }
  return audio_infos
  // this.$emit('load_audio',audio_infos)
}
export function f2(val) {
  axios.get('/ajax/seeMessages',{params:{
            audio_id:val
          }
        }).then((res)=>{
          if(res.data.length===0){
            this.count=0
            this.loading = false
          }else{
            this.count = res.data
            this.loading = false
          }
          this.dialogVisible = true
        })
}