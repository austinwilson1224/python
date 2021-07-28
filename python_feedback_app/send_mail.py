import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '89fe5182954cc9'
    password = '2ad67345b9ef9e'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
    sender_email = 'email@example.com'
    reciever_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = reciever_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())