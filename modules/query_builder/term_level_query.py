
_term = "term"

class TermQuery():

    def __init__(self):
        self.query = dict()
    
    def term(self, field, search, boost=None):
        """
        term query
        검색하고자 하는 필드에 정확한 텀을 포함하고 있는지 확인하는 쿼리
        """
        self.query[_term][field][_value] = search

        if boost != None:
            self.query[_term][_boost] = boost
        
        return self.query


    def terms(self,field, value, boost):
        """
        검색하고자 하는 필드에 정확한 텀들을 포함하고 있는지 확인하는 쿼리
        """

    def terms_set(self, field, values, value_only):
        """
        지정된 용어중 하나 이상과 일치하는 문서를 찾는다. 지정된 최소값과 일치해야 하는 용어의 수는 필드 또는 스크립트와 일치해야 한다.
        """

    def range(self, field, get, gt, lte, lt):
        """
        검색 하고자 하는 필드에서 입력한 범위에 포험되는 날짜나, 숫자, 문자열등을 검색할 때 사용
        """        

    def exist(self, field):
        """
        검색하고자 하는 필드에 값이 있는지 여부 확인
        """

    def missing(self, field):
        """
        검색하고자 하는 필드에 값이 없는지 확인
        """

    def prefix(self, field, value, boost):
        """
        검색하고자 하는 필드에서 입력한 값으로 시작하는 문장이 있는지 검색할 때 사용
        """


    def wildcard(self, field, value, boost):
        """
        와일드 카드 *,? 를 사용하여 검색하는 방법, 전체를 다 뒤져서 찾아야 하기 때문에 성능에 좋지 못하다.
        """

    def fuzzy(self, field, value, boost, fuzziness, prefix_length, max_expansions):
        """
        입력한 term과 비슷한 문자를 찾을때 사용하는 쿼리 레벤스테인 거리 알고리즘을 사용하며, 설정한 거리에 따라서 어느정도 유사도에 값을 찾을지 정할수 있다.
        한글 초성 중성 종성 단위의 거리는 따로 처리가 필요함
        """

    def _type(self, value):
        """
        입력한 타입에 맞는 값을 찾는 쿼리
        """

    def ids(self, values:list(), type):
        """
        타입과 IDS를 가진 값을 찾는 쿼리
        """