
class Analyze(object):
    """
    TODO 기능 추가 필요 & VALID CHECK 
    문자를 분석한다.
    """
    def __init__(self):
        self.query = dict()

        self.texts = []
        self._filter = None

    def tokenizer(self, value):
        self.query["tokenizer"] = value
        return self

    def text(self, values):
        self.text.extend(values)
        return self

    # todo param 받아서 변경하는걸로
    def filter(self, values):
        self._filter = values
        return self

    def build(self):
        if  self._filter != None:
            self.texts = ' '.join(self.texts)
            self.query['filter'] = self._filter

        self.query['text'] = self.texts
        return self.query
        
