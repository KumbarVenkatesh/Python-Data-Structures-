def fun(n):
    if n>0:
        print(f"{n}")
        fun(n-1)
x=3
fun(x)
