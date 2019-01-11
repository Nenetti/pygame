import time

FPS = 60
FRAME_RATE = int(1000 / FPS)


class Engine:
    s = 0  # type: float
    e = 0  # type: float

    def start(self):
        self.s = time.time()

    def end(self):
        self.e = time.time()

    def get_time(self):
        return self.e - self.s
