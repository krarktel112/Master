import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileOpenHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File opened: {event.src_path}")

def watch_directory(path):
    observer = Observer()
    event_handler = FileOpenHandler()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    path_to_watch = "."  # Replace with the directory you want to watch
    watch_directory(path_to_watch)
