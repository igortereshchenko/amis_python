print('starting program')

a1=int(input('enter 1st vertical'))
b1=int(input('enter 1st horizontal'))
a2=int(input('enter 2nd vertical'))
b2=int(input('enter 2nd horizontal'))
if a1<9 and a1>0 and b1<9 and b1>0 and a2<9 and a2>0 and b2<9 and b2>0:
    if ((a1+b1)%2)==((a2+b2)%2):
        print('yes')
    else:
        print('no')
else:
    print('invalid coordinates')
