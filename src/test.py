import sys, os
sys.path.append(os.getcwd()+"/src")

class Tester(object):

    def __init__(self):
        self.talk_no = 1
        pass
    
    def read_file(self, name):
        f = open(f"{name}", "r")
        while True:
            line = f.readline()
            if not line : break
            
            self.read_line(line)

    def read_line(self, line):
        if line.startswith("#"):
            print(f"{self.talk_no} 번째 대화 주소 키워드")
            self.talk_no += 1
            return
        
        if line.startswith("//"):
            return
        
        print(line)


if __name__ == "__main__":

    test = Tester()
    file_name = "test.csv"
    file_path = os.path.join(os.getcwd()+"/src", file_name)
    test.read_file(file_path)
