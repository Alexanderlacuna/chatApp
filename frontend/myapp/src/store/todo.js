
import axios from "axios";
const state={
    users:"",
    messages:[],
    auth_key:""

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

    RESET:(state)=>{
        state.users=""
    }


}
const actions={
async register_user({commit},payload){
    console.log(commit)
    try{
      let response=await axios.post("http://127.0.0.1:5000/register",payload);
      console.log(response)
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
 }

}

const getters={
    getMessages:(state)=>state.messages,
    getAnonyJoin:(state)=>state.users,

}

export default {
    mutations,
    actions,
    getters,
    state
}