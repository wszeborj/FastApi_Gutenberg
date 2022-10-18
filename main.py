from fastapi import FastAPI, Request
from scraper import Scrape
from text_statistic import TextStat

app = FastAPI()
scrape = Scrape()


def download_data(full_path):
    text_data = scrape.download_book(full_path)
    return text_data

#zad1.2
@app.get("/{full_path:path}/all_words")
def main_path(full_path: str):
    text_data = download_data(full_path)
    text_stat = TextStat(text_data)
    return text_stat.counted_words

#zad1.1 & zad1.1.1
@app.get("/{full_path:path}/word/{word}")
def path_word(full_path: str, word: str):
    text_data = download_data(full_path)
    text_stat = TextStat(text_data)
    return text_stat.find_word(word)

#zad1.3
@app.get("/{full_path:path}/most_common/{how_much}")
def most_common(full_path: str, how_much: int):
    text_data = download_data(full_path)
    text_stat = TextStat(text_data)
    return text_stat.most_common(how_much)

#zad1.4
@app.get("/{full_path:path}/least_common/{how_much}")
def least_common(full_path: str, how_much: int):
    text_data = download_data(full_path)
    text_stat = TextStat(text_data)
    return text_stat.least_common(how_much)

#zad1.4
@app.get("/{full_path:path}/sentences")
def sentences(full_path: str,):
    text_data = download_data(full_path)
    text_stat = TextStat(text_data)
    return text_stat.sentences()
