from functools import reduce
lst = ["Sameer","khan","Afsar","Aadil"]
a= reduce(lambda x,y : x+y , lst)
print(a)