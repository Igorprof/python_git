const regex = /\B'|'\B/g;

const inputStr = document.querySelector('.inputStr');
const resultP = document.querySelector('.result');

inputStr.addEventListener('input', () => {
    const str = inputStr.value;
    resultP.innerHTML = str.replace(regex, "\"");
})
