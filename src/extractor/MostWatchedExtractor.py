from extractor.Extractor import Extractor
from formatter.CliVideoFormatter import CliVideoFormatter


class MostWatchedExtractor(Extractor):
    formatter = CliVideoFormatter()

    def extract(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT *, COUNT(*) as count FROM watch_history GROUP BY id ORDER BY count DESC')

        video = cursor.fetchone()

        return {
            'heading': 'Most watched video:',
            'videos': [
                {
                    'video': video,
                    'notes': [
                        ['watched ', video['count'], ' times']
                    ]
                }
            ]
        }
