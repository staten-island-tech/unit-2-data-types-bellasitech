factor = int(input ('Please type in the number you want me to factor'))
factor1 = int(input ('Please type in the number you want me to factor'))


def gcf(x):
    for i in range(1, x+1): 
        if((x % i == 0)): 
            gcf = i
            print(i)

values = gcf(factor)
print('Factoring Next')
values1 = gcf(factor1)






