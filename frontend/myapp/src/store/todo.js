const state={
    users:"",
    messages:[]

}
const mutations={

    CALL_TOKEN:(state,payload)=>{
        state.users=payload
        console.log("hello there")
    },

    ANONY_MESSAGE:(state,payload)=>{
        state.messages.push(payload)

    },

    RESET:(state)=>{
        state.users=""
    }


}
const actions={
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