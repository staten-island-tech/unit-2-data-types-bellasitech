def gcfe(x,y):
    while y!=0:
        z=y
        y=int(x)%int(y)
        x=z
    return x
x = int(input("number"))
y= int(input("number"))

gcf=gcfe(x,y)
print(gcf)

