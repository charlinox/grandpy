#!/usr/bin/python3
# coding: utf-8

from parser import Parser


def main():
    """  Start  """
    text = "salut, comment vas-tu? pourrais-tu par hasard m'indiquer quelle est l'adresse de la tour eiffel, s'il te plait ?"
    parser = Parser(text)
    parsed_question = parser.start()


if __name__ == "__main__":
    main()
