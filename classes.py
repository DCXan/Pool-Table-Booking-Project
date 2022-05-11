import datetime
import time


class PoolTable:
    def __init__(self, table_number):
        self.name = f"Table # {table_number}"
        self.occupied = False
        self.startTime = None
        self.endTime = None
        self.totalTime = None

    def check_out(self):
        self.occupied = True
        self.startTime = datetime.datetime.now().replace(microsecond = 0)

    def check_in(self):
        self.occupied = False    
        self.endTime = datetime.datetime.now().replace(microsecond = 0)