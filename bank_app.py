from datetime import datetime
now=datetime.now()
ac_balances = 0
admin_user_name = "Admin"
admin_password = "Admin@123"

#===CREATE NEW ACCOUNT NUMBER====
def create_account_number():
    with open("customer_accounts.txt", "r") as customers_file:
        return f"{int(customers_file.readlines()[-1].split(",")[0])+1}"
    
#=====DEPOSIT FUNCTION=====
def deposit():
    global ac_balances
    while True:
        try:
            depAmount=float(input("Enter The Deposit Amount: "))
            if depAmount > 0:
                ac_balances= ac_balances + depAmount
                print("✅ Successfull deposit! Your Depost Amount Is: ", depAmount, "Now Your Balance Is: ", ac_balances)
            else:
                print("💴 Invalid Deposit Amount. Must Be Greater Than 0.")
                break
        except ValueError:
            print("❌ Invalid Input..")
            continue
        return ac_balances           

#=====WITHDRAWAL FUNCTION=====
def Withdrawal():
    global ac_balances
    while True:
        try:
            withAmount=float(input("Enter The Withdrawal Amount: "))
            if withAmount <= 0:
                print("💴 Invalid Widhrawal Amount. Must Be Greater Than 0.")
            elif withAmount <= ac_balances:
                ac_balances= ac_balances - withAmount
                print("✅ Successfull Withdrawal! Your Withdrawal Amount Is: ", withAmount, "Now Your Balance Is: ", ac_balances)
                break
            else:
                print("🪫💵Insufficien Balance.")
                continue
        except ValueError:
            print("❌ Invalid Input..")
            continue
        return ac_balances

#=====CREATE CUSTOMER ACCOUNT=====
def create_customer_account():
    print("........Customer Account Creation Menue.......")
    ac_num=create_account_number()
    name=str(input("Enter Your Name: "))
    address=str(input("🏡 Enter Your Address: "))
    password=str(input("🗝️ Enter New Password: "))
    deposit()
    with open("customer_accounts.txt", "a") as customers_file:
        customers_file.writelines(f"{str(ac_num)},{name},{address},{password},{ac_balances}\n")
    with open("transactions.txt", "a") as transactions_file:
        transactions_file.write(f"{ac_num}, Dip ,{ac_balances},{now}\n")

#======MAIN MENUE===========
def main_menue():
    while True:
            print("========Welcome To The Banking Application======")
            print("...............This Is Main Menue............")
            print("1️⃣ For Admin Menue")
            print("2️⃣ For Customer Menue")
            print("3️⃣ For Exit")
            choose = input("Enter your choose (1,2,3): ")
            if choose == "1":
                admin_login()
            elif choose == "2":
                customer_login()
            elif choose == "3":       
                print("🤝 Thank You For Choosing Our Service! ❤️")
                break
            else:
                print("❌ Invalid Choose! Please Choose 1-3...")
        
#======ADMIN MENUE===========
def admin_login():
    get_admin_user_name = str(input("Enter The Admin User Name: "))
    get_admin_password = str(input("🗝️ Enter The Admin Password: "))

    while True:
        if  admin_user_name == get_admin_user_name and admin_password == get_admin_password:
            print("========Welcome To The Banking Application======")
            print("...............This Is Admin's Menue............")
            print("1️⃣ For Create Account")
            print("2️⃣ For Deposit Money")
            print("3️⃣ For Withdrawal Money")
            print("4️⃣ For Check Balance")
            print("5️⃣ For Transaction History")
            print("6️⃣ For Exit")
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
                print("🤝 Thank You For Choosing Our Service! ❤️")
                break
            else:
                print("❌ Invalid Choose! Please Choose 1-6...")
        else:
                print("❌ Incorrect Username or password! Please Enter The Correct Username and Password.")

#========CUSTOMER MENUE========
def customer_login():
    get_customer_account_number = str(input("Enter The Account Number: "))
    get_customer_password = str(input("🗝️ Enter The Account Password: "))

    while True:
        if  admin_user_name == get_customer_account_number and admin_password == get_customer_password:
            print("========Welcome To The Banking Application======")
            print("...............This Is Customer's Menue............")
            print("1️⃣ For Deposit Money")
            print("2️⃣ For Withdrawal Money")
            print("3️⃣ For Check Balance")
            print("4️⃣ For Transaction History")
            print("5️⃣ For Exit")
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
                print("🤝 Thank You For Choosing Our Service! ❤️")
                break
            else:
                print("❌ Invalid Choose! Please Choose 1-5...")
        else:
                print("❌ Incorrect Username or password! Please Enter The Correct Username and Password.")                        

#create_customer_account()     

        