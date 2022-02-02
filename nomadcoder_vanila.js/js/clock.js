const clock = document.querySelector("#clock");
const fullDate = document.querySelector("#fulldate");
// function sayHello(){
//     console.log("hello");
// }

// setInterval(sayHello, 5000); // 반복할 함수, 실행 주기 ms단위(1000ms = 1s)

// setTimeout(sayHello, 5000); // 실행할 함수, 실행될 시간

function getFullDate() {
    const toDayDate = new Date();
    const year = String(toDayDate.getFullYear());
    const month = String(toDayDate.getMonth() + 1);
    const day = String(toDayDate.getDay());
    fullDate.innerText = `${year}년 ${month}월 ${day}일`;
}

function getClock() {
    const date = new Date();
    const hours = String(date.getHours()).padStart(2, "0");
    const minutes = String(date.getMinutes()).padStart(2, "0");
    const seconds = String(date.getSeconds()).padStart(2, "0");
    clock.innerText = `${hours} : ${minutes} : ${seconds}`;
}

getFullDate();
getClock();
setInterval(getClock, 1000);

// "1".padStart(2,"0") // padStart(문자 개수, 패딩 문자) => 문자열의 개수가 1파라미터와 맞지 않으면 문자열 앞자리에 2파라미터를 추가함