

class BoolQuery(object):

    def __init__(self):
        self._query = dict()
        """
        occur type : must, filter, should, must_not
        """
        self._query["bool"] = dict()
        self._query["bool"]["filter"] = []
        self._query["bool"]["must"] = []
        self._query["bool"]["should"] = []
        self._query["bool"]["must_not"] = []
    
    def filter(self, queries):
        self._query["bool"]["filter"].extend(queries)
        return self

    def should(self, *queries):

        self._query["bool"]["should"].extend(queries)
        return self
    
    def must(self, *queries):

        self._query["bool"]["must"].extend(queries)
        return self
    
    def must_not(self, queries):

        self._query["bool"]["must_not"].extend(queries)
        return self

    def build(self):
        return self._query




def boosting(self):
    pass

def constant_score(self):
    pass

def dis_max(self):
    pass

def function_score(self, functions:list()):
    pass

def indices(self):
    pass

def limit(self):
    pass