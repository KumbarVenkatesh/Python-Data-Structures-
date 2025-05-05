def sum(n):
    if n==0:
        return 0
    else:
        return sum(n-1)+n
r=sum(5)
print(f"{r}")

