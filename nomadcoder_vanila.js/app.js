function add(){
    let c = a + b
    console.log(c)    
}

let a = document.getElementById("num_1")
let b = document.getElementById("num_2")

let d = document.getElementById("btn")

d.addEventListener("click", add)