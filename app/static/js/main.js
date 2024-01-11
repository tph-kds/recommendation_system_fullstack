let left_btn = document.getElementsByClassName("btn-left")[0];
let right_btn = document.getElementsByClassName("btn-right")[0];
let cards = document.getElementsByClassName("shop_cards")[0];
console.log(cards.scrollLeft)

left_btn.addEventListener("click", () => {
    cards.scrollLeft -= 262;
})


right_btn.addEventListener("click", () => {
    cards.scrollLeft += 262;
})

function showText() {
    document.getElementById("hidden-text").style.opacity = "1";
}


function hideText() {
    document.getElementById("hidden-text").style.opacity = "0";
}
// chuyển động giữa các số

// const arrowButtonLeft = document.getElementById("arrowButtonLeft");
// const arrowButtonRight = document.getElementById("arrowButtonRight");
// const elementToToggle = document.querySelectorAll(".elementToToggle");

// linksContainer.addEventListener("click", function(event) {
//     if (event.target.classList.contains("elementToToggle")) {
//       const allLinks = linksContainer.querySelectorAll(".elementToToggle");
//       allLinks.forEach(link => link.classList.remove("is_active"));
      
//       event.target.classList.add("is_active");
//     }
//   });
  
const arrowButtonLeft = document.getElementById("arrowButtonLeft");
const arrowButtonRight = document.getElementById("arrowButtonRight");
const elementToToggle = document.querySelectorAll(".elementToToggle");

let activeIndex = 0; // Chỉ số của phần tử được chọn (bắt đầu từ 0)

function setActive(index) {
    elementToToggle.forEach(element => {
        element.classList.remove("is_active");
    });
    elementToToggle[index].classList.add("is_active");
}

arrowButtonLeft.addEventListener("click", function() {
    if (activeIndex > 0) {
        activeIndex--;
        setActive(activeIndex);
    }
});

arrowButtonRight.addEventListener("click", function() {
    if (activeIndex < elementToToggle.length - 1) {
        activeIndex++;
        setActive(activeIndex);
    }
});

const arrowButtonLeft1 = document.getElementById("arrowButtonLeft1");
const arrowButtonRight1 = document.getElementById("arrowButtonRight1");
const elementToToggle1 = document.querySelectorAll(".elementToToggle1");
  //#endregion  let activeIndex = 0; // Chỉ số của phần tử được chọn (bắt đầu từ 0)

let activeIndex1 = 0; 

function setActive1(index) {
    elementToToggle1.forEach(element => {
        element.classList.remove("is_active");
    });
    elementToToggle1[index].classList.add("is_active");
}

arrowButtonLeft1.addEventListener("click", function() {
    if (activeIndex1 > 0) {
        activeIndex1--;
        setActive1(activeIndex1);
    }
});

arrowButtonRight1.addEventListener("click", function() {
    if (activeIndex1 < elementToToggle1.length - 1) {
        activeIndex1++;
        setActive1(activeIndex1);
    }
});

const icon = document.querySelector('.icon_search')
const search = document.querySelector('.search')
const input = document.querySelector('.input_search')
console.log(icon)
icon.onclick = function() {
    search.classList.toggle('active_search')
    input.classList.toggle('input_search_active')
}