const quotes = [
    {
        quote: "어려움은 새로운 아이디어를 개발하는 것이 아니라 옛 것으로부터 벗어나는 것이다",
        author: "존 매이너드 케인스",
    },
    {
        quote: "스스로 상상하지 못하는 일은 결코 이루지 못할 것이다",
        author: "카렌 포드",
    },
    {
        quote: "좋은 생각과 행동은 결코 나쁜 결과를 낳을 수 없다 나쁜 생각과 행동은 결코 좋은 결과를 낳을 수 없다",
        author: "제임스 앨런",
    },
    {
        quote: "우리는 오늘 우리의 생각이 데려다 놓은 자리에 존재한다. 우리는 내일 우리의 생각이 데려다 놓을 자리에 존재할 것이다",
        author: "제임스 앨런",
    },
    {
        quote: "좋은 충고를 받아들이는 것은 자신의 능력을 키우는 것이다",
        author: "요한 볼프강 괴테",
    },
    {
        quote: "행동의 가치는 그 행동을 끝까지 이루는 데 있다",
        author: "칭기즈칸",
    },
    {
        quote: "흔들리지 않고 피는 꽃이 어디 있으랴",
        author: "도종환",
    },
    {
        quote: "목적 없는 공부는 기억에 해가 될 뿐이며, 머릿속에 들어온 어떤 것도 간직하지 못한다",
        author: "레오나르도 다빈치",
    },
    {
        quote: "젊었을 때 배움을 게을리한 사람은 과거를 상실하며 미래도 없다",
        author: "에우리피데스",
    },
    {
        quote: "교육의 목적은 인격의 형성이다",
        author: "허버트 스펜서",
    },
]

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];

// Math.round(1.1); // 반올림
// Math.ceil(1.1); // 올림
// Math.floor(1.9) // 내림
// quotes.length // 배열 길이 반환

quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;