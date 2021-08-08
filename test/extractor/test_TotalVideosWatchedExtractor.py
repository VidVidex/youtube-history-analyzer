import os
from pathlib import Path
from unittest import TestCase

from analyzer import Analyzer


class TestTotalVideosWatchedExtractor(TestCase):
    def test_extract(self):
        history_json = os.path.join(Path(__file__).parent.parent.resolve(), 'resources/watch-history.json')

        analyzer = Analyzer(history_json, extractor_names=["TotalVideosWatched"])

        analyzer.import_history_json()
        result = analyzer.extractors[0].extract()

        self.assertEqual('Total number of videos watched:', result['heading'])
        self.assertEqual([[16]], result['videos'][0]['notes'])
