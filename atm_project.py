print("---ATM options---")
def atm():
    print("1-Deposit")
    print("2-Withdraw")
    print("3-Check balance")
    print("4-Exit")
balance=0
while True:
    atm()
    try:
        choice=int(input("Choose an option: "))
    except ValueError:
        print("Enter a valide option!")
        continue
    if choice==1:
        try:
            money=int(input("Enter money: "))
        except ValueError:
            print("Enter a number!")
            continue
        if money>0:
            balance+=money
        else:
            print("The written numbre should be positif!")
    elif choice==2:
        try:
            money=int(input("Enter money: "))
        except ValueError:
            print("Enter a number!")
            continue
        if money<=balance:
            balance-=money
        else:
            print("insufficient money!")
    elif choice==3:
        print(f"Your balance is: {balance}")
    elif choice==4:
        print("Thanks for using our services!")
        break
    else:
        print("Choose a valid options!")