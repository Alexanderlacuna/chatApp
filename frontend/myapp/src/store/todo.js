
import axios from "axios";
const state={
    users:"",
    messages:[],
    auth_key:"",
    current_user:"",
    groups:[]

}
const mutations={

    CALL_TOKEN:(state,payload)=>{
        state.users=payload
        console.log("hello there")
    },
    ADD_AUTH_KEY:(state,payload)=>{
        state.auth_key=payload.auth_key

    },

    ANONY_MESSAGE:(state,payload)=>{
        state.messages.push(payload)

    },
    ADD_GROUPS:(state,payload)=>{
        state.groups=payload
    },

    RESET:(state)=>{
        state.users=""
    }


}
const actions={
async create_group({commit,state},payload){
    let token=state.auth_key;
    console.log(`the token is ${token}`);
    console.log(`the payload is ${payload}`)
    let data={
      items:payload
    }

    try{
        let response=await axios.post("http://127.0.0.1:5000/chat/createroom",data,{
            params:{
                "auth_key":token

            }
        });
        console.log(response);
        console.log(commit);

    }
    catch(e){
        console.log(e)
        console.log(e.response)
    }
    
  
   

},
async register_user({commit},payload){
    console.log(commit)
    try{
      let response=await axios.post("http://127.0.0.1:5000/register",payload);
      console.log(response)
      let data=response.data
      commit("ADD_AUTH_KEY",data)
    }
    catch(e){
        console.log(e.response)
    }
},
 async login_user({commit},payload){

    try{
        let response=await axios.post("http://127.0.0.1:5000/login",payload);
        let data=response.data
        console.log(data)
        commit("ADD_AUTH_KEY",data)

    }
    catch(e){
        console.log(e)
      console.log(e.response)
      
    }

    // commit("RESET")
     
     

 },
 async SOCKET_anonymous_join({commit},payload){
     console.log("token received")
     console.log(payload)
     commit("CALL_TOKEN",payload)
 },

 async SOCKET_anony_send({commit},payload){
     console.log("received anonymous message")
     console.log(payload)
     commit("ANONY_MESSAGE",payload)
 },

 async reset_join({commit}){
     commit("RESET")
 },

 async set_groups({commit}){
    try{
        let response=await axios.get("http://127.0.0.1:5000/getrooms");
        console.log(response)
        commit("ADD_GROUPS",response.data)

    }
    catch(e){
          console.log(e.response)
    }

     
 }

}

const getters={
    getMessages:(state)=>state.messages,
    getAnonyJoin:(state)=>state.users,
    getAuthKey:(state)=>state.auth_key,
    getGroups:(state)=>state.groups

}

export default {
    mutations,
    actions,
    getters,
    state
}