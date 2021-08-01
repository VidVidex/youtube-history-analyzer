from unittest import TestCase

from analyzer import Analyzer


class TestAnalyzer(TestCase):
    def test_import_history_json(self):
        analyzer = Analyzer('resources/watch-history.json')

        analyzer.import_history_json()
        self.assertEqual(len(analyzer.watch_history), 16)
