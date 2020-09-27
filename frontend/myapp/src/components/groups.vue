<template>
  <div class="min-h-screen">
     <div class="text-center my-4">
     <h3 class="underline font-bold">join groups</h3>
      <div class="space-x-2  flex  justify-center pt-3 items-center">
      <h3 class="font-semibold text-lg " >AVANDARS</h3>
      <button class=" rounded-lg  text-white px-2 py-1 bg-red-400">Join</button>
      </div>
     </div>

     <div>
        <group/>
     </div>
  </div>
</template>

<script>
import group from "@/components/auth/group.vue"
export default {
  components:{
    group
  }

}
</script>

<style>

</style>