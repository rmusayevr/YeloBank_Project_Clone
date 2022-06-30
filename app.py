from flask import Flask

app = Flask(__name__, template_folder='Templates', static_folder="Assets")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:yelobank@127.0.0.1:3307/YeloBankProjectDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True;
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = 'YeloBank'

from extensions import *
from controller import *
from models import *
from form_model import *

if __name__ == "__main__":
    app.init_app(db)
    app.init_app(migrate)
    app.run(port = 5000, debug=True, compare_type = True)
