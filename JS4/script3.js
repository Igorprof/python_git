console.log('задание 3');
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
    totalPrice() {
        return this.goods.reduce((total, cur) => total + cur.price*cur.quantity, 0);
    }
}

console.log(backet.totalPrice());

