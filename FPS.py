import time

FPS = 60
FRAME_RATE = int(1000 / FPS)


class Engine:
    s = 0  # type: float
    e = 0  # type: float

    @staticmethod
    def start():
        global s
        s = time.time()

    @staticmethod
    def end():
        global s
        global e
        e = time.time()
    @staticmethod
    def get_time():
        global s
        global e
        return e - s
