## RASSuvi Scrapper

```Python
from app import Scrapper

paths = {"Title": "//title/text()", "Heading": "//h3/a/text()"}
url = "http://books.toscrape.com/"

s = Scrapper(method="GET", url=url, paths=paths)

for d in s.extract():
    print(d)