#!/usr/bin/python3
# coding: utf-8

import unicodedata
import re

class Parser:

    def __init__(self, text):
        """Initializes the parser."""
        self.text = text

    def remove_accents(self):
        self.text = ''.join(
            c for c in unicodedata.normalize('NFD', self.text)
            if unicodedata.category(c) != 'Mn'
            )
        return self

    def parser_text(self):
        self.text = re.search(
            r"(ou se trouve|ou se situe|ou est|quelle est l'adresse de|aller|aller a|aller au| aller aux)\s+([^,.?!]+)",
            self.text
            ).group(2)
        return self

    def remove_capitals(self):
        self.text = self.text.lower()
        return self

    def start(self):
        """  Start  """
        text_without_accent = self.remove_accents(self.text)
        self.parser_text(text_without_accent)