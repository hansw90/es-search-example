class FunctionScoreQuery(object):
    """
    용어나 필드를 부스팅하여 스코어를 조정하는데는 한계가 있다.
    좀더 유연하게 스코어링을 조절하기 위해 function_score 쿼리를 사용한다.
    """
    
    def __init__(self):
        self._query = dict()
        self._query["function_score"] = dict()
        self._query["function_score"]['functions'] = []

    def query(self, quries):
        self._query["fucntion_score"]["query"] = quries
        return self

    def boost(self, values):
        self._query["function_score"]["boost"] = values
        return self

     #functions에서 정의되는 함수들은 쿼리의 결과에 대해서만 적용된다.
    def functions(self, functions):
        
        self._query["function_score"]['functions'].extend(functions)

    def function(self, filter=None, boost_factor=None, script_score=None, weigth=None, random_score=None, field_value_factor=None, decay_functions=None, weight=None):
        q = dict()
        
        if filter != None: 
            q["filter"] = filter
        
        # 가장 간단한 함수로, 단순 상수곱 한다, 필터를 이용하여 부스팅할 문서를 결정한다.
        if boost_factor != None:
            q['boost_factor'] = boost_factor
        
        # 가장 자유도가 높은 스코어링 방식
        if script_score != None:
            q["script_score"] = script_score
        
        # 문서를 랜덤하게 정렬하고 싶을때 사용한다. seed값을 동일하게 주면 동일한 결과가 나타난다.
        if random_score != None:
            q['random_score'] = random_score
        
        # 숫자형 필드의 값을 스코어에 이용한다. ex) 좋아요 버튼을 누른 카운트등을 검색결과에 이용할때 사용
        if field_value_factor != None:
            q['field_value_factor'] = field_value_factor
        
        # 특정 필드의 값을 이용하여 스코어를 점진적으로 줄여나가는 함수 (decay, gauss, exp)
        if decay_functions != None:
            q['decay_functions'] = decay_functions

        if weight != None:
            q['weight'] = weight
        
        return q

    
    def max_boost(self, values):
        self._query["function_score"]["max_boost"] = values
        return self

    # functions 배열안의 계산된 스코의 결합 방법을 지정한다.
    # (multiply), sum, avg, first, max, min
    def score_mode(self, values):
        self._query["function_score"]["score_mode"] = values
        return self

    # 함수 스코어를 쿼리 결과의 스코어와 결합하는 방법
    def boost_mode(self, values):
        self._query["function_score"]["boost_mode"] = values
        return self

    def min_score(self, values):
        self._query["function_score"]["min_score"] = values
        return self

    def build(self):
        return self._query
