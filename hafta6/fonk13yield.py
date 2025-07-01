def myFunc():
    yield "Heelo"
    yield 51
    yield "Good Bye"

x= myFunc()
print(next(x))
print(next(x))
print(next(x))
