from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST

from resources.users import UserRegister, User, UserLogin, UserLogout, TokenRefresh

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.secret_key = 'taylor'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWTManager(app)

@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1: #Instead of hard-coding, you should read from a config file or a database.
        return {'is_admin': True}
    return {'is_admin': False}
    
@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(self, decrypted_token):
    return decrypted_token['jti'] in BLOCKLIST

@jwt.expired_token_loader
def expired_token_callback(self, error):
    return jsonify({
        'description': 'The token has expired.',
        'error': 'token_expired'
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'desription': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(self, error):
    return jsonify({
        'desription': 'Request does not contain an access token.',
        'error': 'authorization_required'
    }), 401


@jwt.needs_fresh_token_loader
def token_not_fresh_callback(self, error):
    return jsonify({
        'desription': 'The token is not fresh.',
        'error': 'fresh_token_required'
    }), 401


@jwt.revoked_token_loader
def revoked_token_callback(self, error):
    return jsonify({
        'desription': 'The token has been revoked.',
        'error': 'token_revoked'
    }), 401


api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(TokenRefresh, '/refresh')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)  # important to mention debug=True