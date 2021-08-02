# Adding a new extractor

Create a new file called `SomethingExtractor.py` in the `extractor` directory and modify the following template to make your own extractor:

```python
from extractor.Extractor import Extractor
from formatter.CliVideoFormatter import CliVideoFormatter


class SomethingExtractor(Extractor):
    formatter = CliVideoFormatter()

    def extract(self):
        
        # Your data extraction logic goes here

        return {
            'heading': "This will be displayed before the extracted data",
            'videos': [
                {
                    'video': None,
                    'notes': []
                }
            ]
        }
```

Since `SomethingExtractor` extends `Extractor` it has access the the `self.watch_history` property, which is a list of dicts, each containing a watched video:

```python
[
    {
        'id': '7JTWc6jWZ9Q', 
        'title': "An Unedited, Rain-Soaked Ride on Claughton's Aerial Ropeway", 
        'url': 'https://www.youtube.com/watch?v=7JTWc6jWZ9Q', 
        'channel_name': 'Tom Scott', 
        'channel_url': 'https://www.youtube.com/channel/UCBa659QWEk1AI4Tg--mrJ2A', 
        'time': datetime.datetime(2021, 7, 19, 17, 49, 43, 147000, tzinfo=tzutc())
    },
    {
        'id': 'shXAjhcXP58', 
        'title': 'Good Riddance (Time Of Your Life) - Green Day Cover', 
        'url': 'https://www.youtube.com/watch?v=shXAjhcXP58', 
        'channel_name': 'Anne Reburn', 
        'channel_url': 'https://www.youtube.com/channel/UChyNJxSsIXh2KyY3VvLnI2g', 'time': datetime.datetime(2021, 7, 17, 11, 32, 23, 654000, tzinfo=tzutc())
    }
]
```

While python dicts are nice and all, sometimes you need more powerful queries. That is why you also have access to a SQLite connection `self.connection`. The database contains a single table with the following structure:
```sql
create table watch_history
(
    id           char(11)      not null,
    title        varchar(2048) not null,
    url          varchar(128)  not null,
    channel_name varchar(128)  not null,
    channel_url  varchar(128)  not null,
    time         datetime      not null
);
```


## Formatter

Each extractor has a `formatter` property which specifies the formatter that will be used to display extracted data. For now you can leave this set to `CliVideoFormatter`.

### Return format

Your `extract` method should return a dict with the following structure:
```py
{
    'heading': "This will be displayed before the extracted data",
    'videos': [
        {
            'video': None,
            'notes': []
        }
    ]
}
```

`videos` list contains dicts with the videos you've extracted from the watch history and optionally related notes, which will be displayed next to the  video.

`notes` has the following structure:

```py
'notes': [
    ['watched ', count, ' times']
]
```

Each list under `notes` will be displayed as a single line in the final text. Each list contains another list in which numbers are separate from words so that the formatter can color numbers differently than strings.


## Registering a new extractor

After you've created the `SomethingExtractor` class, add your extractor name to the `available_extractors` property of `Analyzer` class.

To make sure your extractor works as intended add a `TestSomethingExtractor(TestCase)` class in the `test/extractor/test_SomethingExtractor.py` file and create at least one test case for your `extract()` method.

Addionally add a short description of what this extractor does to the `usage.md` file
