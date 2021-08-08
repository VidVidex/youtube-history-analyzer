from extractor.Extractor import Extractor
from formatter.CliVideoFormatter import CliVideoFormatter


class TotalVideosWatchedExtractor(Extractor):
    formatter = CliVideoFormatter()

    def extract(self):

        count = len(self.watch_history)

        return {
            'heading': "Total number of videos watched:",
            'videos': [
                {
                    'video': None,
                    'notes': [[count]]
                }
            ]
        }