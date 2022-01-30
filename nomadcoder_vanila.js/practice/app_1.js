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

const me= "sexy";
const day = [1, 2, false, true, undefined, null, "text", me];
console.log(day);
day[2] = "angel";
console.log(day);
day.push("devil");
console.log(day);

player.sexy = "soon";
console.log(player);

//return
const age = 96;
function calculateKrAge(ageOfForeigner) {
    return ageOfForeigner + 2;
}

const krAge = calculateKrAge(age);
console.log(krAge);

const calculator = {
    plus: function(a, b){
        return a + b
    },
    minus: function(a, b){
        return a - b
    },
    multiple: function(a, b){
        return a * b
    },
    divide: function(a, b){
        return a / b
    },
    power: function(a, b){
        return a ** b
    },
};

const plusResult = calculator.plus(1, 2);
const minusResult = calculator.minus(plusResult, 1);
const multiResult = calculator.multiple(10, minusResult);
const divideResult = calculator.divide(multiResult, minusResult);
const powerResult = calculator.power(divideResult, 3)

console.log("plus = ", plusResult);
console.log("minus = ", minusResult);
console.log("multiple = ", multiResult);
console.log("divide = ", divideResult);
console.log("power = ", powerResult);
console.log("-------------------------------------");

const yourAge = parseInt(prompt("How old are you?"));
//console.log(typeof "15", typeof parseInt("15"));
//console.log(yourAge, parseInt(yourAge));
console.log(yourAge);

console.log(isNaN(yourAge));

if(isNaN(yourAge) || yourAge < 0) {
    console.log("Please write a real positive number");
} else if(yourAge < 18) {
    console.log("You are too young");
} else if(yourAge >= 18 && yourAge <= 50){
    console.log("You can drink");
} else if(yourAge > 50 && yourAge <= 80) { 
    console.log("You should exercise");
} else if (yourAge > 80) {
    console.log("You can do whatever you want");
} 