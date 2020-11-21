const cart = {
    cartBlock: null,
    clearButton:null,
    goods: [], 
    init() {
        this.cartBlock = document.querySelector('.cartBlock');
        this.clearButton = document.querySelector('.clearBtn');
        this.clearButton.innerText = 'Очистить';
        this.clearButton.addEventListener('click', this.clearCart.bind(this));

        this.render();
    },
    render() {
        if (this.goods.length > 0) {
            this.cartBlock.innerText = `В корзине: ${this.getTotalQuantity()} товаров на сумму ${this.getCartPrice()} рублей`
        } else {
            this.cartBlock.innerText = 'Корзина пуста';
        }
    }, 
    getCartPrice() {
        return this.goods.reduce((total, cur) => total + cur.price*cur.quantity, 0);
    }, 
    getTotalQuantity() {
        return this.goods.reduce((total, cur) => total + cur.quantity, 0)
    },
    clearCart() {
        this.goods = [];
        this.render();
    }
};

const good = {
    cart,
    goodElement: null,
    goodBLocks: [],
    goods: [
        {
            name: 'Конструктор Лего мал.',
            price: 1200,
            quantity: 1,
        },
        {
            name: 'Машинка радиуправляемая speedX',
            price: 3200,
            quantity: 1,
        },
        {
            name: 'Аккумуляторы LiOH упаковка по 4 шт.',
            price: 250,
            quantity: 1,
        },
        {
            name: 'Электронный конструктор',
            price: 6700,
            quantity: 1,
        }
    ],
    init() {
        this.goodElement = document.getElementById('goods');
        for (const good of this.goods) {
            const block = document.createElement('div');
            block.classList.add('goodBlock');

            const pName = document.createElement('p');
            pName.classList.add('goodName');
            pName.innerText = good.name;

            const pPrice = document.createElement('p');
            pName.classList.add('goodPrice');
            pPrice.innerText = String(good.price);

            const buyBtn = document.createElement('button');
            buyBtn.classList.add('buyBtn');
            buyBtn.innerText = 'Купить';
            buyBtn.addEventListener('click', () => this.buy(good));

            block.appendChild(pName);
            block.appendChild(pPrice);
            block.appendChild(buyBtn);
            this.goodBLocks.push(block);
            this.goodElement.appendChild(block);
        }
        this.cart.init();
    }, 
    buy(g) {        
        const oldGood = this.cart.goods.find(gCur => gCur.name == g.name);
        if (oldGood) {
            oldGood.quantity += 1;
        } else {
            this.cart.goods.push({...g});
        }        
        this.cart.render();
    }
}

// cart.init();
good.init();
// const checkBtn = document.getElementById('check');
// checkBtn.addEventListener('click', () => {
//     console.log(cart.goods);
//     console.log(good.goods);
// })