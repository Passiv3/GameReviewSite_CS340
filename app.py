from flask import Flask, render_template, json, request, redirect
from flask_mysqldb import MySQL
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
    db_connection = db.connect_to_database()
    return render_template("index.html")

@app.route('/games', methods = ["POST", "GET"])
def gamePage():
    db_connection = db.connect_to_database()

    if request.method == "GET":
        gameQuery = """SELECT game_id, developer_name, game_name, release_date
                    FROM Games 
                    LEFT JOIN Developers
                    ON Games.developer_id = Developers.developer_id;"""
        gameCursor = db.execute_query(db_connection=db_connection, query = gameQuery)
        Games = gameCursor.fetchall()

        devQuery = "SELECT * FROM Developers"
        devCursor = db.execute_query(db_connection=db_connection, query = devQuery)
        Developers = devCursor.fetchall()
    
    if request.method == "POST":
        game_name = request.form["game_name"]
        developer_id = request.form["developer"]
        releaseDate = request.form["release_date"]
        query = """INSERT INTO Games (developer_id, game_name, release_date) 
                VALUES ('%s', '%s', '%s')""" %(developer_id, game_name, releaseDate)
        cur = db.execute_query(db_connection = db_connection, query = query)
        return redirect("/games")

    return render_template("games.html", games = Games, developers = Developers)

@app.route('/developers', methods = ["POST", "GET"])
def developerPage():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        devQuery = "SELECT * FROM Developers ORDER BY developer_id"
        devCursor = db.execute_query(db_connection=db_connection, query = devQuery)
        Developers = devCursor.fetchall()
    
    if request.method == "POST":
        developer_name = request.form["developer_name"]
        query = "INSERT INTO Developers (developer_name) VALUES ('%s')" %(developer_name)
        cur = db.execute_query(db_connection = db_connection, query = query)
        return redirect("/developers")
        
    return render_template("developers.html", developers = Developers)

@app.route('/genres', methods = ["POST", "GET"])
def genrePage():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        genreQuery = "SELECT * FROM Genres"
        genreCursor = db.execute_query(db_connection=db_connection, query = genreQuery)
        Genres = genreCursor.fetchall()
    
    if request.method == "POST":
        genre_name = request.form["game_genre"]
        query = "INSERT INTO Genres (game_genre) VALUES ('%s')" %(genre_name)
        cur = db.execute_query(db_connection = db_connection, query = query)
        return redirect("/genres")

    return render_template("genres.html", genres = Genres)

@app.route('/reviewers', methods = ["POST", "GET"])
def reviewerPage():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        reviewerQuery = "SELECT * FROM Reviewers"
        reviewerCursor = db.execute_query(db_connection=db_connection, query = reviewerQuery)
        Reviewers = reviewerCursor.fetchall()
    
    if request.method == "POST":
        reviewer_name = request.form["name"]
        query = "INSERT INTO Reviewers (reviewer_name, number_of_review) VALUES ('%s', 0)" %(reviewer_name)
        cur = db.execute_query(db_connection, query = query)
        return redirect("/reviewers")

    return render_template("reviewers.html", reviewers = Reviewers)

@app.route('/delrev/<int:id>')
def deletePage(id):
    query = "DELETE FROM Reviews WHERE review_id = '%s';" %(id)
    cur = db.execute_query(db_connection = db_connection, query = query)
    
    return render_template("delete.html")

@app.route('/editrev/<int:id>')
def editPage(id):
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Reviews WHERE review_id = %s" %(id)
    cursor = db.execute_query(db_connection=db_connection, query = query)
    nowEditing = cursor.fetchall()
    return render_template("edit.html", edit = nowEditing)

@app.route('/reviews')
def reviewsPage():
    db_connection = db.connect_to_database()
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

@app.route('/gameGenres', methods = ["POST", "GET"])
def gameGenres():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        gameGenreQuery = """SELECT game_name, game_genre, GameGenres.game_id, GameGenres.genre_id
                            FROM GameGenres
                            JOIN Games on Games.game_id = GameGenres.game_id
                            JOIN Genres on Genres.genre_id = GameGenres.genre_id
                            ORDER BY game_name;"""
        gameGenreCursor = db.execute_query(db_connection=db_connection, query = gameGenreQuery)
        GameGenres = gameGenreCursor.fetchall()

        gameQuery = "SELECT game_id, game_name FROM Games"
        gameCursor = db.execute_query(db_connection=db_connection, query = gameQuery)
        Games = gameCursor.fetchall()

        genreQuery = "SELECT * FROM Genres"
        genreCursor = db.execute_query(db_connection=db_connection, query = genreQuery)
        Genres = genreCursor.fetchall()
    
    if request.method == "POST":
        gameID = request.form["GameName"]
        genreID = request.form["GenreName"]
        query = "INSERT INTO GameGenres (game_id, genre_id) VALUES ('%s', '%s')" %(gameID, genreID)
        cur = db.execute_query(db_connection = db_connection, query = query)
        return redirect("/gameGenres")

    return render_template("gameGenres.html", gameGenres = GameGenres, games = Games, genres = Genres)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/search')
def search():
    searchquery = """SELECT Reviews.review_id, Genres.game_genre, Games.game_name 
                    FROM Reviews 
                    INNER JOIN GameGenres ON Reviews.game_id = GameGenres.game_id INNER JOIN Genres ON GameGenres.genre_id = Genres.genre_id INNER JOIN Games ON Reviews.game_id = Games.game_id"""
    return render_template("search.html")

# Listener
if __name__ == "__main__":
    # Port is second argument here
    port = int(os.environ.get('PORT', 59123)) 
    
    app.run(port=port, debug = True) 
