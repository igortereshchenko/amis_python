print("""Здравствуйте!
Данная программа предназначена для определения цвета двох шахматных клеток""")
#Выводим приветствие и предназначение программы
x = int(input("Введите номер начального ряда:"))#Команда для ввода переменной
y = int(input("Введите номер начального столбца:"))#Команда для ввода переменной
x1 = int(input("Введите номер конечного ряда:"))#Команда для ввода переменной
y1 = int(input("Введите номер конечного столбца:"))#Команда для ввода переменной
if (x+x1)%2 == (y+y1)%2:
    res = "Yes"
else:
    res = "No"
print(res)
print(input("Нажмите клавишу \"Enter\" для окончания работы программы"))
