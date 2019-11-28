import os
import json
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    i=1
    def on_modified (self, event):
        new_name = "new_file_" + str(self.i)
        for filename in os.listdir(folder_to_track):
            file_exists = os.path.isfile(folder_destination + "/" + new_name)
            while file_exists:
                self.i += 1
                new_name = "Beat2Sem2019_" + str(self.i)
                file_exists = os.path.isfile(folder_destination + "/" + new_name)

            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + new_name
            os.rename(src, new_destination)

folder_to_track = "C:/Users/arthu/Desktop/Teste"
folder_destination = "C:/Users/arthu/Desktop/Destino"
event_hander = MyHandler()
observer = Observer()
observer.schedule(event_hander, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
