import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# SMTP server settings (e.g., Gmail)
SMTP_SERVER = "server"
SMTP_PORT = port  # TLS port (use 465 for SSL)

# Sender credentials (use an App Password if required)
EMAIL_SENDER = "login"
EMAIL_PASSWORD = "password"

# Email settings
EMAIL_RECIPIENT = "login"
EMAIL_SUBJECT = "Quick Email Sending Test"
EMAIL_BODY = "Hello, this is an email sent using Python and smtplib!"

# Create the email message
msg = MIMEMultipart()
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECIPIENT
msg["Subject"] = EMAIL_SUBJECT
msg.attach(MIMEText(EMAIL_BODY, "plain"))

try:
    # Connect to the SMTP server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Enable TLS encryption
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)  # Log in to the server
    server.sendmail(
        EMAIL_SENDER,
        EMAIL_RECIPIENT,
        msg.as_string()
    )  # Send the email
    server.quit()  # Close the connection

    print("Email sent successfully!")

except Exception as e:
    print(f"Error sending the email: {e}")
