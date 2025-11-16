from abc import ABC, abstractmethod


class BaseTask(ABC):

    @staticmethod
    def run() -> None: ...
