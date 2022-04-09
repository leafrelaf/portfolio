  from random import randint

name=input("what ur name")
action=input('rock (r),paper(p) or  scissor(s)')

print(name,"chosses",action)

chosen=randint(1,3)

if chosen==1:
  computer='r'
elif chosen==2:
    computer='s'
else:
    computer='s'


print("computer chooses",computer)




if action=='r'and computer=='r' :
 print("draw!")

elif action=='r'and computer=='p' :
 print("computer wins")

elif action=='r'and computer=='s' :
 print(name, "wins")



elif action=='p' and computer=='s':
 print("computer winds")

elif  action=='p' and computer=='p':
 print("draw")

elif action=='p' and computer=='r':
    print(name, "wins")



elif  action=='s'and  computer=='r':
 print("computer wins")

elif action=='s' and computer=='p':
    print(name," wins")

elif action=='s' and computer=='s':
 print("draw")
 









