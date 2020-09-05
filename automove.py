#¡ /usr/bin/python3.7

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

import os

import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):

            new_destination = None

            src = folder_to_track + "/" + filename

           # print
            fullfile = folder_to_track + filename
            date_creation = datetime.strptime(time.ctime(os.path.getctime(fullfile)),"%a %b %d %H:%M:%S %Y")

            extension = os.path.splitext(filename)[1]

            print(filename)
            print(extension.lower())
            print(extension)

            if extension.lower().endswith(('.png','.jpg','.jpeg')):
                folder_destination = folder_images + "/" + \
                                     str(date_creation.year) + "_" \
                                     + str(date_creation.month) + "/"

                if not os.path.exists(folder_destination):
                    os.makedirs(folder_destination)
                new_destination = folder_destination + filename


            elif extension.lower().endswith(('.pdf')):
                new_destination = folder_pdf + "/" + filename


            if new_destination:
                os.rename(src, new_destination)



folder_to_track = "/home/bonzo/Documentos/"
folder_images = "/home/bonzo/Documentos/Imagenes"
folder_pdf = "/home/bonzo/Documentos/PDF"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=False)
observer.start()

try:
    while True:
        time.sleep(30)
except KeyboardInterrupt:
    observer.stop()

observer.join()