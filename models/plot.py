import time

import cv2
import numpy as np
import pyautogui
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

from AlbionOnlineBotProofOfConcept import helper
from AlbionOnlineBotProofOfConcept.models.eventable import Eventable


class Plot():
    def __init__(self, x, y, is_collectable = 0):
        self.is_collectable = is_collectable
        self.x = x
        self.y = y

    def collect(self):
        pyautogui.click(self.x, self.y)
        print('Click sur le plot')
        self.confirm()
        pass

    def confirm(self, keyboard=None):
        eventables = [
            Eventable('plot_confirm_recolt',
                      "C:/Users/DeusKiwi/PycharmProjects/albionBot/AlbionOnlineBotProofOfConcept/ressources/confirm.PNG"),
        ]

        confirms = []
        start_time = time.time()  # Temps de début de la recherche
        timeout = 3  # Temps limite en secondes
        while len(confirms) < 1 and time.time() - start_time < timeout:
            for eventable in eventables:
                eventable.image = cv2.imread(eventable.path)

                founds = helper.analyze_screen(eventables)

                confirms = founds.get('plot_confirm_recolt', [])
        if len(confirms) < 1:
            print("Le bouton de confirmation n'a pas été trouvé.")
            helper.mount()
            return  # Sortir de la fonction si le bouton n'est pas trouvé

        pyautogui.click(confirms[0].x, confirms[0].y)
        print('Click sur le bouton de confirmation')
        time.sleep(1)

        pass
