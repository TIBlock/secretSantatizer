# this model will manage the participants in our user's lists.

from db import db

class ParticipantModel(db.Model):
    __tablename__ = 'participants'

    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')
    list_name = db.Column(db.String(80))
    paticipants = db.Column(db.String)

def __init__(self,  creator_id, list_name, paticipants):
    self.creator_id = creator_id
    self.list_name = list_name
    self.paticipants = paticipants

def save_to_db(self):
    db.session.add(self)
    db.session.commit()

def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()

def json(self):
    return {
        'id': self.id,
        'creator_id': self.creator_id,
        'list_name': self.list_name,
        'paticipants': self.paticipants,
    }
