def factorial(n: int) -> int:
    memo = {}
    def fact(x: int, m: dict):
        if m.get(x) != None:
            return m.get(x)
        elif x == 0:
            return 1
        else:
            m[x] = fact(x-1, m) * x
            return m[x]
    return fact(n, memo)

print(factorial(5))