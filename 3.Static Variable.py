class Static:
    x=0 #Class Variable(Static Variable)
    def fun(self,n):
        if n>0:
            Static.x+=1
            return Static.fun(self,n-1)+Static.x
        return 0
s=Static()
r=s.fun(5)
print(f"{r}")

r=s.fun(5)
print(f"{r}")

