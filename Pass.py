import string
import random
l=string.ascii_letters
d=string.digits
spchr=string.punctuation
clist=[]
c=l+d+spchr
passw = []
print("<---------------------PASSWORD GENERATOR------------------------->")
while True:
    l=int(input("Enter length of password: "))
    if l<8:
        print("password lngth must be atleast 8 characters.")
    elif l>25:
        print("Password must be less than 20 characters.")
    else:
        break
while True:
    ch1=int(input(" 1. print random number\n 2. custom password.."))
    if ch1==1:
        for x in range(l):
            password=random.choice(c)
            passw.append(password)
        print("The random password is: "+"".join(passw))
        break
    elif ch1==2:
        print("Choose character sets...")
        print(" 1. letter\n 2. digits\n 3. special characters\n press 4 after selecting the character sets for getting finall output!")
        while(True):
            ch=int(input("pick up a number: "))
            if (ch==1):
                clist+=l
            elif(ch==2):
                clist+=d
            elif(ch==3):
                clist+=spchr
            elif(ch==4):
                break
            else:
                print("please pick a valid options !")
        for i in range (l):
            rgen=random.choice(clist)
            passw.append(rgen)
        print("the random password is :"+"".join(passw))
        break
    else:
        print("invalid choice")
if l>=8 and l<=10:
    print("Password strenght is : Medium!")
if l>10 and l<=15:
    print("password strenght is : Good!")
if l>15 and l<=20:
    print("Password strength is : Strong")
if l>20:
    print("Password strength is very very Strong !")