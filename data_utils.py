import tushare as ts
import pandas as pd
import os
import time
from matplotlib import pyplot as plt
import matplotlib.dates as mdate


# ----------------------获取当前时间------------------- #
def getCurrentTime():
    return time.strftime('[%Y-%m-%d]', time.localtime(time.time()))


# ----------------------下载某只股票数据------------------- #
# code:股票编码 日期格式：2020-03-11 filename：文件夹路径./data/ p_change：涨跌幅
def get_stock_data(code, date1, date2, filename):
    df = ts.get_hist_data(code, start=date1, end=date2)
    df1 = pd.DataFrame(df)
    df1 = df1[['open', 'high', 'close', 'low', 'volume', 'p_change']]
    df1 = df1.sort_values(by='date')
    print('共有%s天数据' % len(df1))
    if not os.path.exists(filename):
        os.makedirs(filename)
    path = code + '.csv'
    df1.to_csv(os.path.join(filename, path))


# ----------------------下载沪深300指数数据------------------- #
# date1是开始日期，date2是截止日期，filename是文件存放目录
def get_hs300_data(date1, date2, filename):
    df = ts.get_hist_data('399300', start=date1, end=date2)
    df1 = pd.DataFrame(df)
    df1 = df1[['open', 'high', 'close', 'low', 'volume', 'p_change']]
    df1 = df1.sort_values(by='date')
    print('共有%s天数据' % len(df1))
    df1.to_csv(os.path.join(filename, '399300.csv'))


# ----------------------下载沪深300股票信息------------------- #
def get_hs300_code_name(filename):
    df = ts.get_hs300s()
    df1 = pd.DataFrame(df)
    df1 = df1[['name', 'code']]
    df1.to_csv(os.path.join(filename, 'hs300.csv'))


# ----------------------绘制沪深300指数走势图------------------- #
def plot_hs300():
    # 获取连接备用
    cons = ts.get_apis()
    ts.set_token('luoganttcc46fcca1e059c38cde5f56fe7748f53c274036cb8cf0c061c2056a690')
    pro = ts.pro_api()

    df = ts.bar('000300', conn=cons, asset='INDEX', start_date='2020-01-01', end_date='2020-03-20')
    df = df.sort_index()

    # 生成figure对象
    fig = plt.figure(figsize=(12, 6))
    # 本案例的figure中只包含一个图表
    ax = fig.add_subplot(111)
    # 设置x轴为时间格式
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))

    # 设置x轴坐标值和标签旋转45°的显示方式
    plt.xticks(pd.date_range(df.index[0], df.index[-1], freq='M'), rotation=45)
    # x轴为table.index，也就是‘受理日期’，y轴为数量，颜色设置为红色
    ax.plot(df.index, df['open'], color='b')
    plt.show()


# ------------------------批量下载股票数据------------------------ #
def download_hs300_stock_data(date1, date2, filename):
    df = pd.read_csv('data/hs300.csv')['code']
    for code in df:
        code = "{0:06d}".format(code)
        if not os.path.exists('data/{}.csv'.format(code)):
            get_stock_data(code, date1, date2, filename)





if __name__ == "__main__":
    #get_stock_data('399300', '2020-01-01', '2020-03-18', './data/')
    #get_hs300_code_name('./data/')
    plot_hs300()
