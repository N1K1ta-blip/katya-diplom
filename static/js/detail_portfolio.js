function Carousel(e, id, counter) {
  let corousel = document.getElementById('portfolio_slider'+ id.toString());
  let img = document.querySelectorAll('.carousel-item'+ id.toString());
  let x = e.getAttribute('data-value');
  console.log(img[counter-1])
  console.log(counter)
  for (let i = 0; i < counter; i++) {
      img[i].classList.remove('active');
  }
  img[counter-1].classList.add('active')
  corousel.style.display = 'block'
}

document.addEventListener('keydown', function(e) {
    let keyCode = e.keyCode;
    let corousel = document.getElementById('portfolio_slider')
    if (keyCode === 27) {//keycode is an Integer, not a String
      corousel.style.display = 'none'
    }
});

function Close(id) {
  let corousel = document.getElementById('portfolio_slider'+ id.toString())
  corousel.style.display = 'none'
}
