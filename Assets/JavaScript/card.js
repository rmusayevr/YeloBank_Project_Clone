let button1 = document.getElementById("firstb")
let button2 = document.getElementById("secondb")
let div1 = document.getElementById("firstd")
let div2 = document.getElementById("secondd")

button1.addEventListener('click', function() {
    if (!div2.classList.contains('d-none')) {
        div2.classList.add('d-none')
    }
    div1.classList.remove('d-none')
    button1.classList.add('b-bottom')
    button2.classList.remove('b-bottom')
})
button2.addEventListener('click', function() {
    if (!div1.classList.contains('d-none')) {
        div1.classList.add('d-none')
    }
    div2.classList.remove('d-none')
    button2.classList.add('b-bottom')
    button1.classList.remove('b-bottom')
})