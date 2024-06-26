# 1. На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.
# Получаем строку и разбиваем её на слова, сохраняя их в список s
s = input().split()

# Выводим элементы списка s, разделяя их переводами строки
print(*s, sep="\n")

#2. На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Напишите программу, которая выводит инициалы человека.
# Получаем строку и разбиваем её на слова, сохраняя их в список s
s = input().split()
# Проходим по каждому слову i в списке s
for i in s:
    print(i[0], end=".")  # Выводим первую букву слова i и добавляем точку в конце
#3.В операционной системе Windows полное имя файла состоит из буквы диска, после которого ставится двоеточие и символ  "\",
# затем через такой же символ перечисляются подкаталоги (папки), в которых находится файл, в конце пишется имя файла (C:\Windows\System32\calc.exe).
# На вход программе подается одна строка с корректным именем файла в операционной системе Windows.
# Напишите программу, которая разбирает строку на части, разделенные символом "\". " \Каждую часть вывести в отдельной строке.
    # Получаем строку и разделяем её на подстроки, используя обратный слеш в качестве разделителя
    s = input().split('\\')
    # Выводим подстроки, разделяя их переводами строки
    print(*s, sep="\n")
#4 На вход программе подается строка текста, содержащая целые числа. Напишите программу, которая по заданным числам строит столбчатую диаграмму.
# Получаем строку и разбиваем её на слова, предполагая, что каждое слово - это число
s = input().split()
# Проходим по каждому слову i в списке s
for i in s:
    print('+' * int(i))  # Выводим '+' умноженный на целое число, представленное словом i

#5 На вход программе подается строка текста, содержащая 4 целых неотрицательных числа, разделенных точкой.
# Напишите программу, которая определяет, является ли введенная строка текста корректным ip-адресом.
# Получаем строку и разбиваем её на четыре числа, используя точку в качестве разделителя
s = input().split('.')
# Проходим по каждому числу i в списке s
for i in s:
    if int(i) < 0 or int(i) > 255:  # Проверяем, что число является допустимым (в пределах от 0 до 255)
        print('НЕТ')  # Если число недопустимо, выводим 'НЕТ'
        break  # Прерываем цикл, так как одино из числел недопустимый
else:
    print('ДА')  # Если все числа допустимые, выводим 'ДА'

# 6 На вход программе подается строка текста и строка-разделитель. Напишите программу, которая вставляет указанный разделитель между каждым символом введенной строки текста.

s = input()  # Считываем первую строку
r = input()  # Считываем вторую строку
# Преобразуем первую строку s в список символов
# Затем объединяем символы из списка, используя вторую строку r в качестве разделителя
res = r.join(list(s))
# Выводим результат
print(res)

#7 На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел.
# Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
s = input().split()
c = 0  # Инициализируем счетчик повторяющихся слов
# Проходим по каждому индексу i в списке s
for i in range(len(s)):
    # Для каждого индекса i, проходим по оставшимся словам, начиная с индекса i + 1
    for j in range(i + 1, len(s)):
        if s[j] == s[i]:  # Если слова с индексами i и j совпадают
            c += 1  # Увеличиваем счетчик на 1
print(c)  # Выводим общее количество повторяющихся слов
