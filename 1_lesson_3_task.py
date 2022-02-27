#Создаётся переменная типа list для добавления вводимых слов
words_list = []

#указывается флаг для создания цикла бесконечного ввода необходимых слов
flag = True

#пока flag равен true - вводим слова, которые добавляются в words_list
while flag == True:
    intermediate_var = input("Введите слово. Для остановки введите 'stop': ")
    #создаем try...except конструкцию для выведения ошибок по словам, которые не переведутся в байтовый формат
    try:
        if intermediate_var == 'stop':
            break
        words_list.append(eval('b' + '"' + intermediate_var + '"'))
    except SyntaxError as err:
        print(f'Введеное слово не может быть записано в байтовом формате. Причина:\n{err}')

#данный цикл создан для отображения всех введёных слов, их типа и длины
for word in words_list:
    print(word)
    print(type(word))
    print(len(word))
