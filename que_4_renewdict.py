employees = {"Robert_Downey":
                 {"Mark": ["TL", 3, {"Leonardo": ["JD", 1], "Alexandra": ["JD", 1]}],
                  "Samuel": ["TL", 8],
                  "Paul": ["TL", 8, {"Fergal": ["SD", 4]}],
                  "Tom": ["TL", 8, {"Jerry": ["JD", 1.5], "John": ["JD", 1.6]}]},

             "Anne_Hathaway":
                 {"Chris": ["TL", 5, {
                     "James": ["TL", 0, {"Jennifer": ["SD", 3.8], "Scott": ["SD", 3.8], "Sophie": ["SD", 3.8]}]}],
                  "Pratt": ["TL", 5],
                  "Emma": ["TL", 5],
                  "Will": ["TL", 5, {"Edge": ["SD", 3], "Ryan": ["SD", 3.5]}],
                  "Smith": ["TL", 5, {"Walker": ["SD", 2.7], "Diana": ["SD", 2.7]}]}
             }
####################################################################################################################
# (A)
# l1 = []
# def func(a):
#     for k, v in a.items():
#         if type(v) == dict:
#             l1.append(k)
#             func(v)
#         elif type(v) == list:
#             l1.append(k)
#
#             for i in v:
#                 if type(i) == dict:
#                     func(i)
#                     # l1.append(i)
#                 elif type(i) == list:
#                     l1.append(i)
#                     for j in i:
#                         if type(j) == dict:
#                             # l1.append(j)
#                             func(j)
# func(employees['Robert_Downey'])
# print(l1)
####################################################################################################################
# (B)
# l2 = []
# def exp(a):
#     for k,v in a.items():
#         if type(v)==dict:
#             exp(v)
#         elif type(v) == list:
#             if v[1] > 4:
#                 l2.append(k)
#             for i in v:
#                 if type(i) == dict:
#                     exp(i)
#                 elif type(i) == list:
#                     if i[1] > 4:
#                         l2.append(k)
# exp(employees)
# print(l2)
####################################################################################################################
# (C)
# l3=[]
# def change(a):
#     for k,v in a.items():
#         if type(v)==dict:
#             change(v)
#         elif type(v) == list:
#             if v[1]>3.5 and v[1]<4.5:
#                 l3.append(k)
#             for i in v:
#                 if type(i)==dict:
#                     change(i)
#                 elif type(i)==list:
#                     if i[1]>3.5 and i[1]<4.5:
#                         l3.append(k)
# change(employees)
# print(l3)
# ########################################################################################################################
#(D)
# def tl_change(a):
#     for k, v in a.items():
#         if type(v) == dict:
#             tl_change(v)
#         else:
#             type(v) == list
#
#             if v[0] == 'TL' and v[1] == None:
#                 print(k, ': N/a')
#             elif v[0] == 'TL':
#                 print(k, ':', v[1])
#             for i in v:
#
#                 if type(i) == dict:
#                     tl_change(i)
# tl_change(employees)
# ########################################################################################################################
#(F)
# l4=[]
# def less_exp(a):
#     for k, v in a.items():
#         if type(v) == dict:
#             less_exp(v)
#         elif type(v) == list:
#             for j in v:
#                 if type(j) == dict:
#                     less_exp(j)
#                 elif v[1] == None:
#                     pass
#                 elif v[1] < 2:
#                     l4.append(k)
# less_exp(employees)
# print(set(l4))
# ########################################################################################################################

