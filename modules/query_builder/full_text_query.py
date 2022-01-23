from dataclasses import field
from quries import match, multi_match, match_boolean_prefix, match_phrase, match_phrase_prefix

class FullTextQuery(object):

    query = dict()

    def __init__(self):
        self.query = dict()

    def match(self, field, value):
        return match.Match(field=field, value=value)
    
    def multi_match(self, fields:list(), value):
        return multi_match.MultiMatch(fields, value)

    def match_boolean_prefix(self, field, value):
        return match_boolean_prefix.MatchBooleanPrefix(field=field, value=value)

    def match_phrase(self, field, value):
        return match_phrase.MatchPhrase(field=field, value=value)

    def match_phrase_prefix(self, field, value):
        return match_phrase_prefix.MatchPhrasePrefix(field=field, value=value)


    