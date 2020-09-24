<template>
  <v-app>
    <div>
  <div>
    <navbar/>
  </div>
  <router-view></router-view>
    </div>
  </v-app>
</template>

<script>
import navbar from "./components/navbar.vue"
export default {
  name: "App",
  sockets:{
    connect:function(){
    
      console.log("connected")
      this.$socket.emit("join_public",{message:"this is the first"})
    },

    anonymous_join:function(data){
      console.log(data)
      console.log("anonymous joined")
    }

  },

  components: {
    navbar
   
  },


  data: () => ({
    //
  })
};
</script>
