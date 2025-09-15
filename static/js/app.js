/* particlesJS.load(@dom-id, @path-json, @callback (optional)); */



const menuBtn = document.getElementById("menu-btn");
const navLinks = document.getElementById("nav-links");
const menuBtnIcon = menuBtn.querySelector("btn3");

menuBtn.addEventListener("click", (e) => {
  navLinks.classList.toggle("open");

  const isOpen = navLinks.classList.contains("open");
  menuBtnIcon.setAttribute("class", isOpen ? "ri-close-line" : "ri-menu-line");
});

navLinks.addEventListener("click", (e) => {
  navLinks.classList.remove("open");
  menuBtnIcon.setAttribute("class", "ri-menu-line");
});

function grid_col3_btn2() {
  var leftPos = $('#ul-1').scrollLeft() + 200;
  console.log("grid_col3_btn1", leftPos);
  $('#ul-1').scrollLeft(leftPos);

}

function grid_col3_btn1() {
  var leftPos = $('#ul-1').scrollLeft() - 200;
  console.log("grid_col3_btn1", leftPos);
  $('#ul-1').scrollLeft(leftPos);

}

const scrollRevealOption = {
  distance: "50px",
  origin: "bottom",
  duration: 1000,
};



ScrollReveal().reveal(".hero .hero-header", {
  ...scrollRevealOption,
});

ScrollReveal().reveal(".section", {
  duration: 2000,
  interval: 1000,
});

ScrollReveal().reveal(".section-head-line", {
  duration: 2000,
  interval: 1000,
});

ScrollReveal().reveal(".grid-item", {
  delay: 500,
  duration: 1000,
  interval: 500,
});



ScrollReveal().reveal(".form-table", {
  delay: 500,
  duration: 1000,
  interval: 500,
});

ScrollReveal().reveal(".form-button", {
  delay: 500,
  duration: 1000,
  interval: 500,
});