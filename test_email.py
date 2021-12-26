import smtplib, ssl
import os

port = 465
password = 'mlhwdtmjcvzmugof'

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("taltalmailing@gmail.com", password)
    server.sendmail('taltalmailing@gmail.com', 'jjj1305@hanmail.net', "Hi")
    server.sendmail('taltalmailing@gmail.com', 'kjhwnsghksk@naver.com', "Hi")
