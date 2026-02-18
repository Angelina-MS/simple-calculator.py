answer=input("would you like to add or subtract?").strip().lower()
if answer=="add":
    a=float(input("what is your first number?"))
    b=float(input("what is your second number?"))
    print("Result:",a+b)
elif answer=="subtract":
    a=float(input("what is your first number?"))
    b=float(input("what is your second number?"))
    print("Result:",a-b)
else:print("invalid")