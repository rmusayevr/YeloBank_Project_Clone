$("#menu_button").click( function() {
    if ($(".not-menu").hasClass("d-flex")) {
      $(".not-menu").addClass("d-none");
      $(".not-menu-main").addClass("d-none");
      $(".not-menu").removeClass("d-flex");
      $(".display-none").removeClass("d-none");
      $(".display-none").addClass("d-flex");
      $("#menu_button").html(`<i class="bi bi-x-lg"></i>`) 
    }
    else if ($(".not-menu").hasClass("d-none")) {
      $(".not-menu").removeClass("d-none");
      $(".not-menu-main").removeClass("d-none");
      $(".not-menu").addClass("d-flex");
      $(".display-none").addClass("d-none");
      $(".display-none").removeClass("d-flex");
      $("#menu_button").html(`<i class="bi bi-list"></i>`)
    }
  });
  
let firstNavbar = document.querySelector(".first-navbar")
let secondNavbar = document.querySelector(".second-navbar")

var lastScrollTop = 0;

window.addEventListener("scroll", function(){ 
   var st = window.pageYOffset || document.documentElement.scrollTop; 
   if (st > lastScrollTop){
    $(".first-navbar").addClass("d-none")
    secondNavbar.style.backgroundColor = "white"
    secondNavbar.style.paddingTop = "10px"
    $("#internet_bank").addClass("d-none")
   } 
   else if (st == 0 ) {
    secondNavbar.style.backgroundColor = 'transparent'
    secondNavbar.style.paddingTop = "50px"
   }
   else {
    secondNavbar.style.paddingTop = "50px"
    $(".first-navbar").removeClass("d-none")
    secondNavbar.style.backgroundColor = "white"
    $("#internet_bank").removeClass("d-none")
   }
   lastScrollTop = st <= 0 ? 0 : st; 
}, false);