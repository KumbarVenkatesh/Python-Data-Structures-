def fun(n):
    if n>0:
        print(f"{n}")
        fun(n-1)
        fun(n-1)

fun(3)

