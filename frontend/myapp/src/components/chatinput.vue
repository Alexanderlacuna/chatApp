<template>
   <form @submit.prevent="handleSubmit">
     <div class="grid grid-cols-12 gap-1">
          <div class="col-span-10">
    <v-container fluid>
    <v-textarea
      name="input-7-1"
      filled
      label="Message"
      auto-grow
      v-model="message"
      placeholder="Type your message here"
     
    ></v-textarea>
  </v-container>
             
          </div>
           <div class="flex items-center">
              <button class="px-6 py-3 rounded-lg bg-black text-white" type="submit" >
                  Send
              </button>
           </div>
         
      </div>

   </form>
</template>

<script>
import {mapGetters} from "vuex";
export default {
  computed:{
   ...mapGetters(["getUser"])
 
  },

    sockets:{
    connect:function(){
    
      console.log("connected")
      this.$socket.emit("join_public",{message:"this is the first"})
    }

  },

    data:function(){
        return{
            message:""
        }
    },

      methods:{
      handleSubmit:function(){
          this.$socket.emit("anony_message",{username:this.getUser,data:this.message})
          
      }

  }
  

}
</script>

<style>

</style>