from extractor.Extractor import Extractor
from formatter.CliVideoFormatter import CliVideoFormatter


class MostRecentExtractor(Extractor):
    formatter = CliVideoFormatter()

    def extract(self):
        video = self.watch_history[0]

        return {
            'heading': "Most recently watched video:",
            'videos': [
                {
                    'video': video,
                    'notes': []
                }
            ]
        }
