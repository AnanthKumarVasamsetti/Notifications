from flask import Flask
from BSE_scrapper import scrape

app = Flask(__name__)

@app.route('/')
def start_server():
    return 'Congrats successfully deployed two processes'

if __name__ == '__main__':
    app.run()