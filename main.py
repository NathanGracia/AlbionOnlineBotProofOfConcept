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


sys.path.insert(0, "/models")

pp = pprint.PrettyPrinter(indent=4)

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

def main():


    old_frame_dead = 0
    plots = []

    eventables = [

        Eventable('plot_recoltable', "ressources/plot_recoltable_1920.PNG"),

    ]
    for eventable in eventables:
        eventable.image = cv2.imread(eventable.path)
    while True:

        # Recherchez l'image sur l'écran.
        for eventable in eventables:

            # Recherchez l'image sur l'écran.
            image_locations = list(pyautogui.locateAllOnScreen(eventable.image, confidence=0.7))

            # Prendre une capture d'écran de l'écran entier
            screenshot = pyautogui.screenshot()
            # Convertir la capture d'écran en une image OpenCV
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)


            if(len(image_locations)) > 0 :

                plt.imshow(screenshot)
                filtered_locations = filter_duplicates(image_locations, threshold=100)
                print(f"Nombre de plots trouvés après filtrage : {len(filtered_locations)}")
                for image_location in filtered_locations:

                    if image_location:
                        # Prend les coordonées.
                        left, top, width, height = image_location
                        # Ajoutez cette ligne pour faire cliquer la souris sur l'image détectée
                        #pyautogui.click(left + width / 2, top + (height / 2) + 100)  # Ici je descend un petit peu le curseur, car l'icône est suréleve. Rajouter une propriété dans l'objet ?
                        plots.append(Plot());
                        plt.gca().add_patch(Rectangle((left, top), width, height, edgecolor='green',
                                                      facecolor='none',
                                                      lw=2))
                plt.show()

                # else:
                #    eventable.old_frame = 0


if __name__ == '__main__':
    main()
