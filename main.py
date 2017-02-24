from flask import Flask, render_template, session, redirect, url_for, flash, send_file
import form
import numpy as np
import pylab
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from flask import Flask, send_file
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


plt.style.use('ggplot') 
font = {'family' : 'meiryo'}
plt.rc('font', **font)


def plot(image):
    x = np.linspace(0, 10)
    y = np.sin(x)
    plt.plot(x, y)
    plt.savefig(image, format='png')