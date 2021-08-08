from extractor.Extractor import Extractor
from formatter.CliVideoFormatter import CliVideoFormatter


class FavouriteChannelExtractor(Extractor):
    formatter = CliVideoFormatter()

    def extract(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT channel_url, channel_name, COUNT(*) as count FROM watch_history GROUP BY channel_url ORDER BY count DESC')

        channel = cursor.fetchone()

        return {
            'heading': "Your most watched channel is",
            'videos': [
                {
                    'video': None,
                    'notes': [[f'{channel["channel_name"]} ({channel["channel_url"]}) with ', channel["count"], ' total views']]
                }
            ]
        }
