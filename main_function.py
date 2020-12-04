import smtplib
import ssl
from email.utils import formataddr
from email.message import EmailMessage

# Server, sender and receiver information
smtp_server = "smtp.gmail.com"
port = 587 # For starttls
context = ssl.create_default_context() # Create a secure SSL context
sender_email = "developmentkerem@gmail.com"
sender_name = "Her gün 1 kelime"
sender_password = input(f"Enter your password for {sender_email}:")
receiver_email = "kerem_boyali@hotmail.com"
receiver_name = receiver_email

# Construct the message object
msg = EmailMessage()
msg['From'] = formataddr((sender_name, sender_email))
msg['To'] = formataddr((receiver_name, receiver_email))
msg['Subject'] = "Bugünün kelimesi: Deneme"
msg.set_content("Lorem ipsum")

# Try to log in to server and send email
try:
    s = smtplib.SMTP(smtp_server, port)
    s.starttls(context=context) # Secure the connection
    s.login(sender_email, sender_password)
    s.send_message(msg) # Send e-mail
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    s.quit()