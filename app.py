import os
from security import authenticate, identity
from flask_jwt import JWT
from flask_restful import Api, Resource
from flask import Flask
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'abc123'

api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

# this code only runs when we directly run the application from terminal
# it won't run in heroku as uwsgi loads the app itself, not the file
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

# this is some new code
