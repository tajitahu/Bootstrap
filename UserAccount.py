#User account page

import time
import random
from datetime import datetime
import hashlib



ACCOUNTS = {}
LOGINS = {}

class GuestAccount:
    def __init__ (self, account, title, name, age, email, address, phone_number):
        """Guest Account details"""
        self.account = account
        self.title = title
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.phone_number =phone_number
        self.is_member = True
    def display_info(self):
        print("Account Number: " + self.account, "\n")
        print("Name: " + self.title + " " + self.name)
        print("Age: " + self.age)
        print("Email: " + self.email)
        print("Address: " + self.address)
        print("Phone Number: " + self.phone_number)

class MembersAccount:
    def __init__ (self, account, title, name, age, email, address, phone_number, points):
        """Special Members Account details"""
        self.account = account
        self.title = title
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.points = points
        self.is_guest = True
    def display_info(self):
        print("Account Number: " + self.account, "\n")
        print("Name: " + self.title + " " + self.name)
        print("Age: " + self.age)
        print("Email: " + self.email)
        print("Address: " + self.address)
        print("Phone Number: " + self.phone_number)
        print("Points: "+ self.points)
    
class AdminAccount:
    def __init__ (self, name, role, enum, ):
        """Guest Account details"""
        self.name = name
        self.role = role
        self.enum = enum
        self.is_admin = True
    def display_info(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Employee Number:", self.enum)

def take_age():
    """Used to calculate guests Age"""
    global day
    global month
    global year
    day = int(input("\nEnter your birthdate day (DD): "))
    while not (1<= day <=31):
        print("That is not a valid day, choose a number between 01 and 31 please.")
        day = int(input("Enter your birthdate day (DD): "))
    month = int(input("Enter your birthdate month (MM): "))
    while not (1<= month <=12):
        print("That is not a valid month, please enter a number between 01 and 12")
        month = int(input("Enter your birthdate month (MM): "))
    year = int(input("Enter your birthdate year (YYYY): "))
    while not (1900<= year <=2005):
        if year < 1900:
            print("Sorry we don't allow vampire guests at the resort. It's bad for business...")
            year = int(input("Enter your birthdate year (YYYY): "))
        elif year > 2005:
            print("Sorry you have to be over 18 to create a guest account for The Omeya Resort...")
            year = int(input("Enter your birthdate year (YYYY): "))
        else:
            print("Error....")
            year = int(input("Enter your birthdate year (YYYY): "))
    def calculate_age(YY,MM,YYYY):
       global correct
       today = datetime.now()
       age_year = today.year - year
       if today.month > month and today.day > day:
          age = age_year
       else:
          age = age_year -1
       age = str(age)
       print("\nyour age is: " + age)
       correct = input("Is this correct? (y/n): ")
       correct = correct.lower()
       while correct != "y" and correct != "n":
            print("Please select 'y' or 'n'")
            print("your age is: " + age)
            correct = input("Is this correct? (y/n): ")
            correct = correct.lower()
       if correct == "n":
               take_age()
    calculate_age(day,month,year)

def hash_password(password):
    global hashed_password
    password = str(password)
    h = hashlib.new("sha256")
    h.update(password.encode())
    hashed_password = h.hexdigest()
    confirm = input("Please confirm your password: ")
    confirm = str(confirm)
    while hashed_password != hashlib.sha256(confirm.encode()).hexdigest():
        print("\nThose passwords do not match...")
        h = hashlib.new("sha256")
        password = input("\nPlease create a password: ")
        password = str(password)
        h.update(password.encode())
        hashed_password = h.hexdigest()
        confirm = input("Please confirm your password: ")
        confirm = str(confirm)
    print("Your password has been confirmed")
    LOGINS[account_num] = hashed_password
    return hashed_password

def take_name():
    """Takes the users name"""
    global title
    title = input("\nEnter your title: ")
    title = title[0].upper() + title[1:].lower()
    first = input("\nEnter your first name: ")
    first = first[0].upper() + first[1:].lower()
    middle = input("Would you like to enter a middle name? (y/n): ")
    middle = middle.lower()
    while middle != "y" and middle != "n":
        print("Please choose either y or n")
        middle = input("Would you like to enter a middle name? (y/n): ")
        middle = middle.lower()
    if middle == "y": 
        middle_name = input("What is your middle name?: ")
        middle_name = middle_name[0].upper() + middle_name[1:].lower()
    last = input("Please Enter your last name: ")
    last = last[0].upper() + last[1:].lower()
    global name
    if middle == "y":
        name = first + " " + middle_name + " " + last
    if middle == "n":
        name = first + " " + last

def take_email():
    global email
    email = input("\nPlease enter your email address: ")
    email = email.lower()

    while "@my.ntu.ac.uk" not in email and "n" not in email:
        print("Sorry... You must have access to an NTU email to create a guest account")
        email = input("Please enter your email address: ")
    notifications = input("Are you happy to receieve email notifications? (y/n): ")
    while notifications != "y" and notifications != "n":
        print("That is not a valid answer, please enter either y or n.")
        time.sleep(2)
        notifications = input("Are you happy to receieve email notifications? (y/n): ")
    notifications = notifications.lower()
    if notifications == "y":
        print("Great, you will receive email notifications for purchases and bookings.")
    else:
        print("Okay, you will not receive email notifications for purchases and bookings.")

def take_address():
    first_line = input("\nPlease enter your first line of address: ")
    second_line = input("Please enter your second line of address: ")
    city = input("Please enter your town/city: ")
    country = input("Please enter your country: ")
    postcode = input("Please enter your postcode: ")
    global address
    address = first_line + "\n" + second_line + "\n" + city + "\n" + country + "\n" + postcode

def take_number():
    global number
    number = int(input("\nPlease enter your phone number(Do not use + or *): "))
    while not (10<= len(str(number)) <=12):
        print("That number is not the correct length")
        number = int(input("\nPlease enter your phone number: "))

def create_guest_account():
    """Create a guest account"""
    new_account_num = random.randint(2000, 2999)
    while new_account_num in ACCOUNTS:
        new_account_num = random.randint(2000, 2999)
    global account_num
    account_num = new_account_num
    name = take_name()
    age = take_age()
    email = take_email()
    address = take_address()
    number = take_number()
    time.sleep(3)
    print("\nThank you for your details. Your Guest Account has been created.")
    time.sleep(2)
    print("You can access and change your details within the account menu")
    time.sleep(2)
   
    print("\nYour account number is " + str(account_num))
    print("You can access this in the account menu")
    input("Press enter to continue: ")
    print("\nIt is time to create your login details.")
    time.sleep(2)
    print("Your username is your account number: " + str(account_num))
    time.sleep(2)
    print("\nIt is now time to create a password. Your're password is secure in our system.")
   
    password = input("\nEnter a password: ")
    hash_password(password)
    ACCOUNTS[account_num] = name
    LOGINS[account_num] = hashed_password
    account_num = GuestAccount(account_num, title, name, age, email, address, number)
def create_members_account():
    """Create a Special Members account"""
    new_account_num = random.randint(2000, 2999)
    while new_account_num in ACCOUNTS:
        new_account_num = random.randint(2000, 2999)
    account_num = new_account_num
    name = take_name()
    age = take_age()
    email = take_email()
    address = take_address()
    take_number()
    time.sleep(3)
    points = 0
    print("\nThank you for your details. Your Special Members Account has been created.")
    time.sleep(2)
    print("You currently have", points, "points.")
    time.sleep(2)
    print("For every £1 you spend in the Special Members Hub, you will receive 1 point")
    time.sleep(2)
    account_num = MembersAccount(account_num, title, name, age, email, address, number, points)
    print("Your account number is " + str(account_num))
    print("You can access this in the account menu")
    input("\nPress enter to continue: ")


    print("\nIt is time to create your login details.")
    time.sleep(2)
    print("Your username is your account number: " + str(account_num))
    time.sleep(2)
    print("\nIt is now time to create a password. Your're password is secure in our system.")
    password = input("\nPlease create a password: ")
    hash_password(password)
    ACCOUNTS[account_num] = name
    
    


def create_admin_account():
    """Create an Admin account"""
    new_account_num = random.randint(2000, 2999)
    while new_account_num in ACCOUNTS:
        new_account_num = random.randint(2000, 2999)
    enum = new_account_num
    take_name()
    role = input("\nPlease enter your job role: ")
    time.sleep(2)
    account_num = AdminAccount(name, role, enum)
    print("Your Employee/Account number is", str(enum))
    print("You can access this in the account menu")
    input("Press enter to continue.")
    print("\nIt is time to create your login details.")
    time.sleep(2)
    print("Your password is entirely secure in our system.")
    time.sleep(2)
    print("Your username is your account number: " + str(enum))
    print("\nIt is now time to create a password. Your're password is secure in our system.")

    password = input("\nPlease create a password: ")
    hash_password(password)
    ACCOUNTS[account_num] = name
  


      
print("\t\t\tWelcome to the User Account Menu")

#List the different types of user accounts
print("\n\nFirst choose the account that you want to create...\n")
print("Note: You have been given access to create a Special Members account.")

def account_types():
    """Prints the different account types"""
    print("""
 1. Guest - Suitable for all guests looking to stay at our resort
 2. Special Member - Suitable for significantly important guests looking to stay at our resort
 3. Administrator - Suitable for resort staff members\n
""")
    
#Let member select which account they are signing into (Guest, Special Member, Administrator)
account_types()
account_type = int(input("Select an account (1-3): "))

while account_type not in (1, 2, 3): 
    print("That is not a valid account type... Please select a number 1-3")
    account_type = int(input("Select an account (1-3)"))

#This is used as an indicator to whether the account has been created. I will add 1 when an account has been created then reset the value to 0 
account_created = 0

while account_created < 1:
    if account_type == 1:
        correct = input("You have selected a guest account. Is this correct? (y/n): ")
        correct = correct.lower()
        if correct == "y":
            print("Great... Let's proceed in setting up your Guest Account.")
            time.sleep(2)
            create_guest_account()
            account_created += 1
        elif correct == "n":
            print("No problem.")  
            time.sleep(2)
            account_type = int(input("Select an account (1-3)")) 
        else:
            print("That's not a valid chocie...")
            time.sleep(2)
            account_type = int(input("Select an account (1-3)"))
    elif account_type == 2:
        correct = input("You have selected a Special Members account! Is this correct? (y/n): ")
        correct = correct.lower()
        if correct == "y":
            print("Great... Let's proceed in setting up your Special Members Account.")
            create_members_account()
            account_created += 1
        elif correct == "n":
            print("No problem.")    
            time.sleep(2)
            account_type = int(input("Select an account (1-3)"))
        else:
            print("That's not a valid chocie...")
            time.sleep(2)
            account_type = int(input("Select an account (1-3)"))
    elif account_type == 3:
        correct = input("You have selected an Administrator Account Is this correct? (y/n): ")
        correct = correct.lower()
        if correct == "y":
            print("Great... Let's proceed in setting up your Admin Account.")
            create_admin_account()
            account_created += 1
        elif correct == "n":
            print("No problem.")    
            time.sleep(2)
            account_type = int(input("Select an account (1-3)"))
        else:
            print("That's not a valid chocie...")
            time.sleep(2)
            account_type = int(input("Select an account (1-3)"))
    else:
        print("Error... Please select a valid account number...")
        time.sleep(2)
        account_type = int(input("Select an account (1-3)"))
         
#Hash the users password so that only they can know what it is
#salt and hash

#The user will then enter their account where they have access to:
#My details 
#Call reception (A help line with automated responses)
#Purchases and Receipts
#Check in
#Check Out

#They will then be gievn the option to go to the:
#Booking Portal
#Special Members Hub