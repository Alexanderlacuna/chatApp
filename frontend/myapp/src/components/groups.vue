<template>
  <div class="min-h-screen">
     <div class="text-center my-4">
     <h3 class="underline font-bold border-b border-gray-200">join groups</h3>
      <div class="space-x-2  flex  justify-evenly pt-3 items-center  border-b border-gray-300 py-5" v-for="group in getGroups" :key="group.public_id">
      <h3 class="font-semibold text-lg  capitalize w-1/2" >{{group.name}}</h3>
      <button class=" rounded-lg  text-white px-2 py-1 bg-red-400 w-1/2 ml-2 ">Join</button>
      </div>
     </div>

     <div>
        <group/>
     </div>
  </div>
</template>

<script>
import group from "@/components/auth/group.vue"
import {mapActions,mapGetters} from  "vuex";
export default {
  components:{
    group
  },

  created(){
    this.set_groups();

  },
  computed:{

    ...mapGetters(["getGroups"])
  },

  methods:{

    ...mapActions(["set_groups"])
  }

}
</script>

<style>

</style>