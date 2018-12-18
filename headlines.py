import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml',
            'abc': 'http://feeds.abcnews.com/abcnews/topstories',
            'cnn': 'http://rss.cnn.com/rss/edition.rss'}

@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)

