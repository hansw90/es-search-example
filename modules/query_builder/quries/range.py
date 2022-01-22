_range = 'range'

_field = 'field'
_gte = 'gte'
_gt = 'gt'
_lte = 'lte'
_lt = 'llt'
_timezone = 'timezone'
_format = 'format'


class Range(object):
    """
    검색 하고자 하는 필드에서 입력한 범위에 포험되는 날짜나, 숫자, 문자열등을 검색할 때 사용
    """
    def __init__(self, field):
        self.field = field
        self.query = dict()
        self.query[_range] = dict()
        self.query[_range][self.field] = dict()

    # greater than or equal to 이상
    def gte(self, value):
        self.query[_range][_field][_gte] = value
        return self

    # greater than 초과 큼
    def gt(self, value):
        self.query[_range][_field][_gt] = value
        return self

    # less than or equal to
    def lte(self, value):
        self.query[_range][_field][_lte] = value
        return self

    # less than
    def lt(self, value):
        self.query[_range][_field][_lt] = value
        return self

    # ex "+01:00"
    def time_zone(self, value):
        self.query[_range][_field][_timezone] = value
        return self

    # ex "dd/MM/yyyy||yyyy" || 로 구분.
    def format(self, value):
        self.query[_range][_field][_format] = value
        return self

    def build(self):
        return self.query