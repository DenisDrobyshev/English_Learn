import pymorphy2
import translate
import operator


def dict_to_file(name: str, dict_words: dict) -> None:
    en = translate.Translator(from_lang='ru', to_lang='en')
    with open(name, mode='w') as f:
        for word in dict_words:
            f.write(f'{word} | {en.translate(word)} | {dict_words[word]}\n')


def english_book(name: str, book: str) -> None:
    with open(name, mode='r') as f:
        lst = f.read().split()
        dict_to_file(book, sorted_dict(normalize_word_list(lst)))


def normalize_word_list(words_list: list) -> list:
    for i in range(0, len(words_list)):
        lst = [j for j in words_list[i] if j.isalpha()]
        word = "".join(lst)
        words_list[i] = normal_form(word)
    return words_list


def sorted_dict(words: list) -> dict:
    slovar = {}
    for word in words:
        slovar[word] = str(words.count(word))
    if '' in slovar:
        slovar.pop('')
    return dict(sorted(slovar.items(), key=operator.itemgetter(1), reverse=True))


def normal_form(word: str) -> str:
    morph = pymorphy2.MorphAnalyzer()
    return morph.parse(word)[0].normal_form


english_book("input.txt", "output.txt")
