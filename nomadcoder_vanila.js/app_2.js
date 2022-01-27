// const title = document.getElementById("title");
// title.innerText = "Got you!";
// console.log(title.id);
// console.log(title.className);

// const title = document.getElementsByClassName("hello");
// console.log(title);
const title = document.querySelector(".hello h1");
// const title = document.querySelectorAll(".hello h1:first-child");
console.log(title);
title.innerText = "hello!";

title.style.color = "blue";

function handleTitleClick(){
    // console.log("title was clicked!");
    title.style.color = "white";
}
function handleTitleHover(){
    title.style.color = "red";
}
function handleTitleOut(){
    title.style.color = "green";
}
title.addEventListener("click", handleTitleClick);
title.addEventListener("mouseover", handleTitleHover);
title.addEventListener("mouseout", handleTitleOut);

// 마크업 태그의 궁금한 점이 있다면
// 태그명 HTML element mdn 구글링
function handleTitleEnter(){
    title.innerText = "Mouse is here!";
}
title.addEventListener("mouseenter", handleTitleEnter);

function handleTitleLeave(){
    title.innerText = "Mouse is gone!";
}
title.addEventListener("mouseleave", handleTitleLeave);

function handleWindowResize() {
    document.body.style.backgroundColor = "tomato";
}

window.addEventListener("resize", handleWindowResize);

function handleWindowCopy() {
    alert("Copier!");
}

window.addEventListener("copy", handleWindowCopy);
window.addEventListener("offline", handleWindowOffline);
window.addEventListener("online", handleWindowOnline);
function handleWindowOffline() {
    alert("SOS no WIFI");

}
function handleWindowOnline() {
    alert("ALL GOOD!");
}

const h1 = document.querySelector("div.hello2 h1");

function handleTitleClick_2(){
    // if(h1.style.color === "blue"){
    //     h1.style.color = "tomato";
    // } else {
    //     h1.style.color = "blue";
    // }
    const currendColor = h1.style.color;
    let newColor;
    if(currendColor === "blue"){
        newColor = "tomato";
    } else {
        newColor = "blue";
    }
    h1.style.color = newColor;
}

h1.addEventListener("click", handleTitleClick_2);