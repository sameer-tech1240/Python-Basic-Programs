def number():
    num = 1
    while num <= 100 :
        yield num
        num += 1
for i in number():
    print(i)