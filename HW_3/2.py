def show_user_info(first_name, last_name, year, city, email, pnumber):
    print(f'Имя: {first_name}, Фамилия: {last_name}, Год рождения: {year}, Город проживания: {city}, Электронная почта: {email}, Номер телефона: {pnumber}')

print('Пожалуйста, заполните анкету')

name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
year = input('Год рождения: ')
city = input('Город проживания: ')
email = input('Электронная почта: ')
pnumber = input('Номер телефона: ')

show_user_info(first_name=name, last_name=surname, year=year, city=city, pnumber=pnumber, email=email)

