alert('задание 8');
function power(val, pow) {
    if (pow == 1) {
        return val
    }
    return val * power(val, pow - 1)
}

alert(power(5, 3))
alert(power(2, 3))
alert(power(3, 4))
