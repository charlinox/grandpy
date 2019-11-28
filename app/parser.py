#!/usr/bin/python3
# coding: utf-8

import unicodedata
import re


class Parser:
    """ Normalize and parse the question to extract the place """

    def __init__(self, text):
        """Initializes the parser."""
        self.text = text

    def remove_accents(self):
        """ Remove the accents """
        self.text = ''.join(
            c for c in unicodedata.normalize('NFD', self.text)
            if unicodedata.category(c) != 'Mn'
        )
        return self

    def remove_capitals(self):
        """ Remove capitals """
        self.text = self.text.lower()
        return self

    def parser_text(self):
        """ Extract the place by parsing the question """
        match = re.search(
            r"(ou se trouve|ou se situe|ou est|l'adresse de| l'adresse d'|aller\
            |aller a|aller au|aller aux|direction de\
            |l'endroit nommé)\s+([^,.?!]+)",
            self.text)
        if match:
            self.text = match.group(2)
        return self

    def start(self):
        """  Start  """
        self.remove_accents()
        self.remove_capitals()
        self.parser_text()
        return self.text
