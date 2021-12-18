import requests
from bs4 import BeautifulSoup
import datetime

from email_provider import send_email


def get_current_date() -> str:
    """Returns the current date in DD-MM-YYYY format"""

    try:
        now = datetime.datetime.now()

        day = str(now.day)
        month = str(now.month)
        year = str(now.year)

        return f"{day}-{month}-{year}"
    except Exception as err:
        print("Error getting the date 😢😭", err)


def extract_soup(url: str) -> BeautifulSoup:
    """returns the soup of the ``url``"""

    try:
        response = requests.get(url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")

        return soup
    except Exception as err:
        print("Error extracting soup 😢😭", err)


def format_football365_article_list(article_list: list, start_count: int = 1) -> str:
    """
    Format the F365 list of articles into a stringified list of links in the format
    ``serial_number``:: ``article_type`` | ``headline``
    """

    try:
        content = ""
        headlines = {}

        for i, tag in enumerate(article_list):
            link = tag.find("a")

            text = link.get_text(" | ", strip=True)
            text_list = text.split(" | ")
            headline = text_list[1] if len(text_list) == 3 else text_list[0]
            text_to_use = " | ".join(text_list[:-1])

            href = link["href"]
            newLink = f'<a href="{href}">{text_to_use}</a>'
            count = i + start_count

            # This is required to remove duplicate links
            if headline in headlines:
                continue
            else:
                headlines[headline] = count
                content += f"{(str(count))} :: {newLink}\n<br/>"

        return content
    except Exception as err:
        print("Error formatting article list 😢😭", err)


def fetch_football365_articles() -> str:
    """returns the formatted html of the football365 site"""

    try:
        content = "<h2>FOOTBALL365</h2>"

        soup = extract_soup("https://football365.com")
        articles = soup.find_all("li", ["hero__item", "articleList__item"])
        content += format_football365_article_list(articles)

        return content
    except Exception as err:
        print("Error fetching football365 articles 😢😭", err)


content = fetch_football365_articles()
recipients = ["abdulrafiua10@gmail.com"]
subject = f"Football gist for {get_current_date()}"

send_email(content, subject, recipients)
