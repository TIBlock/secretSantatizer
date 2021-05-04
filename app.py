from flask import Flask
from flask_restful import Api
# from flask_jwt_extended import JWTManager

from db import db

# complete revamp of codebase starts here


app = Flask(__name__)   



if __name__ == '__main__':
    app.run(port=5000, debug=True)