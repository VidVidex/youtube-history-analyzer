from collections import Counter

from extractor.Extractor import Extractor
from formatter.CliVideoFormatter import CliVideoFormatter


class MostWatchedExtractor(Extractor):
    formatter = CliVideoFormatter()

    def extract(self):
        ids = [v['id'] for v in self.watch_history]

        counter = Counter(ids)
        count = counter.most_common(1)[0][1]
        most_viewed_video_id = counter.most_common(1)[0][0]

        for v in self.watch_history:
            if v['id'] == most_viewed_video_id:
                video = v
                break

        return {
            'heading': "Most watched video:",
            'videos': [
                {
                    'video': video,
                    'notes': [
                        ['watched ', count, ' times']
                    ]
                }
            ]
        }
