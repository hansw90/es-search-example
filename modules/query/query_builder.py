# ES 쿼리 빌더
import json
import requests

# ES 쿼리를 생성한다.
class ElasticQuery(object):

    _security = None
    _url = None
    _index = None
    _doc_type = None
    _query = None

    # Query Object 를 생성한다.
    def __init__(self, security=None, url=None, index=None, doc_type=None):

        self._security = security
        self._url = url
        self._doc_type = doc_type
        
        self.es_url = f"https://{self._security}{self.es_url}"
        self.default_headers = {'Content-Type': 'application/json; charset=utf-8'}
        

        self._suggesters = []
        self._struct = {}

    # Query를 셋팅한다. 
    def query(self, query):
        self._query = query
    
    # Suggester 를 추가한다.
    def suggest(self, *suggesters):
        self._suggesters.extend(suggesters)

    # 쿼리의 임의속성을 셋팅한다.
    def set(self, key, value):
        self._struct[key] = value
        return self
    
    # 쿼리의 from/offset 을 셋팅한다
    def from_(self, from_):
        self._struct['from'] = from_
        return self

    # 결과 사이즈를 셋팅한다,
    def size(self, size):
        self._struct['size'] = size
        return self

    # timeout 시간을 셋팅한다.
    def timeout(self, timeout):
        self._struct['timeout'] = timeout
        return self

    # fields 셋팅한다.
    def fields(self, fields):
        self._struct['_source'] = fields
        return self
    
    # 결과를 sorting 한다.
    def sort(self, field, order=None):

        if 'sort' not in self._struct:
            self._struct['sort'] = list()
        
        if not order:
            self._struct['sort'].append(field)
        else:
            self._struct['sort'].append({
                field: {
                    'order': order,
                },
            })
        return self

    def struct(self):
        
        # Just query? Use as-is
        if self._query:
            self._struct['query'] = self._query

        if self._suggesters:
            suggs = {}
            for sugg in self._suggesters:
                suggs.update(sugg.dict())

            self._struct['suggest'] = suggs
        
        return self._struct

    # 쿼리의 실행결과를 리턴한다.
    def get(self):
        if self._url is None:
            return None
        
        if self._index is None:
            return None

        if self._doc_type is None:
            return None
        
        res = requests.post(
                    url=self.es_url
                    , headers=self.default_headers
                    , data=self._struct
                    )

        return res


