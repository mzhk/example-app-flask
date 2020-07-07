from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes
from resources.movie_v1 import movies_v1

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/flask-example-app'
}
initialize_db(app)

app.register_blueprint(movies_v1) # using blueprint
initialize_routes(api) # using flask_restful

app.run()
