const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");
const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username";
// const loginButton = document.querySelector("#login-form button");

// function onLogBtnClick(){
//     const username = loginInput.value;
//     // if (username === "") {
//     //     console.log("Please write your name.")
//     // } else if(username.length > 15) {
//     //     alert("Your name is too long.")
//     // }
//     console.log(username);
// }
function onLoginSubmit(event) {
    event.preventDefault(); // 기본 동장 실행 방지
    loginForm.classList.add(HIDDEN_CLASSNAME);
    const username = loginInput.value;
    localStorage.setItem(USERNAME_KEY, username);
    // greeting.innerText = "Hello " + username;
    // greeting.innerText = `Hello ${username}`; // ``(백틱)
    // greeting.classList.remove(HIDDEN_CLASSNAME);
    paintGreeings(username);

}

// loginButton.addEventListener("click", onLogBtnClick);

function paintGreeings(username){
    greeting.innerText = `Hello ${username}`;
    greeting.classList.remove(HIDDEN_CLASSNAME);
}

// const link = document.querySelector("a");
// function handleLinkClick(event){
//     event.preventDefault();
//     console.dir(event);
// }
// link.addEventListener("click", handleLinkClick);

// localStorage.setItem("username", username); // 키, 값 입력
// console.log(localStorage.getItem("username")); // 값 불러오기
// localStorage.removeItem("username"); // 키 제거
// console.log(localStorage.getItem("username"));

const savedUsername = localStorage.getItem(USERNAME_KEY);
if (savedUsername === null) {
    loginForm.classList.remove(HIDDEN_CLASSNAME);
    loginForm.addEventListener("submit", onLoginSubmit);
} else {
    paintGreeings(savedUsername);
}
