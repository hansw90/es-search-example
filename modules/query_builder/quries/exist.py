
_field = 'field'
_exist = 'exist'

class Exist(object):
    """
    검색하고자 하는 필드에 값이 있는지 여부 확인
    """

    def __init__(self):
        self.query = dict()
        self.query[_exist] = dict()
        
    def filed(self, field):
        self.query[_exist][_field] = field
        return self

    def build(self):
        return self.query