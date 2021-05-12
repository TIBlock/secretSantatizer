# some of this is usable and should be modified to work in the new format
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(80))
    l_name = db.Column(db.String(80))
    has_partner = db.Column(db.Boolean)
    partner_id = db.Column(db.Integer)
    pair_list = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def __init__(self, f_name, l_name, has_partner, pair_list, email):
        self.f_name = f_name
        self.l_name = l_name
        self.has_partner = has_partner
        self.partner_id = None
        self.pair_list = pair_list
        self.email = email

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    # The str function below will take the class object of Users and 
    # make it print the info we want for the list
    def __str__(self):
        return f"{self.f_name} {self.l_name} is user {self.id}. Their email is {self.email} and they can be matched with users {self.pair_list}"

    # Used to connect users if they are partners
    # TO DO: Add logic to change status for partner since it will not be automatically set
    def add_partner(self):
        partner_change = input('Does this user have a partner?: ')
        # Add an error handling check here 
        if partner_change.lower() == 'y':
            which_user = int(input('Which user is their partner?: '))
            self.partner_id = which_user   
        else:
            self.partner_id = -1

        return f"User's partner is now {self.partner_id}"

    # This function will populate the user's pair_list with all the ids of the users created  
    def build_user_list(self, user_list):
        self.pair_list.append(user_list)
        
    # This function will check if the person has a partner and
    # move them out of the potential pair list
    # Use the remove() function on the list
    def check_for_partner(self):
        if self.has_partner == True:
            if self.partner_id in self.pair_list:
                self.pair_list.remove(self.partner_id)
            else:
                pass
        
        return self.pair_list

    # This function should check the self.pair_list to see if there are any options to pair
    # If there are it should randomly pick a match
    # Once that pair is made, check to see if any other user is paired with that person
        # if so, pick again
    # Return pair as a string (this would get changed to keep all pairing secret...unless you don't want that)
    def create_pairs(self, user):
        pass

    def next_thing(self, user):
        pass

    def next_step(self):
        pass

# user1 = Users(1, 'Lee', 'Arnold', False)
# user2 = Users(2, 'Tait', 'Loughridge', True)
# print(user1,'\n',user2)

# print(user2.add_partner())