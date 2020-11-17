const backet = {
    goods: [
        {
            name: 'Конструктор Лего мал.',
            price: 1200,
            quantity: 2,
        },
        {
            name: 'Машинка радиуправляемая speedX',
            price: 3200,
            quantity: 1,
        },
        {
            name: 'Аккумуляторы LiOH упаковка по 4 шт.',
            price: 250,
            quantity: 4,
        },
        {
            name: 'Электронный конструктор',
            price: 6700,
            quantity: 1,
        }
    ], 
    isEmpty() {
        return (this.goods.length === 0)
    }, 
    totalPrice() {
        return this.goods.reduce((total, cur) => total + cur.price*cur.quantity, 0);
    }, 
    totalQuantity() {
        return this.goods.reduce((total, cur) => total + cur.quantity, 0)
    }
}

const backetDiv = document.getElementById('backet');
if (backet.isEmpty()) {
    backetDiv.innerText = 'Корзина пуста';
} else {
    backetDiv.innerText = `В корзине: ${backet.totalQuantity()} товаров на сумму ${backet.totalPrice()} рублей`;
}

