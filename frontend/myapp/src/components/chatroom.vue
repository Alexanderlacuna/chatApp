<template>
  <div class="overflow-y-auto">
      <div class="bg-white control-chat border-b border-gray-300">
          <h3 class="font-semibold text-lg text-gray-700">username+online status</h3>
          
      </div>
     
      <div class="py-4 px-3" v-for="message  in  getMessages" :key="message.message_id"> 
          <chatbox :message="message"/>
      </div>

     <div>
         <chatinput/>
     </div>
      
  </div>
</template>

<script>
import chatbox from "@/components/chatbox.vue";
import {mapGetters} from "vuex";
import chatinput from "@/components/chatinput.vue";
export default {
 components:{
     chatbox,
     chatinput,
},
  computed:{
      ...mapGetters(["getMessages"]),


  },


    sockets:{
      anonymous_join:function(data){
      console.log(data)
      console.log("anonymous joined")
    }
         
     },

    data:function(){
        return{
            messages:[]
        }
    }
 }
</script>

<style scoped>
.control-chat{
   min-height:40px;
   display: flex;
   /* justify-content: center; */
   align-items: center;
   padding-left: 20px;
}

</style>