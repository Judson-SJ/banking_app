import datetime

accounts=[]
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
account_num_verification()        
