from datetime import datetime
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

admin_user_name = "Admin" # Admin user name
admin_password = "Admin@123" # Admin password


#  For viva current date


#======= SHOW THE CURRENT DATE====== 
def current_date():
     now=datetime.now().strftime("%Y-%m-%d")
     print("Current Date: " , now)
     
'''
#========CHANGE PASSWORD=======     
def change_password():
     done,ac_num,name = verification()
     if done:
        get_password = input("Enter the new password. (Must more the 6 characters)")
        if len(get_password) > 6:
            con_password = input("Re enter the password")
            if get_password == con_password:
                 with open("customers_accounts.txt" , "a+") as c_file:
                      lines = c_file.readlines()
                      for line in lines:
                           fields = line.strip().split(",")
                           if len(fields) < 4:
                                continue
                           if ac_num == fields[0]:
                                c_file.write(f"{ac_num},{name},{address},{get_password},{balance}")                                                  
        else:
             print("Password must be 6 characters.")
             return
     else:
          return               
                      '''

#====CREATE NEW ACCOUNT NUMBER=====
def create_account_number():
    with open("customers_accounts.txt", "r") as customers_file:
        return f"{int(customers_file.readlines()[-1].split(",")[0])+1}" # Find the last account number and generate next new account number
    
#======VERIFY ACCOUNT======
def verification():    
    get_customer_account_number = input("Enter The Account Number: ")
    get_customer_password = input("🗝️  Enter The Account Password: ")

    with open("customers_accounts.txt", "r") as customers_file:
        lines = customers_file.readlines()      # Lines in customer file
        for line in lines:                      # One line in lines 
            fields = line.strip().split(',')    # Split line by (,)
            if len(fields) < 4:                 # Lenth of line
                continue

            account_number = fields[0]          # Define the value to variable
            customer_password = fields[3]
            customer_name = fields[1]
    
            if account_number == get_customer_account_number and customer_password == get_customer_password: # Verify the account number password
                return True , get_customer_account_number, customer_name # Return the values for using another function
    return False , None
      
#=====DEPOSIT FUNCTION=====
def deposit():
        done,ac_num,name = verification()
        if done:
                # Get latest balance from transactions.txt
                latest_balance = 0.0
                with open("transactions.txt", "r") as transactions_file:
                    t_lines = transactions_file.readlines()
                    for t_line in reversed(t_lines): # Read lines by reversed
                        t_fields = t_line.strip().split(',')
                        if len(t_fields) >= 4 and t_fields[0] == ac_num: # Verify the entered account number = account number from transaction.txt
                            try:
                                latest_balance = float(t_fields[3])
                            except ValueError:
                                pass
                            break  
                # Ask for deposit amount
                while True:
                    try:
                        depAmount = float(input("Enter The Deposit Amount: "))
                        if depAmount > 0:
                            new_balance = latest_balance + depAmount
                            print("✅  Successful deposit! Your Deposit Amount Is:", depAmount)
                            print("💰  Now Your Balance Is:", new_balance)

                            with open("transactions.txt", "a") as transactions_file:
                                transactions_file.write(f"{ac_num},DEPOSIT,{depAmount},{new_balance},{now}\n")
                            return  # Exit after successful deposit
                        else:
                            print("💴  Invalid Deposit Amount. Must Be Greater Than 0.")
                    except ValueError:
                        print("❌  Invalid input. Please enter a valid number.")
        else:
            print("❌  Incorrect Account Number or Password!")

#=====WITHDRAWAL FUNCTION=====
def Withdrawal():
        done,ac_num,name = verification()
        if done:
                # Get latest balance from transactions.txt
                latest_balance = 0.0
                with open("transactions.txt", "r") as transactions_file:
                    t_lines = transactions_file.readlines()
                    for t_line in reversed(t_lines): # Read lines by reversed
                        t_fields = t_line.strip().split(',')
                        if len(t_fields) >= 4 and t_fields[0] == ac_num: # Verify the entered account number = account number from transaction.txt
                            try:
                                latest_balance = float(t_fields[3])
                            except ValueError:
                                pass
                            break
                while True:        
                            try:
                                withAmount=float(input("Enter The Withdrawal Amount: "))
                                if withAmount > 0: 

                                    if latest_balance > 5000.00:  # For viva balance warning
                                         
                                        if withAmount <= latest_balance:
                                            latest_balance= latest_balance - withAmount
                                            print("✅  Successfull Withdrawal! Your Withdrawal Amount Is: ", withAmount, "Now Your Balance Is: ", latest_balance)
                                            with open("transactions.txt", "a") as transactions_file:
                                                    transactions_file.write(f"{ac_num},WITHDRAWAL,{withAmount},{latest_balance},{now}\n")
                                            return  # Exit after successful withdrawal
                                        else:
                                            print("🪫💵 Insufficient Balance.")
                                    else:
                                         print("⚠️  Warning: Balance below Rs.5000 !")
                                         return            
                                else:    
                                    print("💴  Invalid Widhrawal Amount. Must Be Greater Than 0.")
                            except ValueError:
                                print("❌  Invalid Input. Please enter a valid number..") 
        else:                          
            print("❌  Incorrect Account Number or Password!")
        
#=====CHECK BALANCE=======
def check_balance():
        done,ac_num,name = verification()
        if done:
                # Get latest balance from transactions.txt
                latest_balance = 0.0
                with open("transactions.txt", "r") as transactions_file:
                    t_lines = transactions_file.readlines()
                    for t_line in reversed(t_lines): # Read lines by reversed
                        t_fields = t_line.strip().split(',')
                        if len(t_fields) >= 4 and t_fields[0] == ac_num: # Verify the entered account number = account number from transaction.txt
                            try:
                                latest_balance = float(t_fields[3])
                            except ValueError:
                                pass
                            break
                # Get latest balance from transactions.txt
                latest_balance = 0.0
                with open("transactions.txt", "r") as transactions_file:
                    t_lines = transactions_file.readlines()
                    for t_line in reversed(t_lines):
                        t_fields = t_line.strip().split(',')
                        if len(t_fields) >= 4 and t_fields[0] == ac_num:
                            try:
                                latest_balance = float(t_fields[3])
                            except ValueError:
                                pass
                            print("💴  Now Your Balance Is: ", latest_balance)
                            break 
        else:                          
            print("❌  Incorrect Account Number or Password!")                  
                        
#======TRANSACTION HISTORY========= 
def transaction_history():
        done,ac_num,name = verification()
        if done:
                print("\n📜 Transaction History:")
                with open("transactions.txt", "r") as transactions_file:
                    t_lines = transactions_file.readlines()
                    found = False
                    for t_line in t_lines:
                        t_fields = t_line.strip().split(',')
                        if len(t_fields) >= 4 and t_fields[0] == ac_num:
                            print(f"📌 Type: {t_fields[1]}, Amount: {t_fields[2]}, Balance: {t_fields[3]}, Date: {t_fields[4]}")
                            found = True
                    if not found:
                        print("ℹ️  No transactions found for this account.")
                return  # Exit after showing history
        else:
            print("❌ Incorrect Account Number or Password!")

#=====CREATE CUSTOMER ACCOUNT=====
def create_customer_account():
    print("........Customer Account Creation Menue.......")
    ac_num=create_account_number()
    name=str(input("Enter Your Name: "))
    address=str(input("🏡  Enter Your Address: "))
    password=str(input("🗝️  Enter New Password: "))
    while True:
                try:
                    depAmount = float(input("Enter The Deposit Amount: "))
                    if depAmount > 0:
                        new_balance = 0 + depAmount
                        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        print("✅  Successful deposit! Your Deposit Amount Is:", depAmount)
                        print("💰  Now Your Balance Is:", new_balance)
                        with open("customers_accounts.txt", "a") as customers_file:
                            customers_file.writelines(f"{str(ac_num)},{name},{address},{password},{new_balance}\n")
                        with open("transactions.txt", "a") as transactions_file:
                            transactions_file.write(f"{ac_num},DEPOSIT,{depAmount},{new_balance},{now}\n")
                        return 
                    else:
                        print("💴  Invalid Deposit Amount. Must Be Greater Than 0.")
                        continue
                except ValueError:
                    print("❌  Invalid input. Please enter a valid number.")
                    continue
                return

#======MAIN MENU===========
def main_menu():
    while True:
            print("========Welcome To The Banking Application======")
            print("...............This Is Main Menu............")
            print("1️⃣  Admin Menu")
            print("2️⃣  Customer Menu")
            print("3️⃣  Exit")
            choose = input("Enter your choose (1,2,3): ")
            if choose == "1":
                admin_login()
            elif choose == "2":
                customer_login()
            elif choose == "3":       
                print("🤝  Thank You For Choosing Our Service! ❤️")
                break
            else:
                print("❌  Invalid Choose! Please Choose 1-3...")
        
#======ADMIN MENU===========
def admin_login():
    get_admin_user_name = str(input("Enter The Admin User Name: "))
    get_admin_password = str(input("🗝️  Enter The Admin Password: "))

    while True:
        if  admin_user_name == get_admin_user_name and admin_password == get_admin_password:
            print("========Welcome To The Banking Application======")
            print("...............This Is Admin's Menu............")
            print("1️⃣  Create Account")
            print("2️⃣  Deposit Money")
            print("3️⃣  Withdraw Money")
            print("4️⃣  Check Balance")
            print("5️⃣  Transaction History")
            print("6️⃣  Show Current Date")
            print("7️⃣  Back To Main Manu")
            choose = input("Enter your choose (1,2,3,4,5,6,7): ")
            if choose == "1":
                create_customer_account()
            elif choose == "2":
                deposit()
            elif choose == "3":
                Withdrawal()
            elif choose == "4":
                check_balance()
            elif choose == "5":
                transaction_history()
            elif choose == "6":
                current_date()     
            elif choose == "7":       
                break
            else:
                print("❌  Invalid Choose! Please Choose 1-7...")
        else:
                print("❌  Incorrect Username or password! Please Enter The Correct Username and Password.")
                break

#========CUSTOMER MENU========
def customer_login():
            done,ac,num,name = verification()
            if done:
                print("✅ Login Successful!")
                while True:
                    print("\n======== Welcome To The Banking Application ======")
                    print("............... Customer Menu ...............")
                    print("...............Hello! ", name , "...........")
                    print("1️⃣  Deposit Money")
                    print("2️⃣  Withdraw Money")
                    print("3️⃣  Check Balance")
                    print("4️⃣  Transaction History")
                    print("5️⃣  Show Current Date")
                    print("6️⃣  Back To Main Menu")

                    choose = input("Enter your choice (1-6): ")
                    if choose == "1":
                        deposit()
                    elif choose == "2":
                        Withdrawal()
                    elif choose == "3":
                        check_balance()
                    elif choose == "4":
                        transaction_history()  
                    elif choose == "5":
                        current_date()     
                    elif choose == "6":
                        return
                    else:
                        print("❌ Invalid Choice! Please select 1-6.")
            else:
                print("❌ Incorrect Account Number or Password! Please try again.") 
                          
main_menu()
#create_customer_account()     
#deposit()
#Withdrawal()
#transaction_history()
        