from path_failure2 import score
from time import sleep
import sys
from random import randint
number1=randint(1,15)
number2=randint(1,15) 
print("question 3")
sleep(3)
print(number1,'X',number2)
correct_ans=int((number1*number2))
ans=int(input('ans'))
if ans==correct_ans:
   print("well done")
   print("next question")
   import projects.level_1.path_failure4 as path_failure4
  



else:
 sys.exit
 print("worng")