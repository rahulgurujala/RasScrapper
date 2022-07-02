from requests import request, Response
from lxml import html
from typing import Generator
from lxml.html import HtmlElement


class Scrapper:
    def __init__(self, *args, **kwargs) -> None:
        self.args: list = args
        self.kwargs: dict = kwargs
        self.paths: dict = kwargs["paths"]
        self.kwargs.pop("paths")

    def req(self) -> Response:
        return request(*self.args, **self.kwargs)

    def extract(self) -> Generator:
        source: HtmlElement = html.fromstring(self.req().text)
        for key, path in paths.items():
            yield {key: source.xpath(path)}


if __name__ == "__main__":
    paths = {"Title": "//title/text()", "Heading": "//h3/a/text()"}
    url = "http://books.toscrape.com/"

    s = Scrapper(method="GET", url=url, paths=paths)

    for d in s.extract():
        print(d)
