from flask import Flask
from flask_mail import Mail, Message


app = Flask(__name__)


# Not all of the following are required from what I'm seeing
app.config['DEBUG'] = True # This is linked to MAIL_DEBUG - they must match
app.config['TESTING'] = False # This is linked to MAIL_SUPRESS_SEND - they must match
app.config['MAIL_SERVER']='smtp.gmail.com' # Confirm the server set up for G-Mail
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'secretsantatizer@gmail.com'
app.config['MAIL_PASSWORD'] = 'Hohoho2020!'
app.config['MAIL_DEFAULT_SENDER'] = None
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_SUPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

@app.route('/')
def index():
    # Message convention => 
    # msg = Message('Title', sender='', recipients = [''])
    # mail.send(msg)
    msg = Message("Hello", sender = 'secretsantatizer@gmail.com', recipients=['taylorblocker@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return f'Sent'


if __name__ == '__main__':
    app.run(port=5000)