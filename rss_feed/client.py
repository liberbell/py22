import feedparser
import socket

feed = feedparser.parse(("https://news.un.org/feed/subscribe/\en/news/topic/economic-development/feed/rss.xml"))

print("Number of RSS posts: ", len(feed.entries), "\n")