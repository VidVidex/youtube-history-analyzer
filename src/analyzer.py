import importlib
import json
import os
from dateutil import parser


class Analyzer:
    path: str
    watch_history = []
    extractors = []
    extractor_names = []

    def __init__(self, path: str, extractor_names=None):

        if extractor_names is None:
            extractor_names = []

        self.path = path
        self.extractor_names = extractor_names

    def import_history_json(self) -> None:
        self.watch_history = []
        with open(self.path, 'r') as f:
            history = json.load(f)

            for video in history:

                if 'subtitles' in video and 'titleUrl' in video:
                    self.watch_history.append({
                        'id': video['titleUrl'][-11:],
                        'title': video["title"].partition(' ')[2],
                        'url': video["titleUrl"],
                        'channel_name': video["subtitles"][0]['name'],
                        'channel_url': video["subtitles"][0]['url'],
                        'time': parser.parse(video['time'])
                    })

        self._init_extractors()

    def _init_extractors(self) -> None:
        self.extractors = []
        for extractor_name in self.extractor_names:
            # Dynamically creates class from its string representation
            class_name = f'{extractor_name}Extractor'
            module = importlib.import_module(f'extractor.{class_name}')

            extractor = getattr(module, class_name)(self.watch_history)

            self.extractors.append(extractor)

    def print_results(self) -> None:

        for extractor in self.extractors:
            extractor.format()
            print('')
