<template>
  <div class=" w-full bg-white px-4 grid grid-cols-12 gap-2 control-box">
    <div class="col-span-3 control-user space-x-2 border-r border-gray-700">
        <div class="px-4 py-3 bg-gray-700 rounded-full">An</div>
        <div class="self-center">
            <h3 v-if="username">{{username}}</h3>
            <h3 v-else>Anony</h3>
            <!-- <h3 class="overflow-hidden">{{socket_id}}</h3> -->
        </div>
    </div>
    
    <div class="col-span-9 px-2 py-2  font-semibold">
       {{messages}}
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
export default {
props:["message"],
data:function(){
    return{
        messages:"",
        socket_id:"",
        username:""
    }
},
computed:{
    ...mapGetters(["getUser"])

},
created(){
    console.log("here it is")
    this.messages=this.message.data.data;
    this.socket_id=this.message.socket_id;
    this.username=this.message.username
    
    // console.log(this.message.data.data)
}
}
</script>

<style scoped>
.control-box{
    min-height: 60px;
    /* background:green; */
    /* justify-items: center; */
    align-items: center;
}

.control-user{
    display:flex;
}


</style>