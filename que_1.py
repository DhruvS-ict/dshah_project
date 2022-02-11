 # 1. Write a function to extract words from the sentence that are repeated multiple times, the
# function must return value(s). Display those words with ‘#’ separator (use join function).
# For example : WORD1 # WORD2 # WORD3
# str1="hi my name is kavish and yor name is Aryan"
# lst=str1.split()
# print(lst)
# lst_comp={x for x in lst if (lst.count(x))>1}
# print("#".join(lst_comp))
def func(s):
    a=s.split()
    x={i for i in a if (a.count(i))>1}    #count() returns count of how many times obj occurs in a list.
    print("#".join(x))
    return s
func("hi my name is kavish,yor name is Aryan")