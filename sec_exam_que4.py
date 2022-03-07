num = [123,1234,1186,1,2368]
y = list(filter(lambda x: x in range(1000,(9999+1)) and (int((x%1000)/100))%2!=0 and (int(x%10))%2==0 and (x%8==0 or x%5==0),num))
print(y)
# print(int(((9385%10))))

