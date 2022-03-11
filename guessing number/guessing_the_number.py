#sup
#the aim here is for you to guess the number that computer is thinking between 1-100 

from  time import sleep
from random import randint



sleep(1)

guessing_number=randint(1,100)
print("the number have been choosen")
sleep(1)
if guessing_number%2==0:
    print("hint 1:the guessed number is even")
elif guessing_number%2==1:
 print("hint 1:the guessed number is odd")
A=guessing_number-5 
B=guessing_number+5

print("hint 2:the number is between",A,"&",B)
if A<0:
   print("number is positive")


if guessing_number%3==0:
    print("hint 3 :the number is devisible by 3")
elif guessing_number%4==0:
   print("hint 3 :the number is devisibe by 4")
elif  guessing_number%5==0:
    print("hint 3 :the number is devisible by 5")
elif  guessing_number%6==0:
   print("hint 3 :the number is devisible by 6")
elif  guessing_number%7==0:
   print("hint 3 :the number is devisible by 7")
elif  guessing_number%8==0:
   print("hint 3 :the number is devisible by 8")
elif  guessing_number%9==0:
   print("hint 3 :the number is devisible by 9")
elif  guessing_number%10==0:
   print("hint 3 :the number is devisible by 10")
else:
  print("hint 3 :number is a prime number") 
end=int(input("so what do u think number can be ?"))
if end==guessing_number:
   print("u won")
   print("the answer was",guessing_number)
else:
   print("u r wrong")
   print("the answer was",guessing_number)


again=input("do you want to play again ?(Y/N)")
if again=="Y" or "y":
   import number_guesser
elif again=="N" or "n":
   quit()

    



