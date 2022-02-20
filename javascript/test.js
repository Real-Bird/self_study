const nonClick = document.getElementsByClassName("non-click");

// div 클릭 시 해당 영역 외 기본 색 참고
// https://liufeier.tistory.com/22

function handleClick(event) {
  for (let i = 0; i < nonClick.length; i++) {
    nonClick[i].classList.remove("click");
    // div에서 모든 "click" 클래스 제거
  }
  event.target.classList.add("click");
  // 클릭한 div만 "click"클래스 추가
}

for (let i = 0; i < nonClick.length; i++) {
  nonClick[i].addEventListener("click", handleClick);
}

