from asyncio import create_task


class TalkMemory(object):
    """
    대화내에 keyword를 저장하기 위한 객체
    대화형 모델에서 정확한 주소를 찾기 위해선 이전 대화를 기억하는것은 필수이다.
    """

    def __init__(self):
        self.talk = dict()

    def check_talk(self, id):
        if id in self.talk:
            return self.talk[id]

        return self.create_talk(id)

    def create_talk(self, id):
        """
        대화 정보를 담을 map을 생성한다.
        """
        self.talk[id] = {}
        self.talk[id]["completes"] = list()
        self.talk[id]["candidates"] = {}
        self.talk[id]["candidates"]["address"] = []
        self.talk[id]["candidates"]["number"] = []
        return self.talk[id]

    def get_talk(self, id):
        """
        id 를 통해 대화 정보를 가지고 온다.
        """
        return self.talk[id]

    def update_talk(self, id, value):
        """
        대화 정보를 업데이트 한다.
        """

    def delete_talk(self, id):
        """
        대화 정보를 삭제 한다.
        """
        del(self.talk[id])