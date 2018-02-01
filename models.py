import re

import requests
from bs4 import BeautifulSoup


class KeywordsCounter:
    """
    KeywordsCounter class used for count the occurrence on the page of each keyword of the given page
    """
    def __init__(self, url):
        """
        Create instance of KeywordsCounter
        :param url: site url tu parsing:
        """
        if url is None:
            self.url = 'http://zsp1.pila.pl'
        self.url = url
        site = requests.get(self.url)
        self.parsed_site = BeautifulSoup(site.text, 'html.parser')
        self.keywords = None

    def get_keywords(self):
        """
        Find meta tag with word keywords on site. Not important case of word 'keywords'
        :return: list of unique keywords
        """
        keywords_string = self.parsed_site.find("meta", attrs={"name": re.compile("^Keywords$", re.I)}).get('content')
        keywords_string = keywords_string.split(',')
        self.keywords = list(set(keywords_string))

    def count_keywords(self):
        """
        Count the occurrence of each keyword.
        :return: dictionaries, where key is keyword and value is number of occurrences
        """
        result = dict()
        for word in self.keywords:
            element = (self.parsed_site.findAll(text=re.compile(word, re.IGNORECASE)))
            result[word] = sum([x.count(word) for x in element])
        return result
