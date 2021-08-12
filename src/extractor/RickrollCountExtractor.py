from extractor.Extractor import Extractor
from formatter.CliVideoFormatter import CliVideoFormatter


class RickrollCountExtractor(Extractor):
    formatter = CliVideoFormatter()

    def extract(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT COUNT(*) as count FROM watch_history where id = \'dQw4w9WgXcQ\'')

        rickroll_count = cursor.fetchone()

        return {
            'heading': 'You have been rickrolled',
            'videos': [
                {
                    'video': None,
                    'notes': [
                        [rickroll_count['count'], ' times']
                    ]
                }
            ]
        }
