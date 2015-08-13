from flask import Flask
from flask.ext.mail import Mail
from flask.ext.mail import Message
from flask import request

app = Flask(__name__)

mail = Mail(app)

app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_SSL=False,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='xxx@gmail.com',
    MAIL_PASSWORD='xxx')

mail = Mail(app)

@app.route("/sendmail/")
def sendmail():

    ip = str(request.environ['REMOTE_ADDR'])
    user_agent = str(request.headers.get('User-Agent'))
    msg = Message("mrb",
                  sender="xxx@gmail.com",
                  recipients=["xxx@gmail.com"])
    msg.body = 'IP:  ' + ip + '\n\n' + 'User-Agent:  ' + user_agent
    mail.send(msg)
    return "Your header information is sent to you."

@app.route("/")
def index():
    return str(request.access_route)

if __name__ == "__main__":
    app.run()