import smtplib
import ssl
from email.utils import formataddr
from email.message import EmailMessage

# Server, sender and receiver information
smtp_server = "smtp.gmail.com"
port = 587 # For starttls
sender_email = "developmentkerem@gmail.com"
sender_password = input(f"Enter your password for {sender_email}:")
receiver_email = "kerem_boyali@hotmail.com"
context = ssl.create_default_context() # Create a secure SSL context


# Construct the message object
msg = EmailMessage()
msg['From'] = formataddr(('Example Sender Name', sender_email))
msg['To'] = formataddr((receiver_email, receiver_email))
msg.set_content('Lorem ipsum')

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls(context=context) # Secure the connection
    server.login(sender_email, sender_password)
    server.send_message(msg) # Send e-mail
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()