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

  // 지난 달 마지막 일과 요일
  const PLday = preLastDate.getDate();
  const PLweek = preLastDate.getDay();

  // 이번 달 마지막 일과 요일
  const TLday = thisLastDate.getDate();
  const TLweek = thisLastDate.getDay();


  const preDays = []; // 지난 달 남는 일자 담기
  const thisDays = [...Array(TLday + 1).keys()].slice(1); // 이번 달 일자 담기
  const nextDays = []; // 다음 달 이른 일자 담기

  // 지난 마지막 요일이 일요일이 아니면 나머지 요일 개수만큼 후방 일자 추가
  if (PLweek !== 6) {
    for (let i = 0; i < PLweek + 1; i++) {
      preDays.unshift(PLday - i);
    }
  }

  // 이번 달 마지막 요일 뺀 나머지만큼 다음 달 이른 일자 추가
  for (let i = 1; i < 7 - TLweek; i++) {
    nextDays.push(i);
  }

  // 모든 일자 결합
  const dates = preDays.concat(thisDays, nextDays);

  // 지난 달 남은 일자와 다음 달 이른 일자 구분 위한 변수 초기화
  const firstDateIndex = dates.indexOf(1);
  const lastDateIndex = dates.lastIndexOf(TLday);

  // 이번 달과 아닌 달 클래스 구분(CSS 위함)
  dates.forEach((date, i) => {
    const condition = i >= firstDateIndex && i < lastDateIndex + 1
      ? 'this'
      : 'other';
    dates[i] = `<div class="day ${condition}">${date}</div>`;
  })

  // 날짜 추가
  document.querySelector('.days').innerHTML = dates.join('');

  // 오늘 날짜 강조 CSS 위한 변수 초기화
  const today = new Date();

  // 이번 달과 연도가 오늘 일자의 달, 연도와 같으면 'this' 클래스의 date 뽑아냄
  if (currentMonth === today.getMonth() && currentYear === today.getFullYear()) {
    for (let date of document.querySelectorAll('.this')) {
      // +date = 타입을 number로 캐스팅해주는 단항 연산자
      // date 태그의 텍스트와 오늘 일자가 같으면 'today' 클래스 추가하고 반복문 탈출
      if (+date.innerText === today.getDate()) {
        date.classList.add('today');
        break;
      }
    }
  }
}

renderingDate();

// 지난 달 이동 버튼 이벤트
function preMonth() {
  // 해당 월 첫째날로 이동
  // 단순히 월로 계산하면 마지막 일자가 일치하지 않는 달(ex. 8월 31일!==9월 30일)은 건너뛰는 버그 발생 => 예방하기 위함
  date.setDate(1);
  date.setMonth(date.getMonth() - 1);
  renderingDate();
}

// 다음 달 이동 버튼 이벤트
function nextMonth() {
  date.setDate(1);
  date.setMonth(date.getMonth() + 1);
  renderingDate();
}

// 이번 달 이동 버튼 이벤트
function goToday() {
  date = new Date();
  renderingDate();
}

preBtn.addEventListener("click", preMonth);
curBtn.addEventListener("click", goToday);
nextBtn.addEventListener("click", nextMonth);