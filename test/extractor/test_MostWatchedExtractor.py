import os
from pathlib import Path
from unittest import TestCase

from analyzer import Analyzer


class TestMostWatchedExtractor(TestCase):
    def test_extract(self):
        history_json = os.path.join(Path(__file__).parent.parent.resolve(), 'resources/watch-history.json')

        analyzer = Analyzer(history_json, extractor_names=["MostWatched"])

        analyzer.import_history_json()
        result = analyzer.extractors[0].extract()

        self.assertEqual('Most watched video:', result['heading'])
        self.assertEqual('shXAjhcXP58', result['videos'][0]['video']['id'])
        self.assertEqual([['watched ', 3, ' times']], result['videos'][0]['notes'])
