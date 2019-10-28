#!/usr/bin/python3
# coding: utf-8

from grandpy.parser import Parser


def test_remove_accents():
    parser = Parser("éèâ")
    expected_result = "eea"
    assert parser.remove_accents().text == expected_result


def test_parser_text():
    parser = Parser(
        "Salut, comment vas-tu? Pourrais-tu par hasard m'indiquer quelle est l'adresse de la tour eiffel, s'il te plait ?")
    expected_result = "la tour eiffel"
    assert parser.parser_text().text == expected_result


def test_remove_capitals():
    parser = Parser("Salut")
    expected_result = "salut"
    assert parser.remove_capitals().text == expected_result
