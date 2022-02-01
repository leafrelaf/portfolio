from path_failure import score
from time import sleep
import sys
from random import randint
number1=randint(1,15)
number2=randint(1,15) 
print("question 2")
sleep(3)
print(number1,'X',number2)
correct_ans=int((number1*number2))
ans=int(input('ans'))
if ans==correct_ans:
   print("well done")
   print("next question")
   import path_failure3
   
  



else:
 sys.exit
 print("worng")