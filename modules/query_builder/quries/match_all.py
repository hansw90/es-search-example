from typing_extensions import Self


_match_all = 'match_all'
_boost = 'boost'
class MatchAll(object):

    def __init__(self):
        self.query = dict()
        self.query[_match_all] = dict()

    def boost(self, boost=1):
        self.query[_match_all][_boost] = boost
        return self

    def build(self):
        return self.query

    