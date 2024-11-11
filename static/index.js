console.log("hello world");
var hd=document.querySelector('#hid')
console.log(hd.value);



function getid(id){
    hd.value=id
    console.log(hd.value);
}


var a=document.querySelector('#hide')
var b=document.getElementById('updated-name')
var c=document.getElementById('updated-email')
var d=document.getElementById('updated-number')
console.log(a,b,c,d);

function passing(id,name,email,contact){
    console.log("this is function call");
    
    a.value=id
    console.log("id :",a.value);
    
    b.value = name;
    console.log("name:",b.value);

    
    
    c.value = email; 
    console.log("email:",c.value);
    
    d.value = contact;
    console.log("contact:",d.value);

}

var moon=document.querySelector('#moon')
var bd=document.querySelector('body')
moon.addEventListener('click',()=>{
    if(bd.classList.contains('dark-mode')){
        bd.classList.remove('dark-mode')

    }else{
        bd.classList.add('dark-mode')
        bd.style.transition="3s"
    }
})