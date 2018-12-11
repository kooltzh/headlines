import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

RSS_FEED = {'bbc': 'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml',
            'abc': 'http://feeds.abcnews.com/abcnews/topstories'}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEED[publication])
    return render_template("home.html", articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)