#!/usr/bin/python3
# coding: utf-8

from random import choice
from flask import jsonify

from .parser import Parser
from .api import GoogleMapsDownloader, WikiDownloader


def main(question):
    """  Take a question and return data about a place  """

    parser = Parser(question)
    parsed_question = parser.start()
    downloader = GoogleMapsDownloader()
    data_localisation = downloader.find_place(parsed_question)
    data_wiki = WikiDownloader(data_localisation)
    data_by_coord = data_wiki.fetch_by_coord(data_localisation)
    data_by_title = data_wiki.fetch_by_title(data_by_coord)
    if data_localisation["error"] == True:
        grandpy_answer = [
            "Ah non mon ptit gars. Là je vois pas de quoi tu parles !",
            "Tu sais je suis un sourd. Tu peux répéter en articulant ?",
            "Je ne connais pas. Tu es sur que ce lieu existe ?"
        ]
    else:
        grandpy_answer = [
            "J'ai bien trouvé le lieu que tu cherchais. L'adresse est : ",
            "Ouaip poussin, je connais ! L'adresse, c'est : ",
            "Effectivement mon petit. C'est ici : "
        ]
        grandpy_answer2 = [
            "Et mais je connais ce quartier ! Dans le coin tu as un endroit que je connais bien. J'habitais juste en face ! ",
            "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? ",
            "Je pourrais t'en raconter de belles sur ce coin. Tiens par exemple. "
        ]
    data = {
        "address" : data_localisation["address"],
        "lat" : data_localisation["lat"],
        "lng" : data_localisation["lng"],
        "title" : data_by_coord["title"],
        "pageid" : data_by_coord["pageid"],
        "extract" : data_by_title["extract"],
        "fullurl" : data_by_title["fullurl"],
        "error" : data_localisation["error"],
        "grandpy_answer" : choice(grandpy_answer),
        "grandpy_answer2" : choice(grandpy_answer2)
    }
    return jsonify(data)
