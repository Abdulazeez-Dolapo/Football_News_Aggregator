from helpers import extract_soup


def format_bleacher_report_article_list(
    article_list: list, start_count: int = 1
) -> str:
    """
    Format the F365 list of articles into a stringified list of links in the format
    ``serial_number``:: ``headline``
    """

    try:
        content = ""

        for i, tag in enumerate(article_list):
            href = tag.find("a")["href"]
            text = tag.find("h3").get_text("", strip=True)

            newLink = f'<a href="{href}">{text}</a>'
            count = i + start_count

            content += f"{(str(count))} :: {newLink}\n<br/>"

        return content
    except Exception as err:
        print("Error formatting BR article list 😢😭", err)
        raise


def fetch_bleacher_report_articles() -> str:
    """returns the formatted html of the Bleacher Report site"""

    try:
        content = "<h2>BLEACHER REPORT CHELSEA</h2>"

        soup = extract_soup("https://bleacherreport.com/chelsea")

        # There are lots of embedded twitter cards and I don't know how to extract the text and links from them at the moment.
        # NOTE: handle embedded tweets

        articles = soup.find_all("li", ["articleSummary"])
        content += format_bleacher_report_article_list(articles)

        return content
    except Exception as err:
        print("Error fetching Bleacher Report articles 😢😭", err)
        raise
