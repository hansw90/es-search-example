class BoostingQuery(object):
    """
    긍정적이 쿼리와 일치하는 문서를 반환 하면서, 부정적 쿼리와 일치하는 문서의 Relevance Score 를 줄인다.
    부스팅 쿼리를 사용하면 검색 결과에 특정문서를 제외가 아닌 점수를 줄이며 검색할 수 있다. 
    """
    def __init__(self):
        self._query = dict()
        self._query["boosting"] = dict()
        
    def postive(self, quries):
        self._query["boosting"]["postive"] = quries
        return self

    def negative(self, quries):
        self._query["boosting"]["negative"] = quries
        return self

    def negative_boost(self, values):
        self._query["boosting"]["negative_boost"] = values
        return self
    
    def build(self):
        return self._query