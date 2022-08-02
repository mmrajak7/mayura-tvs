import os
from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://u106031583_Rajak12345:Rajak12345@sql222.main-hosting.eu:3306/u106031583_mayura'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 30
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 60
app.config['SQLALCHEMY_POOL_RECYCLE'] = 50
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0
app.config['SQLALCHEMY_POOL_PRE_PING'] = True

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 30,
    'pool_recycle': 50,
    'pool_timeout': 60,
    'max_overflow': 0
}
app.config['SECRET_KEY'] = '0c57258251118bbb97c1e20f'
app.config['UPLOAD_EXTENSIONS'] = ['.xlsx']
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_PATH'] = os.path.join(basedir, "static/uploads/")
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from booking.booking import booking
from customer.customer import customer
from invoice.invoice import invoice
from vehicle.vehicle import vehicle
from login.loginRoute import login
from stocks.stocks import stocks
from misc.misc import misc

app.register_blueprint(booking, url_prefix="/api/v1/booking")
app.register_blueprint(customer, url_prefix="/api/v1/customer")
app.register_blueprint(invoice, url_prefix="/api/v1/invoice")
app.register_blueprint(vehicle, url_prefix="/api/v1/vehicle")
app.register_blueprint(stocks, url_prefix="/api/v1/stocks")
app.register_blueprint(misc, url_prefix="/api/v1/misc")
app.register_blueprint(login)
login_manager.login_view = "login.login_page"
login_manager.login_message_category = "info"


@app.route('/')
def hello_world():
    return redirect(url_for("login.login_page"))


@app.errorhandler(404)
def not_found(e):
    print(e)
    return render_template("404.html")


@app.errorhandler(500)
def server_error(e):
    print(e)
    print(request.url)
    return render_template("500.html")


@app.errorhandler(403)
def forbidden_error(e):
    print(e)
    return render_template("403.html")


@app.errorhandler(413)
def too_large(e):
    return render_template("413.html", messaage=e)


@app.template_filter()
def pretty_boolean(value):
    if value:
        return True
    return False


if __name__ == '__main__':
    app.run()
