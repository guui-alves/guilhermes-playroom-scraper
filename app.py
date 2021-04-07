import random
from flask import Flask, jsonify, request
from flask_cors import CORS
from omelete_scraper import OmeleteScraper
from gamespot_scraper import GamespotScraper

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/news')
def get_news():
  omelete = OmeleteScraper()
  gamespot = GamespotScraper()

  omelete_news = omelete.get_omelete_news()
  gamespot_news = gamespot.get_gamespot_news()

  news = omelete_news + gamespot_news
  random.shuffle(news)

  return jsonify({'news': news}), 200

app.run()