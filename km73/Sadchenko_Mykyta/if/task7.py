while True:
    coord11 = int(input("Enter row of first cell: "))
    coord12 = int(input("Enter column of first cell: "))
    coord21 = int(input("Enter row of second cell: "))
    coord22 = int(input("Enter column of second cell: "))
    print()     #JUST an INDENT
    
    if (0< coord11 <9) & (0< coord12 <9) & (0< coord21 <9) & (0< coord22 <9):
        if (coord11+coord12)%2 == (coord21+coord22)%2:
            print("YES")
        else:
            print("NO")
        break
    else:
        print("Need a true coordinates")
        continue
