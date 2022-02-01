'''to check if a number is prime or not'''
x=int(input("enter a number"))
for i in range (2,x):
   if (x%i)==0:
     print(f"{x} number is not prime")
     break
else:
      print(f"{x}number is prime")




