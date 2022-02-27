var_1 = 'разработка'

var_2 = 'сокет'

var_3 = 'декоратор'

var_list = [var_1, var_2, var_3]

for word in var_list:
    print(word)
    print(type(word))

print('----------------------------------------------------')
#с помощью онлайн-конвертера преобразовал строковые представление в формат Unicode,
#результат записал в переменные

var_1_uni = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'

var_2_uni = '\u0441\u043e\u043a\u0435\u0442'

var_3_uni = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

var_uni_list = [var_1_uni, var_2_uni, var_3_uni]

for word in var_uni_list:
    print(word)
    print(type(word))
