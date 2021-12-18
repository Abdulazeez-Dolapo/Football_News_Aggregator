from email_provider import send_email
from helpers import get_current_date
from football_365 import fetch_football365_articles


content = fetch_football365_articles()
recipients = ["abdulrafiua10@gmail.com"]
subject = f"Football gist for {get_current_date()}"

send_email(content, subject, recipients)
