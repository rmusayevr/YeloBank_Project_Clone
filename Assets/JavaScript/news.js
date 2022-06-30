const showMore = document.getElementById("show_more");
showMore.addEventListener("click", function() {
   let all_d_none = document.querySelectorAll(".display_none_for_jinja");
   for(let i = 0; i <= all_d_none.length; i++) {
      if (i < 6) {
         console.log( all_d_none[i]);
         all_d_none[i].classList.remove("d-none");
         all_d_none[i].classList.remove("display_none_for_jinja");
      }
   }
}) 