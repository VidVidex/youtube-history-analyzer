from abc import ABC

from formatter.Formatter import Formatter


class Extractor(ABC):
    formatter: Formatter
    watch_history: list[dict]

    def __init__(self, watch_history: list[dict]):
        self.watch_history = watch_history

    def extract(self) -> dict:
        pass

    def format(self):
        self.formatter.format(self.extract())
