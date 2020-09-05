###########################################################
#  Auto move (and sort) files after being dropped in a folder
#  Developed by Sebastián Nicolás Parodi
#  Email : nparodi@gmail.com
#  Started on Sept 2020
###########################################################

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

import os
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):

            new_destination = None
            src = f"{folder_to_track}/{filename}"
            extension = os.path.splitext(filename)[1]

            if extension.lower().endswith(('.png', '.jpg', '.jpeg')):
                # In case of images i will put them in a sub folder depending on file modification date
                last_modification = datetime.strptime(time.ctime(os.path.getmtime(src)), "%a %b %d %H:%M:%S %Y")

                folder_destination = f"{folder_images}{str(last_modification.year)}_{str(last_modification.month)}/"

                # Checks if folder already exists
                if not os.path.exists(folder_destination):
                    os.makedirs(folder_destination)

                new_destination = folder_destination + filename

            elif extension.lower().endswith('.pdf'):
                # In case of PDF =
                new_destination = folder_pdf + filename

            if new_destination:
                if not os.path.isfile(new_destination):
                    os.rename(src, new_destination)  # Moves file to new destination
                    print(f"{src} was moved to {new_destination}")
                else:
                    print(f"{new_destination} already exists on destination folder")


# Folders to track and destiny folders
folder_to_track = f"{os.path.expanduser('~')}/Documentos"
folder_images = f"{folder_to_track}/Imagenes/"
folder_pdf = f"{folder_to_track}/PDF/"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=False)
observer.start()

try:
    while True:
        time.sleep(30)
except KeyboardInterrupt:
    observer.stop()

observer.join()
