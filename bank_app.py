#import datetime
from datetime import datetime
now=datetime.now()
ac_balances=0
''''accounts=[]
auto_account_num=100001
#Function for create the account
def create_account():
    global auto_account_num
    global accounts
    name=str(input("Enter the account holder name: "))
    pin=(input("Enter the pin number: "))  
    try:
        initial_balance=float(input("Enter your first diposit amount: "))
        if initial_balance <= 0:
            print("Initioal balance is must be a positive....")
            return 
    except ValueError:
        print("Invalid input.....")      
        return
    account_number=auto_account_num
    auto_account_num += 1
    accounts=[f'\n{account_number},{name},{pin},{initial_balance}']
    with open("accounts.txt", "a") as file:
         file.writelines(accounts)
    #accounts[account_number]={"Name":name,"Balance":initial_balance,"Pin":pin}
    #with open("accounts.txt", 'a+') as file:
        #file.write(f'\n{str(accounts)}')
         print(f"*****Succssesfully Created your account***** \n .....Thank you for Join with us.....")
         print(f'Account holder name is: {name} \n Your account number is: {account_number}\n Now Your account balance is: {initial_balance}')
        #print(accounts)
create_account()

def account_num_verification():
    with open("accounts.txt", "r") as file:
        for line in file.readlines([]):
            line +=line
            check=list(file.readlines([line]))
        print(check)
account_num_verification()        '''

       #===GET DATA FROME USER==== 
def get_data_create_account():
    name=str(input("Enter your name: "))
    address=str(input("Enther your address: "))
    pin_number=str(input("Enter new pin number: "))
    return(name,address,pin_number)

       #===CREATE NEW ACCOUNT NUMBER====
def create_account_number():
    with open("customer_account.txt", "r") as customer_file:
        return f"{int(customer_file.readlines()[-1].split(",")[0][1:])+1}"
    
       #=====DEPOSIT FUNCTION=====
def deposit():
    global ac_balances
    try:
        depAmount=float(input("Enter the deposit amount: "))
        if depAmount > 0:
            ac_balances= ac_balances + depAmount
            print("Successfull deposit! Your depost amount is: ", depAmount, "Now your balance is: ", ac_balances)
        else:
            print("Invalid deposit amount. Must be greater than 0.")
    except ValueError:
        print("Invalid Input..")            

        #=====WITHDRAWAL FUNCTION=====
def Withdrawal():
    #global ac_balances
    try:
        withAmount=float(input("Enter the withdrawal amount: "))
        if withAmount <= 0:
            print("Invalid widhrawal amount. Must be greater than 0.")
        elif withAmount <= ac_balances:
            ac_balances= ac_balances - withAmount
            print("Successfull withdrawal! Your withdrawal amount is: ", withAmount, "Now your balance is: ", ac_balances)
        else:
            print("Insufficien balance.")
    except ValueError:
        print("Invalid input..")

def transaction():
    with open("transactions.txt", "a") as transactions_file:
        transactions_file.write()


#=====CREATE CUSTOMER ACCOUNT=====
def create_customer_account():
    get_data_create_account()
    create_account_number()
    deposit()
    with open("customer_account.txt", "a") as customer_file:
        customer_file.writelines f"{create_account_number()},{get_data_create_account(name)},
        {get_data_create_account(address)},{get_data_create_account(pin_number)},{deposit(depAmount)}"

    with open("transactions.txt", "a") as transactions_file:
        transactions_file.write(f"{create_account_number()}, D ,{deposit(depAmount)},{now}")    

create_customer_account()     

        