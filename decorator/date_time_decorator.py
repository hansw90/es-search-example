from datetime import datetime

class DatetimeDecorator:
    
    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        print(datetime.now())
        self.func(*args, **kwargs)
        print(datetime.now())

