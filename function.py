def func(name):
    print("Hello",name,"!")
func("munia")


def func2(num,num2):
    sum = num + num2
    return sum

print(func2(4,5))

#

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))