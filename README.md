# Тестовый проект для университета 

# Скрипт обработки текста 

## Описание

Этот скрипт предназначен для обработки текстовых файлов, преобразуя их содержимое в английский язык и создавая словарь частотности слов. Скрипт использует библиотеки `pymorphy2` для нормализации слов и `translate` для перевода слов с русского на английский язык.

## Функции

### `dict_to_file(name: str, dict_words: dict) -> None`

- **Описание:** Функция записывает словарь слов и их переводы на английский язык в файл.
- **Параметры:**
 - `name`: Имя файла для записи.
 - `dict_words`: Словарь, где ключи - слова, а значения - их переводы на английский язык.

### `english_book(name: str, book: str) -> None`

- **Описание:** Читает текстовый файл, нормализует и переводит слова, а затем создает словарь частотности слов и записывает его в новый файл.
- **Параметры:**
 - `name`: Имя файла для чтения.
 - `book`: Имя файла для записи.

### `normalize_word_list(words_list: list) -> list`

- **Описание:** Нормализует список слов, удаляя не буквенные символы и приводя слова к их нормальной форме.
- **Параметры:**
 - `words_list`: Список слов для нормализации.

### `sorted_dict(words: list) -> dict`

- **Описание:** Создает словарь частотности слов из списка слов.
- **Параметры:**
 - `words`: Список слов для подсчета частотности.

### `normal_form(word: str) -> str`

- **Описание:** Возвращает нормальную форму слова.
- **Параметры:**
 - `word`: Слово для нормализации.

## Пример использования
python english_book("input.txt", "output.txt")
- Этот код читает текст из файла `input.txt`, нормализует и переводит слова, создает словарь частотности слов и записывает его в файл `output.txt`.


