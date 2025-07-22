balance = 1000
pin = "1234"

password = input("Enter you PIN: ")
if password == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        if choice == '1' :
            print(f"You balance is {balance:.2f} THB")


        elif choice == '2' :
            while True :
                withdraw = float(input("How much are you withdraw : "))
                if withdraw > 0 :
                    if balance >= withdraw :
                        balance = balance - withdraw
                        print(f"You withdraw is {withdraw:.2f} THB")
                        print(f"You balance is {balance:.2f} THB")
                    else :
                        print(f"You balance is {balance:.2f} THB")
                        print("You balance Not enough")
                    break
                else :
                    print("Enter you withdraw more than 0 THB")



        elif choice =='3' :
            while True :
                deposit = float(input("How much are you deposit  : "))
                if deposit > 0:
                    balance = balance + deposit 
                    print(f"You deposit is {deposit:.2f} THB")
                    print(f"You balance is {balance:.2f} THB")
                    break
                else : 
                    print("Enter you deposit more than 0 THB")

        elif choice =='4':
            print("Thank you for using the ATM simulation")
            break
        else :
            print("Choose option 1-4 New!!")
       
        
else:
    print("Invalid PIN")
