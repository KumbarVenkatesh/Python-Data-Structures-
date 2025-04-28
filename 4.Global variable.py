x=0 # Global Variable
def fun(n):
    global x # Global variable call
    if n>0:
        x+=1
        return fun(n-1)+x
    return 0
r=fun(5)
print(f"{r}")

r=fun(5)
print(f"{r}")
