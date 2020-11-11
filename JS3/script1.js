console.log('задание 1');
let num = 2;

while (num <= 100) {    
        let flag = true;
        let i = 2;
        while (i <= Math.sqrt(num))
        {
            if (num % i == 0) {
                flag = false; 
                break;
            }
            i++;
        }
        if (flag) {
            console.log(num);
        }    
    num++;
}