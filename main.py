# In this project you will create an online banking program. Users need to 
# have an account number and PIN to identify themselves as owners of an 
# account. Once users get into the system they will have standard options: 
# check balance, deposit, and withdraw. Additionally, a new user or bank 
# administrator can also create a new account, close account, and modify 
# an account (such as edit name, PIN, or any other personal identification 
# required to open an account).


#introduction (welcome message, ask account number and PIN)
def intro():
    print("Welcome to the Elite Bank, please input your account number and PIN to access your account.")
    return input("If you do not have an account, input 'new' to create one.\n")


#if new user: create, close, or modify an account

def creating_acc():
    user_name = input("Your first and last name: ")
    user_birth_date = input("Your birth date (mm/dd/yyyy): ")
    user_SSN = input("Your Social Security number (###-##-###): ")
    user_phone_number = input("Your phone number (###-###-####): ")
    # check user info is in right format
    # send user info to table

#present standard options (check balance, deposit and withdraw)

if intro() == "new":
    creating_acc()