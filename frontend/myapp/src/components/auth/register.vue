<template>
  <div>
    <div>

      <v-layout row class="justify-center ma-2" >
	  			<v-flex md6>
	  			 Sign up
	  			</v-flex>
	  			
	  		</v-layout>

    </div>
      <form @submit.prevent="handleSubmit">
          	<v-layout row class="justify-center ma-2" >
	  			<v-flex md6>
	  				<v-text-field
	  				v-model="username"
	  				color="pink darken-2"
	  				label="Username"
                    :rules="[validUsername]"
      

	  				required
	  				
	  				>
	  					
	  				</v-text-field>
	  			</v-flex>
	  			
	  		</v-layout>
        	<v-layout row class="justify-center ma-2" >
	  			<v-flex md6>
	  				<v-text-field
	  				v-model="email"
	  				color="pink darken-2"
	  				label="Email"
            :rules="[emailValidity]"

	  				required
	  				
	  				>
	  					
	  				</v-text-field>
	  			</v-flex>
	  			
	  		</v-layout>
          <v-layout row class="justify-center mt-2">

	  			<v-flex md6>
	  			  <v-text-field
            :append-icon="show4 ? 'mdi-eye' : 'mdi-eye-off'"
            
            :type="show4 ? 'text' : 'password'"
           
            label="Password"
            v-model="password"
            :rules="[checkpassword]"
            hint="At least 8 characters"
            value="Pa"
            required 
       
            @click:append="show4 = !show4"
          ></v-text-field>
	  			</v-flex>
	  			
	  		</v-layout>
        <v-layout row class="justify-center mt-2">

	  			<v-flex md6>
	  				
	  				<v-btn large block class="ma-2 pink--text darken-2"  type="submit" :disabled="!formIsValid">SUBMIT</v-btn>
	  			</v-flex>
	  			
	  		</v-layout>
      
      </form>
  </div>
</template>

<script>
import {mapActions} from "vuex";
export default {

     data:function(){
        return{
            email:"",
            username:"",
            password:"",
            show4:false,
            pattern:/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        }
    },
    computed:{

    validUsername:function(){
        return this.username.length>=1?true:"username is required"
    },
      checkpassword:function(){
        console.log(`password length is ${this.password.length}`)
        return this.password.length<8?"password must be atleast 8 characters":true

      },

      emailValidity:function(){
        const validity=this.pattern.test(this.email);
        return validity?true:"valid email is required"

      },

      formIsValid:function(){
        const passwordLength=this.password.length>=8
        const emailValidity=this.pattern.test(this.email)

        if (passwordLength && emailValidity && this.username){
          return true
        }
        return false
      }
    },

    methods:{
      ...mapActions(['register_user']),
      handleSubmit(){
        // call actions to pass data
        console.log(this.password,this.email)
        this.register_user({username:this.username,email:this.email,password:this.password})
      }
    }

}
</script>

<style>

</style>