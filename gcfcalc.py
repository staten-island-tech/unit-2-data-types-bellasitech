y = int(input ('Please type in the number you want me to factor'))
x = int(input ('Please type in the number you want me to factor'))


def gcf(x,y):
    if x > y:
        smaller = y
    else:  
        smaller = x 
    for i in range(1, x+1): 
        if((x % i == 0)) and (y % i == 0): 
            gcf = i
        return gcf 

values = gcf(x)
print('Factoring Next')
values1 = gcf(y)
