from termcolor import colored

from formatter.Formatter import Formatter


class CliVideoFormatter(Formatter):

    def format(self, data: dict):
        print(data['heading'])

        if data['videos'][0]['video'] is not None:
            self.print_video(data['videos'][0]['video'])

        for note in data['videos'][0]['notes']:
            print(' ' * 5, end='')
            for part in note:
                if isinstance(part, int):
                    print(colored(part, 'cyan'), end='')
                else:
                    print(part, end='')
            print()

    @staticmethod
    def print_video(video):
        print(' ' * 4, f'{colored(video["title"], "green")} ({video["url"]})')
        print(' ' * 4, f'by {colored(video["channel_name"], "magenta")} ({video["channel_url"]})')
