y = int(input ('Please type in the number you want me to factor'))
x = int(input ('Please type in the number you want me to factor'))


def gcf(x,y):
    for i in range(y+1, x+1): 
        if((x % i == 0)) and (y % i == 0): 
            gcf = i
        return gcf 

values = print(gcf(x, y))


