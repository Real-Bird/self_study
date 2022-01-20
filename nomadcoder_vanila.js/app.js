// funcion 이해하기

function sayHello() {
    console.log("Hello World!");
}

sayHello();
console.log("hi");
sayHello("jin");

function sayHi(nameOfPerson, age) {
    console.log("Hi, my name is " + nameOfPerson + " and I'm " + age);
}

sayHi("Jin");
sayHi("cen", 12);

function plus(firstNumber, secondNumber) {
    console.log(firstNumber + secondNumber);
}

function divide(a, b){
    console.log(a / b);
}

plus();
plus(8, 60);
divide(128, 2);

const player = {
    name : "jin",
    sayHello : function(otherPersonsName){
        console.log("hello " + otherPersonsName + " nice to meet you");
    }
}
console.log(player.name);
player.sayHello("lynn");
