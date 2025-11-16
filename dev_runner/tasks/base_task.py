from abc import ABC, abstractmethod


class BaseTask(ABC):

    @abstractmethod
    def run(self) -> None: ...
