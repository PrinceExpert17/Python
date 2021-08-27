import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Use environment variables to secure this password
username = 'thutmose2021@gmail.com'
password = 'kis20danc!'

def send_email(text='Email Body', subject='Hello Python',
 from_email='ThutMose <thutmose2021@gmail.com>', to_email=None, html=None):
    assert isinstance(to_email, list) #list helps to get a list of emails if there are multiple people to send to
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ','.join(to_email)
    msg['Subject'] = subject

    txt = MIMEText(text, 'plain')
    msg.attach(txt)
    if html != None:
        html = MIMEText(html, 'html')
        msg.attach(html)
    msg_str = msg.as_string()
    #Now login to smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_email, msg_str)

    server.quit()
    #with smtplib.SMTP() as server:
    #    pass





    