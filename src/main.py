import argparse

from analyzer import Analyzer

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze YouTube watch history.')
    parser.add_argument('-p', '--path', help='path to watch-history.json', default='watch-history.json')

    extractor_commands = parser.add_argument_group('Extractors')
    extractor_commands.add_argument('-e', '--extractors', nargs='+', help='display most recent video', choices=['MostRecent', 'MostWatched'])

    args = parser.parse_args()

    analyzer = Analyzer(args.path, extractor_names=args.extractors)
    analyzer.import_history_json()

    analyzer.print_results()
