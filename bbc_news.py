from rss_parser import RssParser

urls = { 
    'top_stories': 'http://feeds.bbci.co.uk/news/rss.xml',
    'world': 'http://feeds.bbci.co.uk/news/world/rss.xml',
    'business': 'http://feeds.bbci.co.uk/news/business/rss.xml',
    'politics': 'http://feeds.bbci.co.uk/news/politics/rss.xml',
    'health':'http://feeds.bbci.co.uk/news/health/rss.xml',
    'education':'http://feeds.bbci.co.uk/news/education/rss.xml',
    'science_and_environment':'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml',
    'technology':'http://feeds.bbci.co.uk/news/technology/rss.xml',
    'entertainment_and_art':'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml',
    
}

top_stories = RssParser(urls['top_stories'], num_items=5)
world = RssParser(urls['world'], num_items=5)
business = RssParser(urls['business'], num_items=5)
politics = RssParser(urls['politics'], num_items=5)
health = RssParser(urls['health'], num_items=5)
education = RssParser(urls['education'], num_items=5)
science_and_environment = RssParser(urls['science_and_environment'], num_items=5)
technology = RssParser(urls['technology'], num_items=5)
entertainment_and_art = RssParser(urls['entertainment_and_art'], num_items=5)


print("--" * 40) 
print(top_stories.parsed_items)
print("--" * 40)
print(world.parsed_items)
print("--" * 40)
print(business.parsed_items)
print("--" * 40)
print(politics.parsed_items)
print("--" * 40)
print(health.parsed_items)
print("--" * 40)
print(education.parsed_items)
print("--" * 40)
print(science_and_environment.parsed_items)
print("--" * 40)
print(technology.parsed_items)
print("--" * 40)
print(entertainment_and_art.parsed_items)
print("--" * 40)