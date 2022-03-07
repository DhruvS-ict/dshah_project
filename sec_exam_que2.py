name = ['nikhar','avish','1avish','Aryan']
y = list(filter(lambda x: x[0].islower() and x[0].isalpha() and x not in '1234567890' and x[0] not in 'aeiouAEIOU',name))
print("".join(y))