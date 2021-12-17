import requests
from bs4 import BeautifulSoup
import datetime

from email_provider import send_email


def get_current_date() -> str:
    """Returns the current date in DD-MM-YYYY format"""

    now = datetime.datetime.now()

    day = str(now.day)
    month = str(now.month)
    year = str(now.year)

    return f"{day}-{month}-{year}"


def extract_soup(url: str) -> BeautifulSoup:
    """returns the soup of the ``url``"""

    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")

    return soup


def format_football365_soup() -> str:
    """returns the formatted html of the football365 site"""

    content = "<h2>FOOTBALL365</h2>"

    soup = extract_soup("https://football365.com")

    for i, tag in enumerate(soup.find_all("li", attrs={"class": "hero__item"})):
        link = tag.find("a")

        text = link.get_text(" | ", strip=True)
        text = text.split(" | ")
        text = text[:-1]
        text = " | ".join(text)

        href = link["href"]
        newLink = f'<a href="{href}">{text}</a>'

        content += f"{(str(i + 1))} :: {newLink}\n<br/>"

    return content


#  print("Extracting news from " + url)
# print("==========================")

#  newContent = ""
#  newContent += "<b>HN Top Stories:</b>\n<br>" + "-" * 50 + "<br>"


# newContent = extract_soup("https://news.ycombinator.com")

# content += newContent
# content += "<br>----------<br>"
# content += "<br><br>End of Message"

# format_football365_soup()
content = format_football365_soup()

# print(content)

# string = "eyes | on | my"
# sl = string.split(" | ")
# sl = sl[:-1]
# sl = " | ".join(sl)
# print(sl)

recipients = ["abdulrafiua10@gmail.com"]
subject = f"Football News {get_current_date()}"

send_email(content, subject, recipients)
