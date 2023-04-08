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
    eventables = [
        Eventable('plot_recoltable',
                  "C:/Users/DeusKiwi/PycharmProjects/albionBot/AlbionOnlineBotProofOfConcept/ressources/plot_recoltable.PNG"),
        Eventable('plot_recoltable',
                  "C:/Users/DeusKiwi/PycharmProjects/albionBot/AlbionOnlineBotProofOfConcept/ressources/plot_recoltable.PNG"),
        Eventable('plot_recoltable',
                  "C:/Users/DeusKiwi/PycharmProjects/albionBot/AlbionOnlineBotProofOfConcept/ressources/plot_recoltable.PNG"),
    ]
    plots = []
    while True:
        while len(plots) < 1:
            for eventable in eventables:
                eventable.image = cv2.imread(eventable.path)

                founds = helper.analyze_screen(eventables)

                plots.extend(founds.get('plot_recoltable', []))

        plots[0].collect()
        plots.pop(0)



def main():

    look_for_collectable_plots()

if __name__ == '__main__':
    main()
