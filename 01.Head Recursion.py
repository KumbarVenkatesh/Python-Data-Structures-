def fun(n):
    if n>0:
        fun(n-1)
        print(f"{n}")

x=3
fun(x)
