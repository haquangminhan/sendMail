from celery import Celery
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'somebodyemail@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

celeryApp = Celery('tasks', broker='amqp://localhost')

@celeryApp.task
def send():
    msg = Message("Hello", sender = "somebodyemail@gmail.com", 
                            recipients=["someoneelse@gmail.com"])
    msg.body = "Hello! Everyone!!!!!!!!"
    with app.app_context():
        mail.send(msg)
    return "sent!!!!!!!!"

# @celeryApp.task
# def add():
#     return "a"

@app.route("/sendmail")
def sendM():
    send.delay()
    # add.delay()
    return 'abc'

if __name__ == '__main__':
    app.run(debug=True)