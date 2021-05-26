function Plus(e){
 let count = document.getElementsByClassName('cart_count')[0].value
 count = Number(count)
 count++
 count = String(count)
 document.getElementsByClassName('cart_count')[0].value = count
}
 
function Minus(e){
 let count = document.getElementsByClassName('cart_count')[0].value
 count = Number(count)
 count--
 count = String(count)
 document.getElementsByClassName('cart_count')[0].value = count
}
document.getElementById('id')
