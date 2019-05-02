from flask import Flask
from BSE_scrapper import scrape

app = Flask(__name__)

@app.route('/')
def hello():
    scrape()

if __name__ == '__main__':
    app.run()