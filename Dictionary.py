a = {1:10 , 2:20 , 3:50}
print(a[1])
print(a.get(3))
print(a.keys())
print(a.values())
print(a.items())
for key in a :
    print(key , a[key])
print("second way to iterate dictionary")
for key in a.items():
    print(key[0] , key[1])

a.update({5:70})
print(a)
a.popitem()
print(a)
a.clear()
print(a)
