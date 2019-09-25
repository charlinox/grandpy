#!/usr/bin/python3
# coding: utf-8

from parser import Parser


def main():
    """  Start  """
    text = "salut, comment vas-tu? pourrais-tu par hasard m'indiquer quelle est l'adresse de la tour eiffel, s'il te plait ?"
    parser = Parser()
    parser.start(text)


if __name__ == "__main__":
    main()
