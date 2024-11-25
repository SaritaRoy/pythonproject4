import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, subject, message, password):
    try:
        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        print("Email sent successfully!")
        server.quit()
    except Exception as e:
        print(f"Error: {e}")

# Input details
sender = input("Enter your email: ")
password = input("Enter your email password: ")
receiver = input("Enter recipient email: ")
subject = input("Enter subject: ")
message = input("Enter message: ")

send_email(sender, receiver, subject, message, password)
