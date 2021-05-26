function CategoriesActive(e){
  let categories = document.querySelectorAll('.categories_one')
  for (var i = 0; i < categories.length; i++) {
    categories[i].classList.remove('active')
  }
  e.classList.add('active')
}

function Authorize(){
  let password = document.getElementById('password').value;

  if(password == 'admin'){
    window.location.href = './admin_editstore.html';
  }
  if(password == 'client'){
    window.location.href = './store_authorization.html';
  }

}
