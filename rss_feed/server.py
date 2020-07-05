
import socket
import feedparser

feed = feedparser.parse("https://support.microsoft.com/app/content/api/content/feeds/sap/en-us/32d322a8-acae-202d-e9a9-7371dccf381b/rss")

print(type(feed))
# print(feed)
print(feed.href)