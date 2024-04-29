import mysql.connector # type: ignore
import random
import os
import time
# In this project you will create an online banking program. Users need to 
# have an account number and PIN to identify themselves as owners of an 
# account. Once users get into the system they will have standard options: 
# check balance, deposit, and withdraw. Additionally, a new user or bank 
# administrator can also create a new account, close account, and modify 
# an account (such as edit name, PIN, or any other personal identification 
# required to open an account).


#connecting to MySQL table
connection = mysql.connector.connect(
    user = 'python_connection',
    database = 'bank_user_info',
    password = 'password9('
)
cursor = connection.cursor()


#introduction (welcome message, present options, ask user where they want to go)
def intro():
    os.system('cls')
    print("Welcome to the Elite Bank, please input 1 - 6 to go where you want to go:")
    options = ['create an account', 'delete an account', 'modify an account', 'check balance', 'withdraw', 'deposit']
    for option in options:
        print(f"{str(options.index(option) + 1)}. {option}")
    return input("")

def uniqueRandint():
    sql = "SELECT PIN FROM user_info"
    cursor.execute(sql)
    temp = random.randint(123456, 1000000)

    #if temp in PIN row in user_info, then it creates another unqiue temp
    for pin in cursor:
        if pin == temp:
           temp = random.randint(123456, 1000000)
    return temp

def getRow(user_PIN):
    try:
        sql = "SELECT * FROM user_info WHERE pin = %s"
        val = [user_PIN]
        cursor.execute(sql, val)
        return cursor.fetchone()
    except:
        print("Please enter a valid PIN.")

def confirm():
    user_choice = input("Are you sure you want to do this? (input 'yes' or 'no')\n").lower()
    if user_choice == 'yes':
        return True
    else:
        print("You will be returned to the main menu.")
        time.sleep(2)
        return main()

def creating_acc():
    user_name = input("Your first and last name: ")
    user_birth_date = input("Your birth date (mm/dd/yyyy): ")
    user_SSN = input("Your Social Security number (########): ")
    user_phone_number = input("Your phone number (##########): ")
    randomNum = uniqueRandint()

    #check user info
    if len(user_name) > 45:
        print("Please enter a name less than 45 characters.")
    if len(user_birth_date) > 10:
        print("Please enter a appropriate date.")
    if int(user_phone_number) > 9999999999:
        print("Please print an appropriate phone number.")

    if confirm():
        #send user info to MySQL
        sql = "INSERT INTO user_info (name, date, SSN, number, PIN, balance) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (user_name, user_birth_date, user_SSN, user_phone_number, randomNum, 0)
        cursor.execute(sql, val)
        connection.commit()

def deleting_acc():
    print("we have to ask your PIN for security")
    user_PIN = input("PIN: ")
    
    if confirm():
        #tries to delete account with user_PIN, else it quits
        try:
            sql = "DELETE FROM user_info WHERE PIN = %s"
            val = [user_PIN]
            cursor.execute(sql, val)
            connection.commit()
            print("Your account is successfully been deleted.")
        except:
            print("Please enter a valid PIN.")

def modify_acc():
    print("we have to ask your PIN for security")
    user_PIN = input("PIN: ")

    #prints all attributes in user_info
    print("\nPlease input one of the follwing attributes to modify your account: ")
    data = ['name', 'date', 'SSN (social security number)', 'number (phone number)']
    for attribute in data:
        print(attribute)

    #asks which attribute; and it's new and current value
    user_choice = input("\n").lower()
    user_confirm = input(f"What is the current {user_choice}: ")
    user_new = input(f"What would be the new {user_choice} be: ")

    #updates attribute to new value
    if confirm():
        try:
            sql = f"UPDATE user_info SET {user_choice} = %s WHERE PIN = %s AND {user_choice} = %s"
            val = [user_new, user_PIN, user_confirm]
            cursor.execute(sql, val)
            connection.commit()

            #if PIN is correct, print correctly changed otherwise hasn't
            if cursor == None:
                print("Please enter the valid information from before.")
            else:
                print(f"Your {user_choice} has been successfully changed.")
        except:
            print("Please enter the valid information from before.")
    # TODO-ish: compare account from before modification and after to see if the modification is successful.

def check_balance():
    print("we have to ask your PIN for security")
    try:
        user_PIN = int(input("PIN: "))
    except:
        print("Please enter a valid PIN.")

    if confirm():
        #gets account from user_PIN
        sql = "SELECT * FROM user_info WHERE pin = %s"
        val = [user_PIN]
        cursor.execute(sql, val)
        user_acc = cursor.fetchone()

    #prints balance from user_acc if correct PIN
    if cursor != None:
        print("balance: " + str(user_acc[(len(user_acc)) - 1]))
    else:
        print("Please enter a valid PIN.")

def change_balance(user_input):
    print("we have to ask your PIN for security")
    user_PIN = input("PIN: ")

    #gets account from user_PIN
    user_acc = getRow(user_PIN)

    #chaage balance by subtracting if user_input = 5, adding otherwise
    print()
    try:
        if user_input == '5':
            user_choice = int(input("How much do you want to withdraw: "))
            new_balance = user_acc[(len(user_acc)) - 1] - user_choice
        else:
            user_choice = int(input("How much do you want to deposit: "))
            new_balance = user_acc[(len(user_acc)) - 1] + user_choice
    except:
        print("Please enter the correction information.")
        quit()

    if confirm():
        #update balance with new balance
        sql = "UPDATE user_info SET balance = %s WHERE pin = %s"
        val = [new_balance, user_PIN]
        cursor.execute(sql, val)
        connection.commit()
        print("balance: " + str(new_balance))

def main():
    # send user where they wanna go from intro()
    user_input = intro()
    os.system("cls")
    #create a function for user to confirm their actions or go back to menu screen

    if user_input == "1":
        creating_acc()
    elif user_input == '2':
        deleting_acc()
    elif user_input == '3':
        modify_acc()
    elif user_input == '4':
        check_balance()
    elif user_input == '5' or user_input == '6':
        change_balance(user_input)
    else:
        print("Please enter a suitable number.")

main()

#printing every item in table
cursor.execute("SELECT * FROM user_info")
for item in cursor:
    print(item)

#close connection to MySQL
cursor.close()
connection.close()