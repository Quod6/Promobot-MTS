from flask import Flask
from config import configuration
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
import smtpd

UPLOAD_FOLDER = '/static/images'




# create our little application
app = Flask(__name__)
#app.config.from_object(configuration)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'leksus.fm@gmail.com',
	MAIL_PASSWORD = '1Adminsaitalyoshinru'
	)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mail = Mail(app)


s = URLSafeTimedSerializer('This is a secret!')


