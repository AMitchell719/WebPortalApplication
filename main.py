from user import User
import webbrowser
import getpass

user1 = User('Mark', 'madCat243', 'IT', 468392, 2814838288)
user2 = User('Donatello', 'madCat243', 'HR', 468392, 2814838288)
user3 = User('Bryan', 'madCat243', 'Management', 468392, 2814838288)

flag = True
authorized = False
counter = 0

user_list = [user1, user2, user3]

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

    elif(user_object.role == 'HR'):
        webbrowser.open('http://localhost:5000/hr')

    elif(user_object.role == 'Management'):
        webbrowser.open('http://localhost:5000/management')
