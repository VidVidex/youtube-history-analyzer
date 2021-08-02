from abc import ABC
from sqlite3 import Connection

from formatter.Formatter import Formatter


class Extractor(ABC):
    formatter: Formatter
    watch_history: list[dict]
    connection: Connection

    def __init__(self, watch_history: list[dict], connection: Connection):
        self.watch_history = watch_history
        self.connection = connection

    def extract(self) -> dict:
        pass

    def format(self):
        self.formatter.format(self.extract())
