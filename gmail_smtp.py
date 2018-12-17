from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import account

def send_gmail_smtp(mail_sender, password, mail_receiver, subject, content=None, file_name=None, smtp_url=account.SMTP_URL, smtp_port=account.SMTP_PORT):
    msg = MIMEMultipart()
    msg['From'] = mail_sender
    msg['To'] = mail_receiver
    msg['Subject'] = subject
    file_name = file_name
    content = content
    
    if content:
        msg.attach(MIMEText((content), 'html'))
    
    if file_name:
        attachment = open(file_name, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('content-dispostion', 'attachment', filename=file_name)
        msg.attach(part)

    try:
        server = smtplib.SMTP(smtp_url, smtp_port)
        server.starttls()
        server.login(mail_sender, password)
        server.sendmail(mail_sender, mail_receiver, msg.as_string)
        server.quit()
    
    except Exception as e:
        print(str(e))
        
        