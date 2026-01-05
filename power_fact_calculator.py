def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
power=lambda a,b:a**b
while True:
    print("----------------FACTORIAL AND POWER---------------")
    print("1.Factorial")
    print("2.power")
    print("3.Exit")
    choice=int(input("Enter the choice="))
    if choice==1:
        num=int(input("Enter the number="))
        print("Factorial=",fact(num))
    elif choice==2:
        a=int(input("Enter the a="))
        b=int(input("Enter the b="))
        print("Power=",power(a,b))
    elif choice==3:
        print("Thank you")
    else:
        print("Invalid choice")
