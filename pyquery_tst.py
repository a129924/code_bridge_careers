from typing import Any, Callable
from pyquery import PyQuery as pq


def get_html_string_from_file(path: str) -> str:
    with open(path, "r+", encoding="UTF-8") as fr:
        return fr.read()


def parser_html(
    html_string: str,
    select_element: str,
    func: Callable[[pq], Any],
):
    # <article class="b-block--top-bord job-list-item b-clearfix js-job-item "
    # b-list-inline__ad-icon
    doc = pq(html_string)
    items = doc(select_element)

    for article in items.items("li:not([class]) a[href]"):
        # print(article.attr("href"))
        print(func(article))


parser_html(
    get_html_string_from_file("./104.html"),
    'article[class="b-block--top-bord job-list-item b-clearfix js-job-item "]\
            ',
    lambda item: item.attr("href"),
)
