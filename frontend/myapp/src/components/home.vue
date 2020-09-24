<template>
  <div class="grid grid-cols-12 gap-1">
    <div class="bg-black col-span-3 border-r-2 border-gray-300"> 
         <users/>
    </div>
     <div class="bg-red-400 col-span-6">
         <chatroom/>
     </div>
     <div  class="bg-black col-span-3">
         <groups/>
     </div>
  </div>
</template>

<script>
import  chatroom from "@/components/chatroom.vue"
import  groups from "@/components/groups.vue"
import  users from "@/components/users.vue"
export default {
    components:{
        chatroom,
        groups,
        users
    }

}
</script>

<style>

</style>