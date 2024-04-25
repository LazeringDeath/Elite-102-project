import mysql.connector # type: ignore
import random
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
testQuery = ("SELECT * FROM user_info")


#introduction (welcome message, present options, ask user where they want to go)
def intro():
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

    #send user info to MySQL
    sql = "INSERT INTO user_info (name, date, SSN, number, PIN, balance) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (user_name, user_birth_date, user_SSN, user_phone_number, randomNum, 0)
    cursor.execute(sql, val)
    connection.commit()

def deleting_acc():
    print("we have to ask your PIN for security")
    user_PIN = input("PIN: ")
    
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
    print("Please input one of the follwing attributes to modify your account: ")
    data = ['name', 'date', 'SSN (social security number)', 'number (phone number)']
    for attribute in data:
        print(attribute)

    #asks which attribute; and it's new and current value
    user_choice = input("").lower()
    user_confirm = input(f"What is the current {user_choice}: ")
    user_new = input(f"What would be the new {user_choice} be: ")

    #updates attribute to new value
    sql = f"UPDATE user_info SET {user_choice} = %s WHERE PIN = %s AND {user_choice} = %s"
    val = [user_new, user_PIN, user_confirm]
    cursor.execute(sql, val)
    connection.commit()
    # TODO: compare account from before modification and after to see if the 
    # modification is successful.

def check_balance():
    pass



# send user where they wanna go from intro()
user_input = intro()
if user_input == "1":
   creating_acc()
elif user_input == '2':
    deleting_acc()
elif user_input == '3':
    modify_acc()
elif user_input == '4':
    check_balance()


#printing every item in table
cursor.execute(testQuery)
for item in cursor:
    print(item)


#close connection to MySQL
cursor.close()
connection.close()

#(1, ';ldksfj', 'lskdjf', 91283, 9283, 0, 0)