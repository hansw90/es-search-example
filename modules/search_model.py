import json
import requests

import modules.utils.es_utils as esutils

class SearchModel(object):

    def __init__(self):
        self.url = "http://office.leevi.co.kr:45501/"
        self.security_token = "elastic:parrot@"
        self.address_index = "/parrot_address"
        self.default_headers = {'Content-Type': 'application/json; charset=utf-8'}
        self.es_url = self.security_token+self.url

        self.doc = "/_doc"
        self.search= "/_search"
        self.update = "/update"
    
    
    def get_docs_by_id(self, index, id, body):
        """
        doc_id를  통하여 docs를 가지고 온다.
        """
        es_url =  f"{self.es_url}{index}{self.doc}/{id}"
        es_result = requests.get(url=es_url, headers=self.default_headers)
        return es_result
    
    def search_docs(self, index, query):
        """
        query를 통해 docs 를 검색한다.
        """
        es_url = f"{self.es_url}{index}{self.search}"
        es_result = requests.post(es_url, headers=self.default_headers, data=json.dumps(query, ensure_ascii=False).encode('utf-8'))
        return es_result

    def insert_docs(self, index, body):
        """
        docs를 추가한다.
        """
        es_url = f"{self.es_url}{index}{self.doc}"
        es_result = requests.post(
                            es_url
                            , headers=self.default_headers
                            , data=json.dumps(body, ensure_ascii=False)
                            , default=esutils.defaultconverter).encode('utf-8')
        return es_result

    def insert_bulk(self, index, body):
        """
        bulk insert를 실시한다.
        """


    def update_docs(self, index, id, body):
        """
        docs를 업데이트 한다.
        """
        data = esutils.del_none(body)
        data = json.dumps(data, ensure_ascii=True).encode('utf-8')
        es_url = f"{self.es_url}{index}{self.update}/{id}"
        es_result = requests.post(
                    url=es_url
                    , headers=self.default_headers
                    , data=data
                    )
        return es_result

    def delete_docs(self, index, id):
        """
        docs를 제거한다.
        """

    def delete_by_query(self, index, query):
        """
        query를 통해 docs들을 제거한다.
        """

    def analyze(self, index, query):
        """
        query를 분석한다.
        """
        pass



# 주소 검색 예제 프로젝트
if __name__ == 'main':
    print("hello address")