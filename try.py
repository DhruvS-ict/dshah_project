# a = [1,2,3]
# b = {1: [4,5,6],2: [7,8],3: [9, 10],4: [11, 12, 13],9: [14, 15],10: [16],13: [19, 20],19: [21]}
#
# Output: [1, 4, 11, 12, 13, 19, 21, 20, 5, 6, 2, 7, 8, 3, 9, 14, 15, 10, 16]


a = [1,2,3]
b = {1: [4,5,6],2: [7,8],3: [9, 10],4: [11, 12, 13],9: [14, 15],10: [16],13: [19, 20],19: [21]}
l1=[]
def func(x):
    for k,v in x.items():
        if k in a:
            l1.append(k)
            if type(v) == list:
                for i in v:
                    if i in b.keys():
                        # func(v)
                        l1.append(i)
                        p=b.get(i)
                        l1.extend(p)
                        for j in p:
                            if j in b.keys():
                                l1.append(j)
                                q=b.get(j)
                                l1.extend(q)
                                for s in q:
                                    if s in b.keys():
                                        l1.append(s)
                                        m=b.get(s)
                                        l1.extend(m)


func(b)
print(l1)
# g=[]
# for i in l1:
#     if i.count()>1:
#         g.append(i)
# print(g)