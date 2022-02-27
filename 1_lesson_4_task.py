#Создаётся переменная типа list для добавления вводимых слов
words_list = []

#указывается флаг для создания цикла бесконечного ввода необходимых слов
flag = True

#пока flag равен true - вводим слова, которые добавляются в words_list
while flag == True:
    intermediate_var = input("Введите слово. Для остановки введите 'stop': ")
    if intermediate_var == 'stop':
        break
    words_list.append(intermediate_var)


#данный цикл создан для отображения всех кодирования и декодирования введёных слов, отображения самих слов и их типов
for word in words_list:
    intermediate_word = word.encode('UTF-8')
    print(f'В кодировке utf-8 слово {word} выглядит как "{intermediate_word}"')
    print(f'Тип закодированного слова {type(intermediate_word)}')
    end_word = intermediate_word.decode('UTF-8')
    print(f'При декодировании в формате utf-8 слово выглядит как "{end_word}"')
    print(f'Тип закодированного слова {type(end_word)}')
