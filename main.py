import feedparser, time

URL = "https://spongerice.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
## [![Typing SVG](https://readme-typing-svg.demolab.com?font=Do+Hyeon&pause=1000&color=F7F7F7&random=false&width=435&lines=%F0%9F%93%92+Latest+Blog+Post)](https://git.io/typing-svg)

"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
