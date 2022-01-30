const h1 = document.querySelector("div.hello h1");

// function handleTitleClick(){
//     const clickedClass = "active";
//     // if (h1.className === clickedClass){
//     //     h1.className = "";    
//     // } else{
//     //     h1.className = clickedClass;
//     // }
//     if (h1.classList.contains(clickedClass)){
//         h1.classList.remove(clickedClass);    
//     } else{
//         h1.classList.add(clickedClass);
//     }
// }

function handleTitleClick(){
    h1.classList.toggle("active");
}

h1.addEventListener("click", handleTitleClick);