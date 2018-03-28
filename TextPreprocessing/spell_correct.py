"""
Reference :
https://github.com/mattalcock/blog/blob/master/2012/12/5/python-spell-checker.rst
"""

import re
import collections


class SpellCorrect:

    def __init__(self,
                 text=None,
                 files=[],
                 initialize=True):
        self.NWORDS = collections.defaultdict(lambda: 1)
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        if initialize:
            self.initialize(text, files)

    def initialize(self, text, files):
        for f in files:
            self.train(self.words(open(f, encoding='utf-8').read()))
        if isinstance(text, str):
            self.train(self.words(text))

    def words(self, text):
        return re.findall('[a-z0-9]+', text.lower())

    def train(self, features):
        for f in features:
            self.NWORDS[f] += 1

    def edits1(self, word):
        s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [a + b[1:] for a, b in s if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b) > 1]
        replaces = [a + c + b[1:] for a, b in s for c in self.alphabet if b]
        inserts = [a + c + b for a, b in s for c in self.alphabet]
        return set(deletes + transposes + replaces + inserts)

    def known_edits2(self, word):
        return set(e2
                   for e1 in self.edits1(word)
                   for e2 in self.edits1(e1)
                   if e2 in self.NWORDS)

    def known(self, words):
        return set(w for w in words
                   if w in self.NWORDS)

    def correct(self, word):
        candidates = self.known([word]) or\
            self.known(self.edits1(word)) or\
            self.known_edits2(word) or\
            [word]
        return max(candidates, key=self.NWORDS.get)

    def sentence_correct(self, sentence, joined=True, ignore_case=True):
        if ignore_case:
            sentence = sentence.lower()
        if joined:
            sentence = sentence.split()
        sent = [word.lower()
                if word.isupper()
                else self.correct(word.lower())
                for word in sentence]
        return " ".join(sent)
