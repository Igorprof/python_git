console.log('задание 2');
function countBasketPrice(goods) {
    let totalPrice = 0.0;
    for (const good of goods) {
        totalPrice += good[1]*good[2];
    }
    return totalPrice;
}

const backet = [ // товары - массив из 3 элементов:название, количество, цена за 1 шт.
    ['Конструктор Лего мал.', 2, 1200], 
    ['Машинка радиуправляемая speedX', 1, 3200], 
    ['Аккумуляторы LiOH упаковка по 4 шт.', 4, 250], 
    ['Электронный конструктор', 1, 6700]
] 

let price = countBasketPrice(backet);
console.log(price);
