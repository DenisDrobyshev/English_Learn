import pymorphy2
import translate

book = {}


morph = pymorphy2.MorphAnalyzer()
en_translate = translate.Translator(from_lang='ru', to_lang='en')


def english_book(name: str):
    with open(name, encoding='utf-8') as file:
        lst = file.read().split()
