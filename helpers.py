import requests
from bs4 import BeautifulSoup
import datetime


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
        raise


def extract_soup(url: str) -> BeautifulSoup:
    """returns the soup of the ``url``"""

    try:
        response = requests.get(url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")

        return soup
    except Exception as err:
        print("Error extracting soup 😢😭", err)
        raise
