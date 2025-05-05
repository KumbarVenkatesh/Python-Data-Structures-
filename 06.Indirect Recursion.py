def funA(n):
    if n>0:
        print(f"{int(n)}")
        funB(n-1)

def funB(n):
    if n>1:
        print(f"{int(n)}")
        funA(n/2)
funA(20)
