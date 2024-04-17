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
    print("1. create an account")
    print("2. delete an account")
    print("3. modify an accounte")
    print("4. check balance")
    print("5. withdraw")
    print("6. deposit")
    return input("")

def creating_acc():
    user_name = input("Your first and last name: ")
    user_birth_date = input("Your birth date (mm/dd/yyyy): ")
    user_SSN = input("Your Social Security number (########): ")
    user_phone_number = input("Your phone number (##########): ")
    randomNum = random.randint(123456, 1000000)

    #check user info
    if len(user_name) > 45:
        print("Please enter a name less than 45 characters")
    if len(user_birth_date) > 10:
        print("Please enter a appropriate date")
    if int(user_phone_number) > 9999999999:
        print("Please print an appropriate phone number")

    #send user info to MySQL
    sql = "INSERT INTO user_info (name, date, SSN, number, PIN, balance) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (user_name, user_birth_date, user_SSN, user_phone_number, randomNum, 0)
    cursor.execute(sql, val)
    connection.commit()

def deleting_acc():
    print("we have to ask your PIN, account number, and name for security")

    user_AC = input("Account number: ")
    user_PIN = input("PIN: ")
    user_name = input("Name: ")

    table_AC = getRow()
    table_PIN = getRow()
    table_name = getRow()
    
    #Makes sure user data matches table data for id, PIN, and name
    if table_AC == table_name == table_PIN:
        # TODO: figure out how to make the condition for the WHERE apply to anything
        sql = "DELETE FROM user_info WHERE PIN = 0"
        val = (user_PIN)
        cursor.execute(sql)
        connection.commit()


        # TODO-ish: Debug line to make sure id for all accounts is correct
        #ALTER TABLE user_info AUTO_INCREMENT = 1;
    else:
        print("Please input the right information corresponding to your account details.")

#gets a row from user_info table
def getRow():
    # TODO: figure out how to make the condition for the WHERE apply to anything
    a = "1"
    sql = f"SELECT * FROM user_info WHERE id = {a}"
    val = (1)
    cursor.execute(sql)
    return cursor.fetchone()


# send user where they wanna go from intro()
# user_input = intro()
# if user_input == "1":
#    creating_acc()
# elif user_input == '2':
#     deleting_acc()


#printing every item in table
cursor.execute(testQuery)
for item in cursor:
    print(item)


#close connection to MySQL
cursor.close()
connection.close()

#(1, ';ldksfj', 'lskdjf', 91283, 9283, 0, 0)