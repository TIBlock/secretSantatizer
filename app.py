# import all relevent libraries and files needed to make things run
from users import Users
from logic import create_user, user_list1
# from flask import Flask
from flask_mail import Mail, Message

# create global veriables that will be used in the application

# ToDo = update logic to use a different list for each group you faciliatate => user_list1 = []


# start the application with a while loop
def menu():
    print('Welcome to the Secret Santatizer App!')

    selection = input("Enter 'a' to add a new user, "
                        "\n'u' to update a current user, "
                        "\n'c' to create your pairs, "
                        "\nor 'q' to quit ")
    while selection != 'q':
        # Create conditionals (if/elif/else) statements based on user selection
        # 
        # What should happen if user chooses 'a'?
        
        if selection == 'a':
            create_user()
            
            selection = input("Enter 'a' to add a new user, "
                        "\n'u' to update a current user, "
                        "\n'c' to create your pairs, "
                        "\nor 'q' to quit ")
            

        # What should happen if user chooses 'u'?

        elif selection == 'u':
            for i in range(len(user_list1)):
                print(f'{i}: {user_list1[i]}')
            edit_menu = int(input("Which User would you like to update?: "))
            
            if edit_menu == '':
                print('Please select a valid option')
                edit_menu = int(input("Which User would you like to update?: "))
            else:
                print(f'You have selected {user_list1[edit_menu]}')
                
                options = int(input("Please choose option to update: "
                                    "\n 1 = Update user email"
                                    "\n 2 = Update user first name"
                                    "\n 3 = Update user last name"
                                    "\n 4 = Add user's partner"))

                if options == 1:
                    user_list1
                    email = self.email

                elif options == 2:
                    pass

                elif options == 3:
                    pass

                elif options == 4:
                    pass

                else:
                    print('Your selection was invalid. Please choose a valid option')

                    options = int(input("Please choose option to update: "
                                    "\n 1 = Update user email"
                                    "\n 2 = Update user first name"
                                    "\n 3 = Update user last name"
                                    "\n 4 = Add user's partner"))


        # What should happen if user chooses 'c'?

        elif selection == 'c':
            pass
        # How do you end the loop if user chooses 'q'

        elif selection == 'q':
            quit

        else:
            print("You did not enter a valid option. Please select a valid option.")
            selection = input("Enter 'a' to add a new user, "
                        "\n'u' to update a current user, "
                        "\n'c' to create your pairs, "
                        "\nor 'q' to quit ")
        # Pass will be deleted when you create all the conditional logic (if/else statements)
        pass

        


            # display options for user to choose from

            # create user should be first option and run several functions at once
            
menu()



