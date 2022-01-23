class ConstantScoreQuery(object):
    """
    constant score 쿼리는 filter query를 래핑하고, TF, IDF 등과 같이 점수 요소에 관계 없이 일치하는 모든 문서에 동일한 점수를 제공한다.
    이는 문서가 얼마나 일치 했는지는 상관 안하고 문서가 일치하냐 안하냐만 고려한다. 
    내가 룰기반 검색을 했을때 이러한 방법 사용함
    """
    def __init__(self):
        self._query = dict()
        self._query["constant_score"] = dict()

    def filter(self, quries):
        self._query["constant_score"]["filter"] = quries
        return self

    def boost(self, values):
        self._query["constant_score"]["boost"] = values
        return self
    
    def build(self):
        return self._query