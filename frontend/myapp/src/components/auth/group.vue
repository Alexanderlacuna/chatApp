<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Create group
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <!-- <span class="headline">Create group</span> -->
           <small>*login is required to complete this action</small>
        </v-card-title>
        <v-card-text>
          <v-container>
               <form >
          	<v-layout row class="justify-center ma-2" >
	  			<v-flex md6>
	  				<v-text-field
	  				v-model="groupName"
	  				color="pink darken-2"
	  				label="groupName"
            

	  				required
	  				
	  				>
	  					
	  				</v-text-field>
	  			</v-flex>
	  			
	  		</v-layout>
        <!-- <v-layout row class="justify-center mt-2">

	  			<v-flex md6>
	  				
	  				<v-btn large block class="ma-2 pink--text darken-2"  type="submit">SUBMIT</v-btn>
	  			</v-flex>
	  			
	  		</v-layout> -->
      
      </form>
          </v-container>
         
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="handlesubmit">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>


<script>
  import {mapActions} from "vuex";
  export default {
    methods:{
        ...mapActions(["create_group"]),
        handlesubmit:function(){
            this.dialog=false;
            console.log("Submitted")
            this.create_group(this.groupName)


        }
    },
    data:function(){
        return {
            groupName:"",
            dialog:false
        }
    }
  }
</script>