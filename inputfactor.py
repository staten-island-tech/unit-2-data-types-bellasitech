factor = int(input ('Please type in the number you want the factors of'))


def gcf(x):
    for i in range(1, x+1): 
        if((x % i == 0)): 
            gcf = i
            print(i)

values = gcf(factor)