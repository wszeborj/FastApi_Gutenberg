# import sys
# import os
# from requests import get
#
#
#
# class Scrape():
#     def __init__(self):
#         pass
#
#     def download_book(self, idbook):
#         url = rf'https://www.gutenberg.org/files/{idbook}/{idbook}-0.txt'
#         try:
#             r = get(url)
#         except Exception as exc:
#             print(f'There was a problem: {exc}')
#             sys.exit(0)
#         return r.content
#
#
# if __name__ == '__main__':
#     scrape = Scrape()
#     print(scrape.download_book('2701'))

import sys
import os
from requests import get
from bs4 import BeautifulSoup


class Scrape():
    def __init__(self):
        pass

    def download_book(self, url):
        try:
            r = get(url)
        except Exception as exc:
            print(f'There was a problem: {exc}')
            sys.exit(0)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.get_text(strip=True)


if __name__ == '__main__':
    scrape = Scrape()
    url = r'https://www.gutenberg.org/files/2701/2701-0.txt'
    print(scrape.download_book(url))

