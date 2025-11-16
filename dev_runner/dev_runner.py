import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, DirModifiedEvent, FileModifiedEvent
from mypy import api

from dev_runner.logger import log


class FileHandler(FileSystemEventHandler):

    def __init__(self, *, path: str, file: str):
        self.path = path
        self.file = file
        super()

    def on_modified(self, event: DirModifiedEvent | FileModifiedEvent) -> None:
        if not event.is_directory:
            result = api.run([
                "--strict",
                self.file,
            ])
            std_info = result[0]
            std_error = result[1]

            std_info = f"mypi: {std_info}"
            std_error = f"mypi: {std_error}"


            if std_error:
                log.error(std_error)
            elif "error:" in std_info:
                log.error(std_info)
            else:
                log.info(std_info)


class DevRunner:

    def __init__(self, *, path: str, file: str):
        self.path = path
        self.file = file
        self.file_handler = FileHandler(path=self.path, file=self.file)
        log.info("Starting dev-runner..")

    def run(self):
        result = api.run([
            "--strict",
            self.file,
        ])
        std_info = result[0]
        std_error = result[1]

        if std_error:
            std_error = f"[mypy]: {std_error}"
            log.error(std_error)
        elif "error:" in std_info:
            std_info = f"[mypy]: {std_info}"
            log.error(std_info)
        else:
            std_info = f"[mypy]: {std_info}"
            log.info(std_info)

    def watch(self):
        self.run()
        observer = Observer()
        observer.schedule(self.file_handler, self.path, recursive=True)
        observer.start()
        observer.join()
