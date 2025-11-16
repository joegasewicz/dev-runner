from watchdog.events import FileSystemEventHandler, DirModifiedEvent, FileModifiedEvent

from dev_runner.tasks import BaseTask


class FileEventHandler(FileSystemEventHandler):

    def __init__(self, *, tasks: list[BaseTask]):
        self.tasks = tasks
        super()

    def on_modified(self, event: DirModifiedEvent | FileModifiedEvent) -> None:
        if not event.is_directory:
            for task in self.tasks:
                task.run()
