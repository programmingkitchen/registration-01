import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

app = Flask(__name__)

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'membership.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#Migrate(app,db)

''''
NOTE! These imports need to come after you've defined db, otherwise you will
get errors in your models.py files.
NOTE:  1.  Import the blueprints defined in the Views
'''
from registrationapp.main.views import main_blueprint
from registrationapp.registration.views import registration_blueprint


'''
NOTE:  2. Register the blueprints.  This prefix sets the link that is produced.
If the templates have the same name, then the first one registered will be
the one that is found.
https://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
'''
app.register_blueprint(main_blueprint,url_prefix="/")
app.register_blueprint(registration_blueprint,url_prefix="/registration")
