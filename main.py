import sys

import cv2
import numpy as np
import pyautogui
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import time
import pickle
import datetime
import pprint
from models.eventable import Eventable
from models.plot import Plot
from PIL import Image
import helper

sys.path.insert(0, "/models")

pp = pprint.PrettyPrinter(indent=4)

def look_for_collectable_plots():
    eventables_categories = {}
    eventables = [
        Eventable('plot_recoltable',
                  "ressources/plot_recoltable_1920_2.PNG"),
        Eventable('plot_recoltable',
                  "ressources/plot_recoltable_1920_1.PNG"),
        Eventable('plot_recoltable',
                  "ressources/plot_recoltable_1920_4.PNG"),
        Eventable('plot_recoltable',
                  "ressources/plot_recoltable_1920_6.PNG"),
        Eventable('plot_recoltable',
                  "ressources/plot_recoltable_1920_7.PNG"),
        Eventable('plot_recoltable',
                  "ressources/plot_recoltable_1920_8.PNG"),
        Eventable('plot_recoltable',
                  "ressources/plot_recoltable_1920_9.PNG"),

    ]
    plots = []
    while True:
        while True:
            for eventable in eventables:
                eventable.image = cv2.imread(eventable.path)
                #todo trouver comment ajouter mes eventables dans la liste au fur et à mesure.
                eventables_categories.setdefault(eventable.name, set()).add(eventable)

            founds = helper.analyze_screen(eventables_categories)

            for AObject in founds.get('plot_recoltable', []):
                plot = Plot(AObject.x, AObject.y, 1)
                plots.append(plot)


    return plots



def main():

    look_for_collectable_plots()

if __name__ == '__main__':
    main()
