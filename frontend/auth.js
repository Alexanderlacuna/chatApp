
function set_url(){
	let url='http://127.0.0.1:5000'
	return url
}

function register(username,email,password){
	url=`${set_url()}/register`
	const response=await fetch(url,{
		methods:"POST",
		headers:{
			"Content-Type":"application/json"
		}
		body:{username,email,password}

	})

 
}



function login_validator({username,password}){
}

function  email_validator(email){

}


async function login(email,password){
url=`${set_url()}/login`
const response=await fetch(url,{
	method:"POST",
	headers:{
		      'Content-Type': 'application/json'
	},
	body:JSON.stringify({email,password})
})


	
}


