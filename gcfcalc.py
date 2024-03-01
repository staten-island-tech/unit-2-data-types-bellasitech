x = int(input ("first number"))
y = int(input ("second number"))
factor = []

def gcf(x,y):
  for i in range(x,y):
    if x%i == 0 and y%i == 0:
        factor.append(i)

gcf(x,y)
print('GCF of', x, 'and', y, 'is', factor[-1])