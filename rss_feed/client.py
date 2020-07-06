import feedparser
import socket

# feed = feedparser.parse("https://news.un.org/feed/subscribe/\en/news/topic/economic-development/feed/rss.xml")
feed = feedparser.parse("https://news.un.org/feed/subscribe/en/news/topic/economic-development/feed/rss.xml")
# feed = feedparser.parse("https://support.microsoft.com/app/content/api/content/feeds/sap/en-us/32d322a8-acae-202d-e9a9-7371dccf381b/rss")

print("Number of RSS posts: ", len(feed.entries), "\n")

while True:
    print("###### Begin Feed ######\n\n")
    for post in feed.entries:
        print(post.title, ":\n", post.link, "\n\n")

    print("###### End Feed ######\n\n")
    time.sleep(30)