from quries import exist, fuzzy, prefix, range, term, terms, terms_set, wildcard

class TermQuery(object):

    def __init__(self):
        self.query = dict()
    

    def term(self):
        return term.Term()

    def terms(self):
        return terms.Terms()

    def terms_set(self):
        return terms_set.TermsSet()

    def range(self):
        return range.Range()

    def exist(self):
        return exist.Exist()
        
    def prefix(self):
        return prefix.Prefix()

    def wildcard(self):
        return wildcard.WildCard()
    
    def fuzzy(self):
        return fuzzy.Fuzzy()
        