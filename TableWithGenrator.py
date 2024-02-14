def table():
    num = 1 
    while True:
        yield num * 5
        num += 1
result = table()
for _ in range(10):
    print(next(result))
