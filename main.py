from user import User
import webbrowser
import getpass

user1 = User('Mark', 'madCat243', 'IT', 1528839, 2814838288)
user2 = User('Donatello', 'madCat243', 'HR', 5639202, 2053924282)
user3 = User('Bryan', 'madCat243', 'Management', 2468392, 2815223838)
user4 = User('Paige', 'madCat243', 'Customer', 2739201, 7138553535)
user5 = User('Chad', 'madCat243', 'IT-User', 3729183, 7134458763)

flag = True
authorized = False
counter = 0

user_list = [user1, user2, user3, user4, user5]

print('Welcome to the Company Portal')
print('*****************************\n')

print('Please enter your username: ')
username = input()

print('\n')

#print('Please enter your password: ')
password = getpass.getpass('Please enter your password: \n')

print('Querying database...\n')

# Loop through each user to check their credentials
for user in user_list:
    if(user.username == username and user.password == password):
        user_object = user_list[counter]
        flag = False
        authorized = True
    else:
        counter += 1

# Incorrect credentials should open a password reset page
if(authorized == False):
    print('Error: Wrong username or password')
    webbrowser.open('http://localhost:5000/reset')

# Begin role checking for access to the proper portal
if(authorized == True):
    if(user_object.role == 'IT'):
        webbrowser.open('http://localhost:5000/itadmin')

    elif(user_object.role == 'IT-User'):
        webbrowser.open('http://localhost:5000/ituser')

    elif(user_object.role == 'HR'):
        webbrowser.open('http://localhost:5000/hr')

    elif(user_object.role == 'Management'):
        webbrowser.open('http://localhost:5000/management')

    elif(user_object.role == 'Customer'):
        webbrowser.open('http://localhost:5000/customer')
