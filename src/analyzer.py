import argparse
import importlib
import json
import sqlite3
from sqlite3 import Connection, Cursor

from dateutil import parser as date_parser


class Analyzer:
    path: str
    watch_history = []
    extractors = []
    extractor_names = []
    connection: Connection
    cursor: Cursor

    available_extractors = ['MostRecent', 'MostWatched', 'TotalVideosWatched', 'FavouriteChannel', 'RickrollCount']

    def __init__(self, path: str, extractor_names=None):

        if extractor_names is None:
            extractor_names = []

        self.path = path
        self.extractor_names = extractor_names
        self.connection = sqlite3.connect('db.sqlite')
        # self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()

        # https://stackoverflow.com/a/3300514
        self.connection.row_factory = self._dict_factory

        self._init_db()

    @staticmethod
    def _dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):

            if col[0] == 'time':
                d[col[0]] = date_parser.parse(row[idx])
            else:
                d[col[0]] = row[idx]
        return d

    def _init_db(self):
        self.cursor.execute('''create table if not exists watch_history 
                                (
                                    id           char(11)      not null,
                                    title        varchar(2048) not null,
                                    url          varchar(128)  not null,
                                    channel_name varchar(128)  not null,
                                    channel_url  varchar(128)  not null,
                                    time         datetime      not null
                                );''')
        self.cursor.execute('delete from watch_history;')
        self.connection.commit()
        self.cursor.execute('vacuum')

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
                        'time': date_parser.parse(video['time'])
                    })

        self.cursor.executemany("INSERT INTO watch_history VALUES(:id, :title, :url, :channel_name, :channel_url, :time)", self.watch_history)
        self.connection.commit()

        self._init_extractors()

    def _init_extractors(self) -> None:
        self.extractors = []
        for extractor_name in self.extractor_names:
            # Dynamically creates class from its string representation
            class_name = f'{extractor_name}Extractor'
            module = importlib.import_module(f'extractor.{class_name}')

            extractor = getattr(module, class_name)(self.watch_history, self.connection)

            self.extractors.append(extractor)

    def print_results(self) -> None:

        for extractor in self.extractors:
            extractor.format()
            print('')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze YouTube watch history.')
    parser.add_argument('-p', '--path', help='path to watch-history.json (default=watch-history.json)', default='watch-history.json')
    parser.add_argument('-e', '--extractors', nargs='+', help='select extractors', choices=Analyzer.available_extractors)

    args = parser.parse_args()

    analyzer = Analyzer(args.path, extractor_names=args.extractors)
    analyzer.import_history_json()

    analyzer.print_results()
