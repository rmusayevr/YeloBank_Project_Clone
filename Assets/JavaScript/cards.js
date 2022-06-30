let span1 = document.getElementById("span1")
let span2 = document.getElementById("span2")
let span3 = document.getElementById("span3")

span2.addEventListener('click', function() {
    span1.classList.add("display-none")
    span2.classList.add("display-none")
    span3.classList.remove("display-none")
})