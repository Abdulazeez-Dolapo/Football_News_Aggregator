from helpers import extract_soup


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
        raise


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
        raise
