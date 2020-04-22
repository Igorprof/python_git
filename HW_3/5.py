stop_sign = '/'
total_sum = 0

while (True):
    numbers = input().split()

    for num in numbers:
        if num.isdigit():
            total_sum += float(num)
        elif num == stop_sign:            
            break

    print(total_sum)
    
    if num == stop_sign:
        break
    
    
