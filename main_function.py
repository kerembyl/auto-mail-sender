import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587 # For starttls
sender_email = "developmentkerem@gmail.com"
password = input(f"Enter your password for {sender_email}:")

receiver_email = "kerem_boyali@hotmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context) # Secure the connection
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message) # Send e-mail
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()