import random

user_list = []

class User:
    def __init__(self, f_name, l_name, email, partner_f_name, partner_l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.partner_f_name =partner_f_name 
        self.partner_l_name = partner_l_name
        self.pair_list = []
        self.gift_receipient = []
        self.gift_giver = []
    

    # def __str__(self):
    #     print(f"{self.f_name} {self.l_name}")

def create_user():
    first_name = input("Please enter the user's first name: ")
    last_name = input("Please enter the user's last name: ")
    email = input("Please input the user's email address: ")
    partner_f_name = input("Please enter the partner's first name: ")
    partner_l_name = input("Please enter the partner's last name: ")

    user_data = User(first_name, last_name, email, partner_f_name, partner_l_name)

    return user_data
    

def print_user_details(user):
    # Print out a string that tells the user important information about this student
    print(f"{user.f_name} {user.l_name}, email: {user.email}, partner: {user.partner_f_name} {user.partner_l_name}.")
   
def print_user_list(users):
    for i, user in enumerate(users):
        print(f"User: {i}")
        print_user_details(user)
        print(' ')

def pick_secret_santa_options(user_list):
    # For each user function has to pick a random user and set that person as the recipient
    

    for user in user_list:
        giver = user.gift_giver
        recipient = user.gift_receipient

        user.pair_list.append(user_list)
        giver = random.choice(user.pair_list)
        recipient = random.choice(user.pair_list)
        
        
        # print(user.gift_giver, user.gift_receipient)
        print(f"{user.f_name} {user.l_name} will give a gift to {recipient[0]} {recipient[1]} and get a gift from {giver[0]} {giver[1]}")

    # If selected recipient == partner, do it again. 
    # If selected user is already selected, do it again. 
    # Each user will have an index number.
    # We can use the index number to make all selections.

def pick_gift_giver(user, user_list):
    pass

def send_email(user):
    pass


def menu():
    
    selection = input("Enter 'p' to print the user list, "
                        "\n'a' to add a new user, "
                        "\n'x' to pair user, "
                        "\nor 'q' to quit. "
                        "\nEnter your selection: ")
    while selection != 'q':
        if selection == 'p':
            print_user_list(user_list)
        elif selection == 'a':
            user_list.append(create_user())  
        elif selection == 'x':
            pick_secret_santa_options(user_list)
            
        # elif selection == 'a':
        #     student_id = int(input("Enter the student ID to add a mark to: "))
        #     student = student_list[student_id]
        #     new_mark = int(input("Enter the new mark to be added: "))
        #     add_mark(student, new_mark)

        selection = input("Enter 'p' to print the user list, "
                        "\n'a' to add a new user, "
                        "\n'x' to add a mark to a user, "
                        "\nor 'q' to quit. "
                        "\nEnter your selection: ")

menu()


