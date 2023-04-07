import pprint

import cv2
import numpy as np
import pyautogui
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import time
import pickle
import datetime
import pprint

pp = pprint.PrettyPrinter(indent=4)


def main():
    class eventable:
        def __init__(self, name, path):
            self.name = name
            self.path = path

            self.old_frame = 0
            self.image = None

    old_frame_dead = 0

    eventables = [
        eventable('crop_recoltable', "ressources/crop_recoltable.PNG"),

    ]
    for eventable in eventables:
        eventable.image = cv2.imread(eventable.path)
    while True:
        # Définissez l'emplacement de l'image que vous voulez localiser.
        image_location = "C:/Users/DeusKiwi/PycharmProjects/GUI/ressources/respawn.png"

        image = cv2.imread(image_location)  # Charger l'image depuis le chemin de fichier

        # Recherchez l'image sur l'écran.
        for eventable in eventables:

            # Recherchez l'image sur l'écran.
            image_locations = list(pyautogui.locateAllOnScreen(eventable.image, confidence=0.7))

            # Prendre une capture d'écran de l'écran entier
            screenshot = pyautogui.screenshot()
            # Convertir la capture d'écran en une image OpenCV
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            # Afficher l'image
            print('Nombre de crops trouvés :' + str(len(image_locations)))
            if(len(image_locations)) > 0 :

                plt.imshow(screenshot)
                for image_location in image_locations:

                    if image_location:
                        # Prend les coordonées.
                        left, top, width, height = image_location
                        # Ajoutez cette ligne pour faire cliquer la souris sur l'image détectée
                        #pyautogui.click(left + width / 2, top + (height / 2) + 100)  # Ici je descend un petit peu le curseur, car l'icône est suréleve. Rajouter une propriété dans l'objet ?

                        plt.gca().add_patch(Rectangle((left, top), width, height, edgecolor='green',
                                                      facecolor='none',
                                                      lw=2))
                plt.show()

                # else:
                #    eventable.old_frame = 0


if __name__ == '__main__':
    main()
