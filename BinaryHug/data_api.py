# app.py
from flask import Flask, request, jsonify
import random
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Connection
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['movie_recommendations']  


def get_random_item(collection_name):
    collection = db[collection_name]
    count = collection.count_documents({})
    if count > 0:
        random_item = collection.find().limit(1).skip(random.randint(0, count - 1))
        return next(random_item, {}).get('title', f'No recommendation available from {collection_name}')
    return f'No recommendation available from {collection_name}'

# Happy mood routes
@app.route('/api/happy/books', methods=['GET'])
def happy_books():
    book = get_random_item('happy_books')
    return jsonify({"mood": "happy", "type": "book", "recommendation": book})

@app.route('/api/happy/movies', methods=['GET'])
def happy_movies():
    movie = get_random_item('happy_movies')
    return jsonify({"mood": "happy", "type": "movie", "recommendation": movie})

@app.route('/api/happy/songs', methods=['GET'])
def happy_songs():
    song = get_random_item('happy_songs')
    return jsonify({"mood": "happy", "type": "song", "recommendation": song})

# Sad mood routes
@app.route('/api/sad/books', methods=['GET'])
def sad_books():
    book = get_random_item('sad_books')
    return jsonify({"mood": "sad", "type": "book", "recommendation": book})

@app.route('/api/sad/movies', methods=['GET'])
def sad_movies():
    movie = get_random_item('sad_movies')
    return jsonify({"mood": "sad", "type": "movie", "recommendation": movie})

@app.route('/api/sad/songs', methods=['GET'])
def sad_songs():
    song = get_random_item('sad_songs')
    return jsonify({"mood": "sad", "type": "song", "recommendation": song})



#route if mood is neutral
@app.route('/api/neutral/books', methods=['GET'])
def neut_books():
    book = get_random_item('happy_books')
    return jsonify({"mood": "neutral", "type": "book", "recommendation": book})

@app.route('/api/neutral/movies', methods=['GET'])
def neut_movies():
    movie = get_random_item('happy_movies')
    return jsonify({"mood": "neutral", "type": "movie", "recommendation": movie})

@app.route('/api/neutral/songs', methods=['GET'])
def neut_songs():
    song = get_random_item('happy_songs')
    return jsonify({"mood": "neutral", "type": "song", "recommendation": song})


if __name__ == '__main__':
    app.run(debug=True, port=5000)