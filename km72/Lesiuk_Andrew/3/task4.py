print("N студентів отримали K яблук і розподілити їх між собою порівну. Неподілені яблука залишились у кошику. Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику?")
while True:
    n=float(input('Введіть N(кількість студентів):'))
    if n<=0:
       print('Кількість має бути більшою за 0')
    else:
        break
while True:
    k=float(input('Введіть K(кількість яблук):'))
    if n<=0:
        print('Кількість має бути більшою за 0')
    else:
        break
print('Яблук дістанеться кожному студенту:',k//n)
print('Яблук залишилося у кошику:',k%n)
