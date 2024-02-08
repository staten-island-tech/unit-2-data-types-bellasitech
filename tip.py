x = (int(input('total')))
service = int(input ('please rate your service here'))

if service == ("bad"):
    print(float(x))
elif service == ("okay"):
    print(float(1.15*x))
elif service == ("good"):
    print(float(1.20*x))
elif service == ("great"):
    print(float(1.25*x))