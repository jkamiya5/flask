from flask import Flask, render_template, session, redirect, url_for, flash, send_file
import matplotlib.pyplot
from matplotlib.backends.backend_agg import FigureCanvasAgg
import random
import string
import os
import my_function as func

class TempImage(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def create_png(self, player, itemName):
        
        fig, ax = matplotlib.pyplot.subplots()
        ax.set_title(player + "のスタッツ・・・" + itemName)  
        obj = func.my_function()
        obj.getData(itemName, player)
        canvas = FigureCanvasAgg(fig)
        canvas.print_figure(self.file_name)

    def create_png1(self, player):
        
        fig, ax = matplotlib.pyplot.subplots()
        ax.set_title(player + "のスタッツ・・・")  
        obj = func.my_function()
        obj.getCorr(player)
        matplotlib.pyplot.savefig(self.file_name)


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        #os.remove(self.file_name)
        print()


    def getPng(self, player, itemName):
        chars = string.digits + string.ascii_letters
        target = ''.join(random.choice(chars) for i in range(64)) + '.png'
        img_name = "static/img/" + target

        with TempImage(img_name) as img:
            img.create_png(player, itemName)
            send_file(img_name, mimetype='image/png')
        
        return img_name

    def getPng1(self, player):
        chars = string.digits + string.ascii_letters
        target = ''.join(random.choice(chars) for i in range(64)) + '.png'
        img_name = "static/img/" + target

        with TempImage(img_name) as img:
            img.create_png1(player)
            send_file(img_name, mimetype='image/png')
        
        return img_name