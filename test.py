import tushare as ts
from matplotlib import pyplot as plt
import matplotlib.dates as mdate
import pandas as pd
import numpy as np
from data_utils import *
import datetime
from config import Arg
import dateutil

args = Arg()

if __name__ == '__main__':
    get_hs300_data(args.date1, args.date2, args.filename)
