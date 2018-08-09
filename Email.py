from Driver import Driver
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email(Driver):
    device_name = "email_smtp_client"
    def send(self, data):
        #Data in form ["address","title","content"]
        fr = "naclcaleb@gmail.com"
        to = data[0]
        msg = MIMEMultipart()
        msg["From"] = fr
        msg["To"] = to
        msg["Subject"] = data[1]

        body = data[2]

        msg.attach(MIMEText(body,'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("naclcaleb@gmail.com","cybersecurity7")
        text = msg.as_string()
        server.sendmail(fr,to,text)
