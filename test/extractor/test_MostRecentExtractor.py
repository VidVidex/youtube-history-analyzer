import os
from pathlib import Path
from unittest import TestCase

from analyzer import Analyzer


class TestMostRecentExtractor(TestCase):
    def test_extract(self):
        history_json = os.path.join(Path(__file__).parent.parent.resolve(), 'resources/watch-history.json')

        analyzer = Analyzer(history_json, extractor_names=["MostRecent"])

        analyzer.import_history_json()
        result = analyzer.extractors[0].extract()

        self.assertEqual('Most recently watched video:', result['heading'])
        self.assertEqual('I0-izyq6q5s', result['videos'][0]['video']['id'])
        self.assertEqual([], result['videos'][0]['notes'])
