import datetime


class Random:

    def __init__(self) -> None:
        time = datetime.datetime.now().microsecond 
        self.x0 = time
        self.x1 = time
        self.x2 = time
    
    def next(self):
        x = (1176 * self.x0 + 1476 * self.x1 + 1776 * self.x2) % (pow(2,32) - 5)
        self.x2 = self.x1
        self.x1 = self.x0
        self.x0 = x
        return x