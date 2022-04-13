const img_container = document.querySelector(".container");
const img_box__btn = document.querySelectorAll(".img_box__btn");
const img_box = document.querySelectorAll(".img_box");
let currentIndex = 0;
const slideCnt = img_box.length;

const prev_btn = document.querySelector(".prev_btn");
const next_btn = document.querySelector(".next_btn");

next_btn.addEventListener("click", () => {
  if (currentIndex >= slideCnt - 1) {
    img_box.forEach((item) => (item.style.transform = "translateX(0%)"));
    currentIndex = -1;
  }
  img_box[(currentIndex + 1) % slideCnt].style.transform = `translateX(-${
    100 * (currentIndex + 1)
  }%)`;
  currentIndex += 1;
});

prev_btn.addEventListener("click", () => {
  if (currentIndex <= 0) {
    img_box[slideCnt - 1].style.transform = `translateX(-${
      100 * (slideCnt - 1)
    }%)`;
    currentIndex = slideCnt - 1;
  } else {
    img_box[(currentIndex + 1) % slideCnt].style.transform = `translateX(-${
      100 * (currentIndex + 1)
    }%)`;
    currentIndex -= 1;
  }
});
