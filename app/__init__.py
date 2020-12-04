from flask import Flask
from Flask_SQLAlchemy import SQLAlchemy


app = Flask(__name__)

boostrap = Boostrap 


db = SQLALchemy


def create_app(config_name):
    app = Flask(__name__)

    # ....

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
