
from flask import Flask, jsonify, request
from pymongo import MongoClient
import csv
import os
import random  

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['movie_recommendations']

#happy content collection
happy_movies_collection = db['happy_movies']
happy_songs_collection=db['happy_songs']
happy_books_collection=db['happy_books']



#sad content collection
sad_movies_collection = db['sad_movies']
sad_books_collection = db['sad_books']
sad_songs_collection = db['sad_songs']

# Function to load CSV data into MongoDB
def load_csv_data():
    
    happy_movies_collection.delete_many({})
    happy_books_collection.delete_many({})
    happy_songs_collection.delete_many({})
    sad_movies_collection.delete_many({})
    
    # Load happy content
    if os.path.exists('Happy.csv'):
        with open('Happy.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)  
            movie_list = []
            for row in csv_reader:
                if row:  
                    movie_list.append({"title": row[0]})  
            
            if movie_list:
                happy_movies_collection.insert_many(movie_list)
                print(f"Loaded {len(movie_list)} happy movies")


    if os.path.exists('Happy Songs.csv'):
        with open('Happy Songs.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)  
            movie_list = []
            for row in csv_reader:
                if row:  
                    movie_list.append({"title": row[0]})  
            
            if movie_list:
                happy_songs_collection.insert_many(movie_list)
                print(f"Loaded {len(movie_list)} Happy Songs")

    if os.path.exists('Happy Books.csv'):
        with open('Happy Books.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)  
            movie_list = []
            for row in csv_reader:
                if row:  
                    movie_list.append({"title": row[0]})  
            
            if movie_list:
                happy_books_collection.insert_many(movie_list)
                print(f"Loaded {len(movie_list)} Happy Books")

    #load sad content
    if os.path.exists('Sad.csv'):
        with open('Sad.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)  
            movie_list = []
            for row in csv_reader:
                if row:  
                    movie_list.append({"title": row[0]})  
            
            if movie_list:
                sad_movies_collection.insert_many(movie_list)
                print(f"Loaded {len(movie_list)} sad movies")

    if os.path.exists('Sad Songs.csv'):
        with open('Sad Songs.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)  
            movie_list = []
            for row in csv_reader:
                if row:  
                    movie_list.append({"title": row[0]})  
            
            if movie_list:
                sad_songs_collection.insert_many(movie_list)
                print(f"Loaded {len(movie_list)} sad songs")

    if os.path.exists('Sad books.csv'):
        with open('Sad books.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)  
            movie_list = []
            for row in csv_reader:
                if row:  
                    movie_list.append({"title": row[0]})  
            
            if movie_list:
                sad_books_collection.insert_many(movie_list)
                print(f"Loaded {len(movie_list)} sad  books")
    
   
    if os.path.exists('Sad.csv'):
        with open('Sad.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)  # Simple CSV reader
            movie_list = []
            for row in csv_reader:
                if row: 
                    movie_list.append({"title": row[0]})  
            
            if movie_list:
                sad_movies_collection.insert_many(movie_list)
                print(f"Loaded {len(movie_list)} sad movies")

# API routes

@app.route('/api/movies/random/<mood>', methods=['GET'])
def get_random_mood_movie(mood):
    if mood.lower() == 'happy':
        movies = list(happy_movies_collection.find({}, {'_id': 0}))
        if movies:
            random_movie = random.choice(movies)
            return jsonify(random_movie["title"])
        return jsonify({"error": "No happy movies found"}), 404
    
    elif mood.lower() == 'sad':
        movies = list(sad_movies_collection.find({}, {'_id': 0}))
        if movies:
            random_movie = random.choice(movies)
            return jsonify(random_movie["title"])
        return jsonify({"error": "No sad movies found"}), 404
    
    else:
        return jsonify({"error": "Invalid mood. Choose 'happy' or 'sad'"}), 400
    


@app.route('/api/books/random/happy')
def happybook():
    books=list(happy_books_collection.find({},{'_id':0}))
    if books:
        show=random.choice(books)
        return jsonify(show["title"])

@app.route('/api/movies/refresh', methods=['POST'])
def refresh_movies():
    load_csv_data()
    return jsonify({"status": "success", "message": "Movie database refreshed"})

if __name__ == '__main__':
    
    load_csv_data()
    app.run(debug=True)



