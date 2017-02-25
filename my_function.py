from pylab import *
from pandas import *
import matplotlib.pyplot as plt
import numpy as np
import pylab
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io
import random
import re
import os
from matplotlib.font_manager import FontProperties


class my_function:
    
    @staticmethod
    def setData(player):
        
        df = pd.read_csv('./kings/data/Kings_Game_HIST_' + player + '.csv', encoding='shift-jis')
        df2 = pd.read_csv('./kings/data/Kings_Game_HISTORY.csv', encoding='shift-jis')
        left = pd.DataFrame(df)
        right = pd.DataFrame(df2)
        output = pd.merge(left, right, how='left', on=['Time'])
        return output

    @staticmethod
    def getData(statsItem, player):
        
        output = my_function.setData(player);
        lose = output.where(output.WinLose == "L")
        win = output.where(output.WinLose == "W")
        win = win.dropna(subset=['No'])
        lose = lose.dropna(subset=['No'])

        plt.plot(win[statsItem], "ko--", color="b", label="1")
        plt.plot(lose[statsItem], "ko--", color="r", label="2")
        plt.legend([u'WIN', u'LOSE'])
        plt.title(player + ":" + statsItem + "_HIST")
        plt.xlabel("TIME")
        plt.ylabel(statsItem)
        return plt

    @staticmethod
    def getCorr(player):        

        output = my_function.setData(player);
        output = output.replace(re.compile('^W$'), 1)
        output = output.replace(re.compile('^L$'), 0)
        obj = output.corr()
        after = obj.sort_values(by="WinLose", ascending=True)
        ax= after.plot.bar(y=['WinLose'])
        return ax

    @staticmethod
    def delFiles(targetPath):        
        for root, dirs, files in os.walk(targetPath, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))