import feedparser
import json

class RssParser():
    def __init__(self, url, num_items=None):
        self.url = url
        self.num_items = num_items
        self.parsed_items = self.pretty_print(self.items())

    def parse_url(self):
        return feedparser.parse(self.url)

    def items(self):
        data = self.parse_url()
        items = []

        for item in data['entries']:
            title = item.get('title', None)
            link = item.get('link', None)
            published = item.get('published', None)
            data_dict = {
                'title': title,
                'link': link,
                'published': published
            }
            items.append(data_dict)

        if self.num_items:
            return items[0:self.num_items]
        else:
            return items

    def pretty_print(self, items):
        return json.dumps(items, indent=4)