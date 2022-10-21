import smtplib
from email.mime.text import \
    MIMEText  # use from email.message import Message so that you can set content,add attachement.
from decouple import config
from . import receipt_factory as factory


def send(order, customer_email):
    """Sends the receipt to the customer"""
    receipt = factory.prepare_receipt_email(order)
    subject = "Receipt for Order#{id}".format(id=order.order_id)
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    EMAIL = config('EMAIL')
    PASSWORD = config('PASSWORD')
    print(EMAIL, PASSWORD)
    server.login(EMAIL, PASSWORD)

    message = MIMEText(receipt, 'html')
    message["From"] = EMAIL
    message["To"] = customer_email
    message["Subject"] = subject

    server.sendmail(EMAIL, customer_email, message.as_string())
