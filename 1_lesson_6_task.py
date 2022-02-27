from chardet import detect

word_list = ['сетевое программирование\n', 'сокет\n', 'декоратор\n']

#записываем слова файл в кодировке OS
with open('test_file.txt', 'w') as file:
    file.writelines(word_list)

#открываем файл в битовом формате и записываем данные в переменную words
with open('test_file.txt', 'rb') as file:
    words = file.read()

#печатаем то, что получили из файла, проверяем кодировку и выводим её для общего ознакомления
print(words)
encoding = detect(words)['encoding']
print('encoding: ', encoding)

#открываем файл повторно, кодировка указывается из предыдущего шага
with open('test_file.txt', 'r', encoding=encoding) as file:
    words = file.read()

#печатаем полученные данные
print(words)
