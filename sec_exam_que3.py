def arm(a):
    if ((int((a%1000)/100))**3 + (int((a%100)/10))**3 + (int(a%10))**3)==a:
        print("YES, It's an Armstrong Number.")
    else:
        print("NO, It's not an Armstrong Number.")
    return a
arm(173)


# print(int(153%10))