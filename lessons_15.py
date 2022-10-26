# Написать класс Quotes.
# Параметр инициализации - количество цитат (int), и имя файла для сохранения (формат json, параметр по умолчанию)
#
# В классе реализовать метод get_quotes.
# Метод сохраняет список оветов (список словарей) сервиса http://forismatic.com/ru/api/. Если метод не вызван - список пустой.
# Если автор не указан, цитату не брать. Цитаты не должны повторяться (уникальные, без повтора).
#
# В классе реализовать метод print_quotes.
# Метод печатает из списока полученных ответов от сервера только цитату и автора (а не весь словарь). По одной в каждой строке.
#
# Реализовать метод save_quotes.
# Метод сохраняет список оветов (список словарей) в json файл.
# Перед сохранением в json, записи отсортировать по фамилии автора (повторим функцию сортировки).
# Функцию для сортировки в класс засовывать не нужно. Напишите ее отдельно перед классом ))
#
# Не забудьте написать try except для обработки ошибки при получении цитат.
# Там не всегда срабатывает преобразование в json.

import requests
import json
import random


def sort_by_surname(item: dict) -> str:
    surname = item["quoteAuthor"].split()[-1]
    return surname


class Quotes:
    def __init__(self, quotes_count: int, filename: str, file_format: str = "json"):
        self.filename = f"{filename}.{file_format}"
        self.format = file_format
        self.quotes_count = quotes_count
        self._url = "http://www.forismatic.com/api/1.0/"
        self._quotes = []

    @property
    def url(self):
        return self._url

    @property
    def quotes(self):
        return self._quotes

    def get_quotes(self):
        for quote_num in range(self.quotes_count):
            self._quotes += [self.get_quote()]

    def get_quote(self):
        params = {
            "method": "getQuote",
            "format": self.format,
            "key": random.randint(0, 999999),
            "lang": "en"
        }
        response = requests.get(self._url, params=params)
        try:
            if response.json()["quoteAuthor"].strip() == "":
                return self.get_quote()
            else:
                return response.json()
        except json.decoder.JSONDecodeError:
            return self.get_quote()

    def print_quotes(self):
        for quote in self._quotes:
            quote_text = quote["quoteText"].strip()
            quote_author = quote["quoteAuthor"].strip()
            print(f"\"{quote_text}\" - {quote_author}.")

    def save_quotes(self):
        with open(self.filename, "w") as json_file:
            json.dump(sorted(self._quotes, key=sort_by_surname), json_file)


# Usage:
if __name__ == "__main__":
    quotes_count = 100
    filename = "test"
    file_format = "json"
    test = Quotes(quotes_count=quotes_count, filename=filename, file_format=file_format)
    test.get_quotes()
    test.print_quotes()
    test.save_quotes()
