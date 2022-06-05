const navBar = document.querySelector(".navlinks");
const menu = document.querySelector(".hamburger");
const commentSection = document.querySelector(".comment_sec");

if (navBar) {
  menu.addEventListener("click", () => {
    navBar.classList.toggle("active");
  });
}

function commentbox() {
  commentSection.style.display = "block";
}
