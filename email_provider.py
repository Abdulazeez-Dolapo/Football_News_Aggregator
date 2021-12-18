import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SERVER = os.environ.get("MAIL_SERVER")
PORT = os.environ.get("PORT")
FROM = os.environ.get("MAIL_FROM")
PASSWORD = os.environ.get("PASSWORD")


def create_server() -> None:
    """Create a server"""

    print("Initializing server")

    server = smtplib.SMTP(SERVER, PORT)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(FROM, PASSWORD)

    print("===========================================================")
    print("Server connected successfully 🎉")
    print("===========================================================")
    return server


def cleanup_server(server) -> None:
    """Clean up the server"""

    server.quit()


def send_email(content: str, subject: str, recipients: str) -> None:
    """Send email to recipients"""

    try:
        server = create_server()

        for recipient in recipients:
            msg = MIMEMultipart()
            msg["From"] = FROM
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.attach(MIMEText(content, "html"))
            server.sendmail(FROM, recipient, msg.as_string())

        print("===========================================================")
        print("Email successfully sent 🎉")
        print("===========================================================")

        cleanup_server(server)
    except Exception as err:
        print("===========================================================")
        print("Error sending email 😢😭", err)
        print("===========================================================")
