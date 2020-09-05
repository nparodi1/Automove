#¡ /usr/bin/python3.7
# dsakjdalsdasdsa

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os

import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename

            extension = os.path.splitext(filename)[1]

            if extension.lower().endswith(('.png','.jpg','.jpeg')):
                new_destination = folder_images + "/" + filename
                os.rename(src, new_destination)
#            else:
#                new_destination = folder_destination2 + "/" + filename



folder_to_track = "/home/bonzo/Documentos/Por Ordenar"
folder_images = "/home/bonzo/Documentos/Por Ordenar/Imagenes"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()

try:
    while True:
        time.sleep(30)
except KeyboardInterrupt:
    observer.stop()

observer.join()
