from data_utils import *
import datetime as dt


# -------------------参数配置----------------- #
class Arg:
    def __init__(self):
        self.filename = './data/'
        self.date1 = '2019-01-01'
        self.date2 = date2 = getCurrentTime()
        self.current = dt.datetime.now().strftime('%Y-%m-%d')
