import '../styles/Cart.css'

class Plant {
  constructor(name,price) {
    this.name = name;
    this.price = price;
  }
}

function Cart() {
  let plant1 = new Plant("Forcisia",12.50);
  let plant2 = new Plant("Lierre",6);
  let plant3 = new Plant("Flowers",18.90);
  let cart = [plant1,plant2,plant3];
  
  let cartCount = 0;
  for (let i=0; i<cart.length; i++) {
    cartCount += cart[i].price;
  }
  return (<div id="cart"><p id="cartTitle">Votre panier</p>
      <ul>
        <li>{plant1.name+' / '+plant1.price.toFixed(2)+' €'}</li>
        <li>{plant2.name+' / '+plant2.price.toFixed(2)+' €'}</li>
        <li>{plant3.name+' / '+plant3.price.toFixed(2)+' €'}</li>
      </ul><p id="total">{'Total = '+cartCount.toFixed(2)+' €'}</p></div>)
}

export default Cart