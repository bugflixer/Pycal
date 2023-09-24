#!usr/bin/python

import os,sys

os.system("sleep 3")
os.system("clear")
os.system("bash $HOME/Pycal/banner.sh")

print("\033[33m\033[1mHello User")
print("\033[1m\033[33mThis is A Calculator  : Made For Beginers  \033[42m ]:\033[37m \nCoded By :  Bugflixer \033[32m:[ \033[0m")
print("\033[1m\033[31m\033[4m............................\033[0m")
print()
num1 = int(input("\033[1m\033[33m[\033[32m!\033[33m]\033[34m Enter the First Number : \033[32m"))
num2 = int(input("\033[1m\033[33m[\033[32m!\033[33m]\033[34m Enter the Second Number : \033[32m"))

print("\033[4m............................")
print()

# Addition Line 

print("\033[32m[\033[33m1\033[32m]\033[31m\033[33m  Addition")
print("\033[32m[\033[33m2\033[32m]\033[31m\033[33m  Subtraction")
print("\033[32m[\033[33m3\033[32m]\033[31m\033[33m  MultiPlication")
print("\033[32m[\033[33m4\033[32m]\033[31m\033[33m  Division")
print()
opt = int(input("\033[31m➢ \033[32mEnter your Choice option : \033[31m"))


# if /else Code 

if opt == 1:
    Ans = num1 + num2
    print()
    print("\033[31mYour Answer:-\033[32m", Ans)

elif opt == 2:
    Ans = num1-num2
    print()
    print("\033[31mYour Answer:-\033[32m", Ans)

elif opt == 3:
    Ans = num1*num2
    print()
    print("\033[31mYour Answer:-\033[32m", Ans)
elif opt == 4:
    Ans = num1%num2
    Ans2 = num1/num2
    print("\033[32m")
    print("\033[31mRemainder:- \033[33m",Ans)
    print("\033[31mQuotient:- \033[33m",Ans2)
    print()

    
else :
    print("\033[33m\033[1mYou have Entered Invalid Option !")
