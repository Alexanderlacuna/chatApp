<template>
  <div class="nav-control justify-around items-center ">
     <div>
      <h3>menu</h3>
     </div>
     <div class="nav-inner  space-x-4">
         <div>
             <h3>Home</h3>
         </div>
         <div>
             <router-link to="/login" >Login/Register</router-link>
             <!-- <h3>Login/register</h3> -->
         </div>
         <div>
             <h3>Create group</h3>
         </div>
         <div>
             <h3>setting</h3>
         </div>

         <div>
             <h3>leave group</h3>
         </div>
     </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.nav-control{
    min-height: 63px;
    background-color:#333;
    color:#fff;
    display:flex; 
    flex-direction:row;
    
}
.nav-inner{
    display: flex;
}
</style>>

