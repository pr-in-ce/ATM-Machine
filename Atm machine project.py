print("*"*65)
print(" "*20,"WELCOME TO THE ATM"," "*20)
print("*"*65)
pin=1234
chance=3
balance=5000
while chance != 0:
    user_pin=int(input("enter your four digit pin :\npin="))
    if user_pin != pin :
        chance-= 1
        print("wrong pin number")
        print("you have chance left ", chance)
    else:
        print()
        print("*"*20,"WELCOME TO YOUR ACCOUNT","*"*20,"\n")
        print("press 1 for check your balance: \npress 2 for withdraw the cash: \npress 3 for credit amount:")
        user_choice=int(input("enter your choice: "))
        if user_choice==1:
            print("your total balance is\n" , balance)
        elif user_choice==2:
            withdrawl=int(input("enter the amount for withdraw :\n"))
            balance-=withdrawl
            print("your withdarwl amount is :\n", withdrawl)
            print("your current balance is :\n", balance )
        elif user_choice==3:
            credit=int(input("enter the amount for credit"))
            balance+=credit
            print("your credit amount is :\n", credit)
            print("your availeble balance is :\n",balance)
        elif user_choice!=(1,2,3):
            print("you are out of choice")
        print("*"*65)
        user_exit=int(input("would you like to exit :\npress 1 for exit :\npress 2 for continue :"))
        if user_exit==1:
            print("*"*20,"THANK YOU FOR VISITING US ","*"*20)
            break
        else:
            continue

        
