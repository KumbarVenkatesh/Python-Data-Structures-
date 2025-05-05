def fact(n):
    if n==0:
        return 1
    return fact(n-1)*n

r=fact(5)
print(f"{r}")
