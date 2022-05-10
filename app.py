from flask import Flask, render_template, json
from flask_mysqldb import MySQL
from flask import request
import database.db_connector as db
import os

# Configuration

app = Flask(__name__, template_folder='templates')

#database connection
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_chundann"
app.config["MYSQL_PASSWORD"] = "8473"
app.config["MYSQL_DB"] = "cs340_chundann"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

db_connection = db.connect_to_database()
mysql = MySQL(app)

# Routes 
@app.route('/')
def root():
    return render_template("index.html")

@app.route('/games')
def gamePage():
    gameQuery = "SELECT * FROM Games"
    gameCursor = db.execute_query(db_connection=db_connection, query = gameQuery)
    Games = gameCursor.fetchall()

    devQuery = "SELECT * FROM Developers"
    devCursor = db.execute_query(db_connection=db_connection, query = devQuery)
    Developers = devCursor.fetchall()

    return render_template("games.html", games = Games, developers = Developers)

@app.route('/developers')
def developerPage():
    devQuery = "SELECT * FROM Developers"
    devCursor = db.execute_query(db_connection=db_connection, query = devQuery)
    Developers = devCursor.fetchall()
    return render_template("developers.html", developers = Developers)

@app.route('/genres')
def genrePage():
    genreQuery = "SELECT * FROM Genres"
    genreCursor = db.execute_query(db_connection=db_connection, query = genreQuery)
    Genres = genreCursor.fetchall()
    return render_template("genres.html", genres = Genres)

@app.route('/reviewers')
def reviewerPage():
    reviewerQuery = "SELECT * FROM Reviewers"
    reviewerCursor = db.execute_query(db_connection=db_connection, query = reviewerQuery)
    Reviewers = reviewerCursor.fetchall()

    return render_template("reviewers.html", reviewers = Reviewers)

@app.route('/delrev/<int:id>')
def deletePage():
    query = "DELETE FROM review WHERE id = '%s'"

    return render_template("delete.html")

@app.route('/editrev/<int:id>')
def editPage():
    return render_template("edit.html")

@app.route('/reviews')
def reviewsPage():
    gameQuery = "SELECT * FROM Games"
    gameCursor = db.execute_query(db_connection=db_connection, query = gameQuery)
    Games = gameCursor.fetchall()

    reviewerQuery = "SELECT * FROM Reviewers"
    reviewerCursor = db.execute_query(db_connection=db_connection, query = reviewerQuery)
    Reviewers = reviewerCursor.fetchall()

    reviewQuery = "SELECT * FROM Reviews"
    reviewCursor = db.execute_query(db_connection=db_connection, query = reviewQuery)
    Reviews = reviewCursor.fetchall()
    return render_template("reviews.html", reviews = Reviews, games = Games, reviewers = Reviewers)

@app.route('/gameGenres')
def gameGenres():
    gameGenreQuery = "SELECT * FROM GameGenres"
    gameGenreCursor = db.execute_query(db_connection=db_connection, query = gameGenreQuery)
    GameGenres = gameGenreCursor.fetchall()

    gameQuery = "SELECT * FROM Games"
    gameCursor = db.execute_query(db_connection=db_connection, query = gameQuery)
    Games = gameCursor.fetchall()

    genreQuery = "SELECT * FROM Genres"
    genreCursor = db.execute_query(db_connection=db_connection, query = genreQuery)
    Genres = genreCursor.fetchall()

    return render_template("gameGenres.html", gameGenres = GameGenres, games = Games, genres = Genres)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/search')
def search():
    searchquery = "SELECT Reviews.review_id, Genres.game_genre, Games.game_name FROM Reviews INNER JOIN GameGenres ON Reviews.game_id = GameGenres.game_id INNER JOIN Genres ON GameGenres.genre_id = Genres.genre_id INNER JOIN Games ON Reviews.game_id = Games.game_id"
    return render_template("search.html")

# Listener
if __name__ == "__main__":
    # Port is second argument here
    port = int(os.environ.get('PORT', 59129)) 
    
    app.run(port=port, debug = True) 
