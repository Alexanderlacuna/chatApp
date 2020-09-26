<template>
  <div class="min-h-screen">
     <div class="text-center my-4">
     <h3>join groups</h3>
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