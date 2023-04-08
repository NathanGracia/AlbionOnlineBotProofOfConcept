import time

import cv2
import keyboard as keyboard
import numpy as np
import pyautogui
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

from AlbionOnlineBotProofOfConcept.models.AbstractObject import AObject
from AlbionOnlineBotProofOfConcept.models.plot import Plot


def filter_duplicates(coords_list, threshold):
    filtered_eventable_list = []
    for coords in coords_list:
        if not filtered_eventable_list:
            filtered_eventable_list.append(coords)
        else:
            distances = [np.linalg.norm(np.array(coords[:2]) - np.array(existing_coords[:2])) for existing_coords in filtered_eventable_list]
            if all(d > threshold for d in distances):
                filtered_eventable_list.append(coords)
    return filtered_eventable_list

def analyze_screen(eventables):
    founds = {}
    # Recherchez l'image sur l'écran.
    for eventable in eventables:
        print('analyze_screen cherche : ' + eventable.name)
        # Recherchez l'image sur l'écran.
        image_locations = list(pyautogui.locateAllOnScreen(eventable.image, confidence=0.8))

        # Prendre une capture d'écran de l'écran entier
        screenshot = pyautogui.screenshot()
        # Convertir la capture d'écran en une image OpenCV
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        if (len(image_locations)) > 0:
            plt.rcParams['image.interpolation'] = 'nearest'
            plt.imshow(screenshot)
            filtered_locations = filter_duplicates(image_locations, threshold=100)
            print(f"Nombre d'eventables trouvés après filtrage : {len(filtered_locations)}")
            for image_location in filtered_locations:

                if image_location:
                    # Prend les coordonées.
                    left, top, width, height = image_location

                    if eventable.name == "plot_recoltable":

                        plot = Plot(left + width / 2, top + height / 2 + 100, 1)
                        founds.setdefault('plot_recoltable', []).append(plot)
                        # ajout du marker sur le plot
                        plt.scatter(plot.x, plot.y, s=200, c=np.random.randint(0, 50), marker='X', cmap='summer')
                    if eventable.name == "plot_confirm_recolt":
                        confirm = AObject(left + width / 2, top + height / 2)
                        founds.setdefault('plot_confirm_recolt', []).append(confirm)
                        # ajout du marker sur le bouton
                        plt.scatter(confirm.x, confirm.y, s=200, c=np.random.randint(0, 50), marker='X', cmap='summer')
                    if eventable.name == "map_player":
                        player = AObject(left + width / 2, top + height / 2)
                        founds.setdefault('map_player', []).append(player)
                        # ajout du marker sur le bouton
                        plt.scatter(player.x, player.y, s=200, c=np.random.randint(0, 50), marker='X', cmap='summer')

                    # ajout du rectangle autour de l'image trouvée
                    plt.gca().add_patch(Rectangle((left, top), width, height, edgecolor='green',
                                                  facecolor='none',
                                                  lw=2))

            # activer la correction gamma dans Matplotlib

            plt.show()
        return founds
def mount():
    keyboard.press_and_release('q')
    time.sleep(4)
