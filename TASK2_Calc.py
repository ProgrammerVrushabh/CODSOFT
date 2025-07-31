def add(a,b):
    print("Sum of ",a," and ",b," is: ",a+b)
def sub(a,b):
    print("Subtraction of ",a," and ",b," is: ",a-b)
def mul(a,b):
    print("Multiplication of ",a," and ",b," is: ",a*b)
def div(a,b):
    if b==0:
        print("Can't divide by zero try again! ")
    else:
        print("Division  of ",a," by ",b," is: ",a/b)
def display():
    print("<----------------------------CALCULATOR---------------------------->")
    print(" 1. Add\n 2. Subtraction\n 3.Multiplication\n 4.Division\n 5.Exit")
    c=int(input("ENTER 1 OR 2 OR 3 OR 4..... \n"))
    if (c==1):
        a=int(input("ENTER VALUE OF 1st number: "))
        b=int(input("ENTER VALUE OF 2nd number: "))
        add(a,b)
    elif (c==2):
        a=int(input("ENTER VALUE OF 1st number: "))
        b=int(input("ENTER VALUE OF 2nd number: "))
        sub(a,b)
    elif (c==3):
        a=int(input("ENTER VALUE OF 1st number: "))
        b=int(input("ENTER VALUE OF 2nd number: "))
        mul(a,b)
    elif (c==4):
        a=int(input("ENTER VALUE OF 1st number: "))
        b=int(input("ENTER VALUE OF 2nd number: "))
        div(a,b)
    elif (c==5):
        print("<---------------------EXITING THE CALCULATOR PROGRAM ---------------------------->")
        return
    else:
        print("Invalid Coice TRY AGAIN !!!!!")
    print("WANT TO PERFORM AGAIN ?")
display()
def Again():
    print("WANT TO PERFORM AGAIN ?")
    ch=input("ENTER Y or y: ")
    for i in ch:
        if (i=="Y"or i=="y"):
            display()
        else:
            print("Invalid choice Try again .")
            Again()
Again()

        
