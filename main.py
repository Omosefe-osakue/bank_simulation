import random
# A Simple programme to simulate
# a Bank Service

#Initialize the variables
tries = 3
bank_name = "ACME Financial Group"
accounts_data = []


#function defining atm processes
def atm():
    global balance
    user_atm_pin = user_data["pin"]
    #Ask the user to input their pin
    userPin = input("Enter your Pin: ")

    while(tries > 0):
         #Check if user input is a valid digit
        if(not userPin.isdigit()):
            print("What you have entered above is not a valid digit")
            break

        #Check if the user pin is correct
        if int(user_atm_pin) == int(userPin):
            userAction= input("Would you like to make a Withdrawal (W), Deposit (D) or see your account Balance (B) : ").lower()
                
            #Get user's preferred action and execute it
            if userAction == "w":
                amount = float(input("How much would you like to withdraw: ")) 
                if 0 < amount and amount <= balance:
                    balance -= amount
                    print(f"Your updated account balance is £{balance}")
                else:
                    print("Insufficient funds.")
                break
            elif userAction == "d":
                amount = float(input("How much would you like to Deposit: ")) 
                if amount > 0:
                    balance += amount
                    print(f"Your updated account balance is £{balance}")
                else:
                    print("Invalid amount")
                break
            else:
                print(f"Your account balance is £{balance}")
                break

        else:
            tries -= 1
            #guard clause
            if(tries == 0):
                break
            userPin = input("You have entered the wrong pin. Please try again : ")

#function to collect user details
def create_account():
    global accounts_data
    while True:
        user_data = {} #dictionary to store user data

        #Take user's first name
        user_name = input("Please input your First name: ").lower()
        user_data["name"] = user_name

        #Take user's second name
        user_surname = input("Please input your Last name: ").lower()
        user_data["surname"] = user_surname

        #take user's phone number
        user_no = input("Please input your Phone number: ")
        if (not user_no.isdigit()):
             print("What you have entered above is not a digit")
             continue
        else:
            user_data["phoneNo."] = user_no

        #take user's email address
        user_email = input("Please input your email address: ").lower()
        user_data["email"] = user_email

        #take user's atm pin
        while True:
            user_atm_pin = input("Please input your 4 digit ATM pin: ")
            if len(user_atm_pin) != 4:
                print("you have entered an invalid pin, Please enter a 4-digit pin.")
            elif (not user_atm_pin.isdigit()):
                print("you have entered a none digit invalid pin")
            else:
                user_data["pin"] = user_atm_pin
                break # exit loop once a valid pin is entered

        #take initial bank balance
        while True:
            user_balance = input("Please input your initial balance: ")
            if (not user_balance.isdigit()):
                print("What you have entered above is not a digit")
                continue
            else:
                user_data["balance"] = float(user_balance)
                break

        #Assign an account number to user
        account_number = random.randint(10000,99999) # generates a 5 digit number as the account number
        user_data["user_accountNo"] = account_number
        print(f"Your account number is {account_number}, Please take note of this as we would require it for other processes.")

        accounts_data.append(user_data) #append user's data to accounts_data list (serves as a database)
        
        another_account = input("Do you want to create another account? (yes/no): ").lower()
        if another_account != "yes":
            break  # Exit the loop if the user doesn't want to create another account
#Main function with all the bank processes 
def main():
    global balance,accounts_data
    while True:
        print(f"Welcome to {bank_name}")
        print("1. Create Account")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change Pin")
        print("5. View balance")
        print("6. View Account details")
        print(f"7. Use {bank_name} ATM")
        print("8. Exit")
        user_choice = input(" How can we help you today: ")

        if user_choice == "1":
            print("Hello, Let's create an account for you")
            create_account()
       
        elif user_choice == "2":
            amount = float(input("How much would you like to withdraw: ")) 
            if 0 < amount and amount < balance:
                balance = balance - amount
                print(f"Your updated account balance is £{balance}")
            else:
                print("Insufficient funds.")

        elif user_choice == "3":
            amount = float(input("How much would you like to Deposit: ")) 
            if amount > 0:
                balance = balance + amount
                print(f"Your updated account balance is £{balance}")
            else:
                print("Invalid amount")

        elif user_choice == "4":
            pass

        elif user_choice == "5":
            print(f"Your account balance is £{balance}")
            
        elif user_choice == "6":
            pass

        elif user_choice == "7":
            atm()

        elif user_choice == "8":
            print("Exiting...")
            break
        else:
            retry = input("You have not given a valid response would you like to try again? ").lower()
            if retry == "y" or retry == "yes":
                continue
            else:
                print("Have a lovely day, Bye.")
                break


#Calling the main function to start the bank simulation
if __name__ == "__main__":
    main()