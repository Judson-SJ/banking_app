from datetime import datetime
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
admin_user_name = "Admin"
admin_password = "Admin@123"

#===CREATE NEW ACCOUNT NUMBER====
def create_account_number():
    with open("customers_accounts.txt", "r") as customers_file:
        return f"{int(customers_file.readlines()[-1].split(",")[0])+1}"
    
#=====DEPOSIT FUNCTION=====
def deposit():
    get_customer_account_number = input("Enter The Account Number: ")
    get_customer_password = input("🗝️  Enter The Account Password: ")

    # Verify account
    with open("customers_accounts.txt", "r") as customers_file:
        lines = customers_file.readlines()
        for line in lines:
            fields = line.strip().split(',')
            if len(fields) < 4:
                continue
            account_number = fields[0]
            customer_password = fields[3]

            if account_number == get_customer_account_number and customer_password == get_customer_password:
                # Get latest balance from transactions.txt
                latest_balance = 0.0
                with open("transactions.txt", "r") as transactions_file:
                    t_lines = transactions_file.readlines()
                    for t_line in reversed(t_lines):
                        t_fields = t_line.strip().split(',')
                        if len(t_fields) >= 4 and t_fields[0] == get_customer_account_number:
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
                            #now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            print("✅  Successful deposit! Your Deposit Amount Is:", depAmount)
                            print("💰  Now Your Balance Is:", new_balance)

                            with open("transactions.txt", "a") as transactions_file:
                                transactions_file.write(f"{get_customer_account_number},DEPOSIT,{depAmount},{new_balance},{now}\n")
                            return  # Exit after successful deposit
                        else:
                            print("💴  Invalid Deposit Amount. Must Be Greater Than 0.")
                    except ValueError:
                        print("❌  Invalid input. Please enter a valid number.")
                return  

        print("❌  Incorrect Account Number or Password!")

#=====WITHDRAWAL FUNCTION=====
def Withdrawal():
    get_customer_account_number = input("Enter The Account Number: ")
    get_customer_password = input("🗝️  Enter The Account Password: ")

    # Verify account
    with open("customers_accounts.txt", "r") as customers_file:
        lines = customers_file.readlines()
        for line in lines:
            fields = line.strip().split(',')
            if len(fields) < 4:
                continue
            account_number = fields[0]
            customer_password = fields[3]

            if account_number == get_customer_account_number and customer_password == get_customer_password:
                # Get latest balance from transactions.txt
                latest_balance = 0.0
                with open("transactions.txt", "r") as transactions_file:
                    t_lines = transactions_file.readlines()
                    for t_line in reversed(t_lines):
                        t_fields = t_line.strip().split(',')
                        if len(t_fields) >= 4 and t_fields[0] == get_customer_account_number:
                            try:
                                latest_balance = float(t_fields[3])
                            except ValueError:
                                pass
                            break
                while True:        
                            try:
                                withAmount=float(input("Enter The Withdrawal Amount: "))
                                if withAmount <= 0:
                                    print("💴  Invalid Widhrawal Amount. Must Be Greater Than 0.")
                                elif withAmount <= latest_balance:
                                    latest_balance= latest_balance - withAmount
                                    print("✅  Successfull Withdrawal! Your Withdrawal Amount Is: ", withAmount, "Now Your Balance Is: ", latest_balance)
                                    with open("transactions.txt", "a") as transactions_file:
                                            transactions_file.write(f"{get_customer_account_number},WITHDRAWAL,{withAmount},{latest_balance},{now}\n")
                                            return  # Exit after successful withdrawal
                                else:
                                    print("🪫💵 Insufficient Balance.")
                                    continue
                            except ValueError:
                                print("❌  Invalid Input..")
                            return                   
        print("❌  Incorrect Account Number or Password!")
                          

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

#======MAIN MENUE===========
def main_menu():
    while True:
            print("========Welcome To The Banking Application======")
            print("...............This Is Main Menu............")
            print("1️⃣  For Admin Menu")
            print("2️⃣  For Customer Menu")
            print("3️⃣  For Exit")
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
        
#======ADMIN MENUE===========
def admin_login():
    get_admin_user_name = str(input("Enter The Admin User Name: "))
    get_admin_password = str(input("🗝️  Enter The Admin Password: "))

    while True:
        if  admin_user_name == get_admin_user_name and admin_password == get_admin_password:
            print("========Welcome To The Banking Application======")
            print("...............This Is Admin's Menu............")
            print("1️⃣  For Create Account")
            print("2️⃣  For Deposit Money")
            print("3️⃣  For Withdrawal Money")
            print("4️⃣  For Check Balance")
            print("5️⃣  For Transaction History")
            print("6️⃣  For Back To Main Manu")
            choose = input("Enter your choose (1,2,3,4,5,6): ")
            if choose == "1":
                create_customer_account()
            elif choose == "2":
                deposit()
            elif choose == "3":
                Withdrawal()
            elif choose == "4":
                print("Check balance")
            elif choose == "5":
                print("Transaction History") 
            elif choose == "6":       
                #print("🤝  Thank You For Choosing Our Service! ❤️")
                break
            else:
                print("❌  Invalid Choose! Please Choose 1-6...")
        else:
                print("❌  Incorrect Username or password! Please Enter The Correct Username and Password.")
                break

#========CUSTOMER MENUE========
def customer_login():
    get_customer_account_number = input("Enter The Account Number: ")
    get_customer_password = input("🗝️  Enter The Account Password: ")

    with open("customers_accounts.txt", "r") as customers_file:
        lines = customers_file.readlines()
        for line in lines:
            fields = line.strip().split(',')
            if len(fields) < 4:
                continue  # skip malformed lines
            account_number = fields[0]
            customer_password = fields[3]         
    while True:
        if account_number == get_customer_account_number and customer_password == get_customer_password:
            print("========Welcome To The Banking Application======")
            print("...............This Is Customer's Menue............")
            print("1️⃣  For Deposit Money")
            print("2️⃣  For Withdrawal Money")
            print("3️⃣  For Check Balance")
            print("4️⃣  For Transaction History")
            print("5️⃣  For Back To Main Manu")
            choose = input("Enter your choose (1,2,3,4,5): ")
            if choose == "1":
                deposit()
            elif choose == "2":
                Withdrawal()
            elif choose == "3":
                print("Check balance")
            elif choose == "4":
                print("Transaction History") 
            elif choose == "5":       
                #print("🤝  Thank You For Choosing Our Service! ❤️")
                break
            else:
                print("❌  Invalid Choose! Please Choose 1-5...")
        else:
                print("❌  Incorrect Username or password! Please Enter The Correct Username and Password.")
                break                        

#create_customer_account()
main_menu()     
#deposit()
#Withdrawal()
        