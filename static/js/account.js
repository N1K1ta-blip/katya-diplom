let selector_count1 = 0;
function Selector_profile(e){
  let thisValue = e.getAttribute('data-value')
  let carousel_item = document.querySelectorAll('.account_carousel')
  if(thisValue != selector_count1){
    let allSelectorAction = document.querySelectorAll('.account__selector_item_active')
    allSelectorAction[0].classList.remove('account__selector_item_active')
    e.classList.add('account__selector_item_active')

    for (var i = 0; i < carousel_item.length; i++) {
      if(carousel_item[i].getAttribute('data-value') == thisValue){
        carousel_item[selector_count1].classList.remove('active')
        carousel_item[i].classList.add('active')
      }
    }

    selector_count1 = thisValue
  }
}
