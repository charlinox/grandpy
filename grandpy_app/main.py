#!/usr/bin/python3
# coding: utf-8

from .parser import Parser
from .api import GoogleMapsDownloader, WikiDownloader
from .grand_py_answer import grand_py_answer


def main(question):
    """  Take a question and return data about a place  """

    parser = Parser(question)
    parsed_question = parser.start()
    downloader = GoogleMapsDownloader()
    data_localisation = downloader.find_place(parsed_question)
    data_wiki = WikiDownloader()
    data_by_coord = data_wiki.fetch_by_coord(data_localisation)
    data_by_title = data_wiki.fetch_by_title(data_by_coord)
    grandpy_answer1, grandpy_answer2 = grand_py_answer(
        data_localisation["error"])
    return {
        "address": data_localisation["address"],
        "lat": data_localisation["lat"],
        "lng": data_localisation["lng"],
        "title": data_by_coord["title"],
        "pageid": data_by_coord["pageid"],
        "extract": data_by_title["extract"],
        "fullurl": data_by_title["fullurl"],
        "error": data_localisation["error"],
        "grandpy_answer": grandpy_answer1,
        "grandpy_answer2": grandpy_answer2
    }
