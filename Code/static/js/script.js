let link1=document.getElementById("link1");
let f1=document.getElementById("f1");
let explain1=document.getElementById("explain");
let f2=document.getElementById("f2");
let link2=document.getElementById("link2");
let explain2=document.getElementById("explain2");
let back=document.getElementById("back");

link1.addEventListener('mouseenter', event => {
	link1.style.color="#330662";
	explain1.style.display="block";
	document.body.style.cursor="pointer";
	
})

link1.addEventListener('mouseleave', event => {
	link1.style.color="#000000";
	explain1.style.display="none";
	
})
link1.addEventListener('click', event => {
	link2.style.color="#330662";
	explain1.style.display="block";
	f2.style.display="none";
	explain2.style.display="none";
	back.style.display="block";
	
})


link2.addEventListener('mouseenter', event => {
	link2.style.color="#330662";
	explain2.style.display="block";
	document.body.style.cursor="pointer";
	
})

link2.addEventListener('mouseleave', event => {
	link2.style.color="#000000";
	explain2.style.display="none";
	
})
link2.addEventListener('click', event => {
	link2.style.color="#330662";
	explain2.style.display="block";
	f1.style.display="none";
	explain1.style.display="none";
	back.style.display="block";
	
})
back.addEventListener('click', event => {
	link1.style.color="black";
	link2.style.color="black";
	explain2.style.display="none";
	f1.style.display="block";
	f2.style.display="block";
	// link1.style.display="block";
	explain1.style.display="none";
	back.style.display="none";
	
})