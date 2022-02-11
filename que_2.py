# 2. Write a program to extract string elements from a list based on below conditions, use
# in-built functions.
# a. First character must capitalize and consonant.
# b. String must not contain any number.
x=[]
string=['Aryan','aryan','Kavish1','dhruv','Nikhar']
vow=['a','e','i','o','u','A','E','I','O','U']
lst_comp=[x for x in string if (x.isalpha()) and (x[0].isupper()) and (x[0] not in vow) and (x!=x.isalnum())]
print("".join(lst_comp))