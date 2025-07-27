p = int(input("Enter a position in the sequence: "))
list = [0, 1]

def FIB(x):
    def fib(a, b, n):
        global list
        c = a + b
        list.append(c)
        if len(list) == n:
            print(list)
            return "end"
        else:
            return fib(b, c, n)

    return fib(list[0], list[1], x)

if p == 1:
    print(list.index(0))
elif p == 2:
    print(list.index(1))
elif p >= 3:
    FIB(p)
    print(list[p - 1])
