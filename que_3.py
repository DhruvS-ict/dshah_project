# 3. Write a program to create a list of numbers, extract integer numbers from a list based on
# below conditions.
# a. Number must be 4 digit long i.e (1000 to 9999)
# b. First digit of the number must be odd and the last digit must be even.
# c. Number must be divisible by either 3 or 7.
p=[]
l=[1234,1003,123,44,2,1004,2000,3000,5002,7000]
lst=[i for i in l if len(str(i))==4 and int(str(i)[0])%2!=0 and int(str(i)[-1])%2==0 and (i%3==0 or i%7==0)]
print(lst)
