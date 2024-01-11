const icon = document.querySelector('.icon_search_name')
const search = document.querySelector('.search')
const input = document.querySelector('.input_search')
const clear = document.querySelector('.clear')

console.log(icon)
icon.onclick = function() {
    search.classList.toggle('active_search')
    input.classList.toggle('input_search_active')
    clear.classList.toggle('clear_active')

}