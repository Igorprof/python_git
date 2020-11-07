alert('задание 6');
function sum(a, b) {
    return a + b;
}

function diff(a, b) {
    return a - b;
}

function mult(a, b) {
    return a*b;
}

function div(a, b) {
    if (b != 0) {
        return a / b;
    } else {
        return 0;
    }
}

function mathOperation(arg1, arg2, operation) {
    switch (operation) {
        case '+':
            return sum(arg1, arg2);
            break;
        case '-':
            return diff(arg1, arg2);
            break;
        case '*':
            return mult(arg1, arg2);
            break;
        case '/':
            return div(arg1, arg2);
            break;
        default:
            alert('нет такой операций');
            return 0;
    }
}

alert(mathOperation(1, 5, '/'));
alert(mathOperation(1, 5, '/'));
alert(mathOperation(1, 5, '/'));
alert(mathOperation(1, 5, '/'));