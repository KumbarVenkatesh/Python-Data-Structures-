def fun(n):
    print(f"{n}")
    if n>100:
        return n-10
    return fun(fun(n+11))
r=fun(95)
print(f"{r}")
