num1=float(input("Enter A Number"))
num2=float(input("Enter A Number"))
num3=float(input("Enter A Number"))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The Largest Number Between",num1,",",num2,"and",num3,"is",largest)     
