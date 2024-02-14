def make(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make
def ordinary():
    print("I am ordinary")
ordinary()