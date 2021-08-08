import os
from pathlib import Path
from unittest import TestCase

from analyzer import Analyzer


class TestMostRecentExtractor(TestCase):
    def test_extract(self):
        history_json = os.path.join(Path(__file__).parent.parent.resolve(), 'resources/watch-history.json')

        analyzer = Analyzer(history_json, extractor_names=["FavouriteChannel"])

        analyzer.import_history_json()
        result = analyzer.extractors[0].extract()

        self.assertEqual('Your most watched channel is', result['heading'])
        self.assertEqual([['Anne Reburn (https://www.youtube.com/channel/UChyNJxSsIXh2KyY3VvLnI2g) with ', 13, ' total views']], result['videos'][0]['notes'])
