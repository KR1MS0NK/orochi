choice = True #using boolean with if else
other = True
if choice and other:
    print("high")
elif choice and not other:
    print("highlow")
elif not choice and other:
    print("lowhigh")
else:
    print("low")

#using comparsm with if else
num1 = 5
num2 = 20
if num1 < num2:
    print("low")
else:
    print("high")