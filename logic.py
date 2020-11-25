from users import Users
users = [
    {'user': 'user1', 'user_id': 1, 'u_f_name': 'Taylor', 'u_l_name': 'Blocker', 'u_has_partner': True},
    {'user': 'user2', 'user_id': 2, 'u_f_name': 'Tay', 'u_l_name': 'Blocker', 'u_has_partner': True},
    {'user': 'user3', 'user_id': 3, 'u_f_name': 'Tylor', 'u_l_name': 'Blocker', 'u_has_partner': True},
    {'user': 'user4', 'user_id': 4, 'u_f_name': 'Tlor', 'u_l_name': 'Blocker', 'u_has_partner': True},
    {'user': 'user5', 'user_id': 5, 'u_f_name': 'Taylr', 'u_l_name': 'Blocker', 'u_has_partner': True},
    {'user': 'user6', 'user_id': 6, 'u_f_name': 'Taylo', 'u_l_name': 'Blocker', 'u_has_partner': True},
]

user_list1 = []
# Create user

def create_user():
    user_count = 0

    if user_count == 0:
        print("Please input your first user")
        u_id = 1
        u_f_name = input("What is the user's first name?: ")
        u_l_name = input("What is the user's last name?: ")
        u_has_partner = input("Does the user have a partner? Y or N: ")
        if u_has_partner.lower() == 'y':
            u_has_partner = True
        else:
            u_has_partner = False

        user_count += 1
    else:
        print("Please input your next user")
        u_id = int(input('Which user is this?: '))
        u_f_name = input("What is the user's first name?: ")
        u_l_name = input("What is the user's last name?: ")
        u_has_partner = input("Does the user have a partner? Y or N: ")
        if u_has_partner.lower() == 'y':
            u_has_partner = True
        else:
            u_has_partner = False

        user_count += 1

    return user_count

# print(create_user())  
print(users)
print(' ')

for user in users:
    user['user'] = Users(user['user_id'], user['u_f_name'], user['u_l_name'], user['u_has_partner'])
    user_list1.append(user['user'])

for l in user_list1:
    print(l)

print(' ')
print(users[0])
# Add user to user_list and id to user_id_list

# Check for and add partner if they have one

# Remove partner from self.pair_list

# Pair user with someone to give a gift to

# Pair user with someone to get a gift from

# Send email to all users when everyone is paired

# Send user to Taylor with full list (test only) and email for pairs all set and sent with option to see the full list(production)