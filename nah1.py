#For sort elements with name wise,age wise & height wise.

a=[]
for i in range(3):
    x = [(x) for x in input("Enter multiple value: ").split(",")]
    a.append(tuple(x))
    b=sorted(a)
    c=sorted(a,key=lambda d: d[1])
    e=sorted(a, key=lambda f: f[2])
print(b)
print(c)
print(e)
b v bb	




#to calculate age from birthdate.
from datetime import date
def age():
    today = date.today()
    print(today)
    age = today.year - 2000 - ((today.month, today.day) < (5, 31))
    return age
print(age())







#Basic DateTime Operations in Python.
# There are six main object classes with their respective components in the datetime module mentioned below:
# datetime.date
#   Syntax:datetime.date( year, month, day)
# datetime.time
#   Syntax: datetime.time(hour, minute, second, microsecond)
# datetime.datetime
#   Syntax: datetime.datetime( year, month, day )  or  datetime.datetime(year, month, day, hour, minute, second, microsecond)
# datetime.tzinfo
# datetime.timedelta
# datetime.timezone
#   Syntax: datetime.timezone()
from datetime import *
from pytz import timezone
import pytz
current = date.today()
new=current.strftime("%x:%c:%d:%B:%Y")
print(current)
print(new)
print("Today's day : ",current.day)
print("Today's month : ",current.month)
print("Today's year : ",current.year)
ct=datetime.now()
print(ct)
newct=ct.strftime("%H:%M:%S")
print(newct)
tzone = timezone('Asia/Calcutta')
normal = datetime(2022, 1, 19)
print(tzone)
print("Operations on normal datetime")
print(tzone.utcoffset(normal, is_dst=True))
print(tzone.dst(normal, is_dst=True))
print(tzone.tzname(normal, is_dst=True))
##OUTPUT##
2022-01-19
01/19/22:Wed Jan 19 00:00:00 2022:19:January:2022
Today's day :  19
Today's month :  1
Today's year :  2022
2022-01-19 11:12:51.729077
11:12:51
Asia/Calcutta
Operations on normal datetime
5:30:00
0:00:00
IST





#1). Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5,between 2000 and 3200 (both included).The numbers obtained should be
# printed in a comma-separated sequence on a single line.
# import random
l=[i for i in range(2000,3200) if i%7==0 and i%5!=0]
print(l)
##OUTPUT##
[2002, 2009, 2016, 2023, 2037, 2044, 2051, 2058, 2072, 2079, 2086, 2093, 2107, 2114, 2121, 2128, 2142, 2149, 2156, 2163, 2177, 2184, 2191, 2198, 2212, 2219, 2226, 2233, 2247, 2254, 2261, 2268, 2282, 2289, 2296, 2303, 2317, 2324, 2331, 2338, 2352, 2359, 2366, 2373, 2387, 2394, 2401, 2408, 2422, 2429, 2436, 2443, 2457, 2464, 2471, 2478, 2492, 2499, 2506, 2513, 2527, 2534, 2541, 2548, 2562, 2569, 2576, 2583, 2597, 2604, 2611, 2618, 2632, 2639, 2646, 2653, 2667, 2674, 2681, 2688, 2702, 2709, 2716, 2723, 2737, 2744, 2751, 2758, 2772, 2779, 2786, 2793, 2807, 2814, 2821, 2828, 2842, 2849, 2856, 2863, 2877, 2884, 2891, 2898, 2912, 2919, 2926, 2933, 2947, 2954, 2961, 2968, 2982, 2989, 2996, 3003, 3017, 3024, 3031, 3038, 3052, 3059, 3066, 3073, 3087, 3094, 3101, 3108, 3122, 3129, 3136, 3143, 3157, 3164, 3171, 3178, 3192, 3199]





# 11). Use a list comprehension to square each odd number in a list. The list is input by a
# sequence of comma-separated numbers.
n=list(map(int,input("Enter any integer : ").split(",")))
b=[i for i in n if i%2!=0]
l=[x**2 for x in b if x%2!=0]
a=dict(zip(b,l))
print(a)
##OUTPUT##
Enter any integer : 1,2,3,4,5,6,7,8,9
{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}





#13). Please write a program to output a random number, which is divisible by 5 and 7,
#between 0 and 10 inclusive using random module and list comprehension.
import random
a=[x for x in range(random.randrange(0,11)) if x%5==0 if x%7==0]
print(a)
##OUTPUT##
[]





#14). Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
import random
a=[random.randrange(100,201) for x in range(5)]
a.sort()
print(a)
##OUTPUT##
[106, 109, 122, 193, 195]





#15&16).Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
import random
print(random.sample([i for i in range(1,1000) if i%5==0 and i%7==0], 5))
##OUTPUT##
[245, 455, 420, 490, 315]





#17).Please write a program to shuffle and print the list [3,6,7,8].
import random
l=[8,7,6,3]
random.shuffle(l)
print(l)
##OUTPUT##
[3, 6, 7, 8]





#19). Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
a=[]
for i in range(0,21):
    a.append(i)
    if i%2==0:
        a.remove(i)
print(a)
         OR
n=[5,6,77,45,22,12,24]
l=[i for i in n if i%2!=0]
print(l)
##OUTPUT##







#20). By using list comprehension, please write a program to print the list after removing
delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
n=[12,24,35,70,88,120,155]
l=[i for i in n if i%5==0 and i%7==0]
print(l)
##OUTPUT##
[35, 70]





#21). By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
array = [[ ['0' for col in range(3)] for col in range(5)] for row in range(8)]
print(array) 
##OUTPUT##
[[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']], [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']], [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']], [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']], [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']], [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']], [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']], [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]]





#22). By using list comprehension, please write a program to print the list after removing the
#0th,4th,5th numbers in [12,24,35,70,88,120,155].
num=[12,24,35,70,88,120,155]
l=[i for i in num if i!=num[0] and i!=num[4] and i!=num[5]]
print(l)
##OUTPUT##
[24, 35, 70, 155]





#23). By using list comprehension, please write a program to print the list after removing the
#value 24 in [12,24,35,24,88,120,155].
num=[12,24,35,24,88,120,155]
l=[i for i in num if i!=24]
print(l)
##OUTPUT##
[12, 35, 88, 120, 155]





#24). With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to
#make a list whose elements are intersection of the above given lists.
l1=[1,3,6,78,35,55]
l2=[12,24,35,24,88,120,155]
m,n = set(l1),set(l2)
b=set()
b={x for x in m and n if x in m!=x in n}
print(list(b))
##OUTPUT##
[35]





#25). With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
#after removing all duplicate values with original order reserved.
num=[12,24,35,24,88,120,155,88,120,155]
print(set(num))
##OUTPUT##
{35, 12, 155, 24, 88, 120}





#29). Please write a program which accepts a string from the console and prints it in reverse order.
inp=input("Enter any string here : ")
print(inp[::-1])
##OUTPUT##
Enter any string here : Hello World
dlroW olleH






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
--------------------------------------------------



#Find Max & Min of 3nos. through Ternary Operator.
d = int(input("Enter the number : "))
e = int(input("Enter the number : "))
f = int(input("Enter the number : "))
    # if d > e:
    #     if d > f:
    #         print(d)
    #     else:
    #         print(f)
    # elif e > f:
    #     print(e)
    # else :
    #print(f)
maximum = d if (d <= e and d <= f) else (e if (e <= f and e <= d) else f)
print(maximum)
##OUTPUT##
Enter the number : 3
Enter the number : 1
Enter the number : 2
1
