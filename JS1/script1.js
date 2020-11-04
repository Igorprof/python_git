function convertCToF(C) {
    return (9 / 5) * Tc + 32
}

let Tc = +prompt('Введите температуру в градусах Цельсия')
let Tf = convertCToF(Tc)
alert('Температура по Фаренгейту равна ' + Tf)