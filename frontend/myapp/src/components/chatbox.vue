<template>
  <div class=" w-full bg-white px-4 grid grid-cols-12 gap-2 control-box">
    <div class="col-span-3 control-user space-x-2 border-r border-gray-700">
        <div class="px-4 py-3 bg-gray-700 rounded-full">U</div>
        <div class="self-center">
            username
        </div>
    </div>
    <div class="col-span-9 px-2 py-2  font-semibold">
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Fuga deleniti id sed sequi doloremque harum enim delectus laboriosam ex vitae.
    </div>
  </div>
</template>

<script>
export default {

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