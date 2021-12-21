from email_provider import send_email
from helpers import get_current_date
from bleacher_report_chelsea import fetch_bleacher_report_articles
from football_365 import fetch_football365_articles

content = ""
content += fetch_football365_articles()
content += "<br/>"
content += fetch_bleacher_report_articles()

recipients = ["abdulrafiua10@gmail.com"]
subject = f"Football gist for {get_current_date()}"

send_email(content, subject, recipients)
