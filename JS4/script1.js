console.log('задание 1');
function getObj(num) {
    if (num > 999) {
        console.log('Число слишком большое!');
        return {};
    }
    const names = ['единицы', 'десятки', 'сотни'];
    let i = 0;
    const resObj = {};
    while (num > 0) {
        resObj[names[i]] = num % 10;
        num = Math.floor(num / 10);
        i++;
    }
    return resObj;
}

console.log(getObj(543));
console.log(getObj(12));
console.log(getObj(679));
console.log(getObj(1001));