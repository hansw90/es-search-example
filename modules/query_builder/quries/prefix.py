_prefix = 'prefix'
_field = 'field'

class Prefix(object):
    """
    검색하고자 하는 필드에서 입력한 값으로 시작하는 문장이 있는지 검색할 때 사용
    """

    def __init__(self):
        self.query = dict()
        self.query[_prefix] = dict()
        
    def filed(self, field):
        self.query[_prefix][_field] = field
        return self

    def build(self):
        return self.query