import time

import cv2
import keyboard as keyboard
import numpy as np
import pyautogui
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

from models.AbstractObject import AObject


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

def analyze_screen(eventables_categories):
    founds = {}
    # Recherchez l'image sur l'écran.
    for eventables_category in eventables_categories.keys():

        #print('analyze_screen cherche : ' + eventables_category)
        image_locations = []
        for eventable in eventables_categories[eventables_category]:
            # Recherchez l'image sur l'écran.
            before = len(image_locations);
            image_locations.extend(list(pyautogui.locateAllOnScreen(eventable.image, confidence=0.7)))
            if before < len(image_locations) :
                print("Trouvé : " + eventable.path)
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


                    result = AObject(left + width / 2, top + height / 2)
                    founds.setdefault(eventable.name, []).append(result)
                    # ajout du marker sur le plot
                    plt.scatter(result.x, result.y, s=200, c=np.random.randint(0, 50), marker='X', cmap='summer')

                    # ajout du rectangle autour de l'image trouvée
                    plt.gca().add_patch(Rectangle((left, top), width, height, edgecolor='green',
                                                  facecolor='none',
                                                  lw=2))

            plt.show()
    return founds
def mount():
    keyboard.press_and_release('q')
    time.sleep(4)
