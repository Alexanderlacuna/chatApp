
var socket = io("http://127.0.0.1:5000")
console.log(socket)


var form=document.querySelector(".form-data")


form.addEventListener("submit",(e)=>{
	e.preventDefault()
	let formData=new FormData(e.target);
	console.log(e)
	console.log("form has been submitted")
	console.log(`formData is, ${formData}`)
	let user=formData.get("username");
	let message=formData.get("message")
	console.log(`the username is ${user} and the message is ${message}`)
	// message_handler({user,message})
	anony_message(socket.id,message)
	form.reset();
})

function message_handler(data){

	console.log("calling it,")
	socket.emit("send_message",data)
}
socket.on("connect",()=>{
	let user={
		name:socket.id,
	
	}
	socket.emit("join_public",user)
})
socket.on("test_server",(data)=>{
	console.log("the data is",data)
})

socket.on("anonymous_join",(data)=>{
	console.log(`this person has joined ${data.name}`)
	console.log("joined public channel")
})


socket.on("receive_message",(data)=>{
	let messages=document.querySelector(".messages")
	let {user,message}=data
    
      messages.innerHTML+=`<p>${user}:${message}</p>`

})

socket.on("room_message",(data)=>{
	console.log("room has received data")
	console.log(data)
})

// events disconnection
socket.on("disconnect",(reason)=>{
	if (reason=="io server disconnect"){
		socket.connect()
	}
	// else the socket will automatically try to reconnecy
})


function test_func(){
	let btn=document.querySelector(".btn-single")
	btn.addEventListener("click",()=>{

		socket.emit("greeting",{email:"alexanderkabua@gmail.com",password:"1234567"})
		console.log("calling it in frontend")
	})
}
document.querySelectorAll(".rooms").forEach((room)=>{
	room.addEventListener("click",(e)=>{
		join_room(e)
	})
})

function join_room(e){
	console.log(e)
	console.log("called function")
	room_data={
		room:e.target.innerText.trim(),
		user:socket.id
	}

	console.log(room_data)
	socket.emit("join",{room_data})
}


function anony_message(anony,message){
	messages={
		user:anony,
		message

	}

	socket.emit("anony_message",messages)
}




test_func()
