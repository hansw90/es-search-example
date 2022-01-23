class BoolQuery(object):
    """
        must : 해당 절에 모든 query가 true 가 되어야 document로 간주한다.
        must_not : 해당 절에 지정된 모든 query 결과가 false가 되어야 일치 document로 간주한다.
        should : 해당 절에 지정된 query가 많이 일치할 수록 Relevance Score를 높혀 검색 순위를 높힌다.
        filter : 해당 절에 지정된 모든 query가 true가 되어야 일치 document 로 간주한다. 단, 이절은 relevance score 계산에 포함되지 않는 filter type context이다.
        """

    def __init__(self):
        self._query = dict()
        self._query["bool"] = dict()
        self._query["bool"]["filter"] = []
        self._query["bool"]["must"] = []
        self._query["bool"]["should"] = []
        self._query["bool"]["must_not"] = []
        self._query["bool"]["minimum_should_match"] = 1
        self._query["bool"]["boost"] = 1.0
    
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

    def minimum_should_match(self, values):
        self._query["bool"]["minimum_should_match"] = values
        return self
    
    def boost(self, values):
        self._query["bool"]["boost"] = values
        return self

    def build(self):
        return self._query