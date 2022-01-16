

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

class FunctionScoreQuery(object):
    """
    용어나 필드를 부스팅하여 스코어를 조정하는데는 한계가 있다.
    좀더 유연하게 스코어링을 조절하기 위해 function_score 쿼리를 사용한다.
    """
    def __init__(self):
        self._query = dict()
        self._query["function_score"] = dict()

def dis_max(self):
    pass

def function_score(self, functions:list()):
    pass

def indices(self):
    pass

def limit(self):
    pass