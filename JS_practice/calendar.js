const root = document.getElementById("root");
const yearMonth = document.querySelector(".year-month");
const calendar = document.querySelector("#calendar");
const preBtn = document.querySelector(".prebtn");
const curBtn = document.querySelector(".curbtn");
const nextBtn = document.querySelector(".nextbtn");

let date = new Date();

function renderingDate() {

  const currentYear = date.getFullYear();
  const currentMonth = date.getMonth();

  yearMonth.innerText = `${currentYear}년 ${currentMonth + 1}월`

  const preLastDate = new Date(currentYear, currentMonth, 0)
  const thisLastDate = new Date(currentYear, currentMonth + 1, 0)

  // 지난 달 마지막 일
  const PLday = preLastDate.getDate();
  const PLweek = preLastDate.getDay();

  // 이번 달 마지막 일
  const TLday = thisLastDate.getDate();
  const TLweek = thisLastDate.getDay();

  // 지난 달 
  const preDays = [];
  const thisDays = [...Array(TLday + 1).keys()].slice(1);
  const nextDays = [];

  if (PLweek !== 6) {
    for (let i = 0; i < PLweek + 1; i++) {
      preDays.unshift(PLday - i);
    }
  }

  for (let i = 1; i < 7 - TLweek; i++) {
    nextDays.push(i);
  }

  const dates = preDays.concat(thisDays, nextDays);

  const firstDateIndex = dates.indexOf(1);
  const lastDateIndex = dates.lastIndexOf(TLday);

  dates.forEach((date, i) => {
    const condition = i >= firstDateIndex && i < lastDateIndex + 1
      ? 'this'
      : 'other';
    dates[i] = `<div class="day ${condition}">${date}</div>`;
  })

  document.querySelector('.days').innerHTML = dates.join('');

  const today = new Date();

  if (currentMonth === today.getMonth() && currentYear === today.getFullYear()) {
    for (let date of document.querySelectorAll('.this')) {
      if (+date.innerText === today.getDate()) {
        date.classList.add('today');
        break;
      }
    }
  }
}

renderingDate();

function preMonth() {
  date.setDate(1);
  date.setMonth(date.getMonth() - 1);
  renderingDate();
}

function nextMonth() {
  date.setDate(1);
  date.setMonth(date.getMonth() + 1);
  renderingDate();
}

function goToday() {
  date = new Date();
  renderingDate();
}

preBtn.addEventListener("click", preMonth);
curBtn.addEventListener("click", goToday);
nextBtn.addEventListener("click", nextMonth);