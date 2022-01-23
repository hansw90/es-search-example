from quries import bool, boosting, constant_score, function_score

class CompoundQuery(object):

    def __init__(self):
        pass

    def bool(self):
        return bool.BoolQuery()

    def boosting(self):
        return boosting.BoostingQuery()

    def constant_score(self):
        return constant_score.ConstantScoreQuery()

    def function_score(self):
        return function_score.FunctionScoreQuery()
