from flask import Flask, url_for, jsonify
from flask import render_template, request,request, redirect
from sqlalchemy import Table, Column, Integer, String, MetaData
#   login import LoginManager, UserMixin, login_user
#rom mail import Mail, Message
from email.message import EmailMessage
from email.mime.text import MIMEText
import smtplib


app = Flask(__name__)

'''app.config['MAIL_SERVER'] = 'amtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'y.652925489@gmail.com'
app.config['MAIL_PASSSWOORD'] = 'fkxa bauj fulc xthh'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app) '''


@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route("/send_email", methods=['POST'])
def send_mail():
    if request.method == "POST":
        from_email = 'y.6529254@gmail.com'
        to_email = 'y.652925489@gmail.com'
        account = 'y.6529254@gmail.com'
        password = 'password'


        subject = 'テスト送信'

        name =  request.form.get('name')
        mail = request.form.get('email')
        detail = request.form.get('detail')
        bodytext = "名前：" + name + "\n" + "メール：" + mail + "\n" + "詳細：" + detail

        s = smtplib.SMTP('smtp.gmail.com',465)
        s.starttls()
        s.login('y.652925489@gmail.com' , 'yjqehopefglwodeb')
        msg = MIMEText(bodytext)
        msg['subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        s.send_messade(msg)
        s.close()
        return render_template('send.html', success=True)
    return render_template("index.html")  



if __name__ == ('__main__'):
    app.run(debug=True, host='0.0.0.0', port=5000)