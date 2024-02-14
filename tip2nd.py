print("What was the value of the bill?")
bill = input()
print("How was the service?")
service = input()
if service == ("good"):
    percentage = 0.20
elif service == ("okay"):
    percentage = 0.15
elif service == ("bad"):
    percentage = 0 
elif service == ("great"):
    percentage = 0.25
tip = bill * percentage
print(tip)



if x > y:
        smaller = y
    else:  
        smaller = x 