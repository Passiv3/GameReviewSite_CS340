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
    db_connection = db.connect_to_database()
    query = "DELETE FROM Reviews WHERE review_id = '%s';" %(id)
    cur = db.execute_query(db_connection = db_connection, query = query)
    
    return render_template("delete.html")

@app.route('/editrev/<int:id>', methods = ["POST", "GET"])
def editPage(id):
    db_connection = db.connect_to_database()
    if request.method == "GET":
        query = "SELECT * FROM Reviews WHERE review_id = %s" %(id)
        cursor = db.execute_query(db_connection=db_connection, query = query)
        nowEditing = cursor.fetchall()

    if request.method == "POST":
        newRating = request.form["rating"]
        newContent = request.form["review_content"]
        newDate = request.form["review_date"]
        query = "UPDATE Reviews SET review_date = '%s', rating = '%s', review_content = '%s' WHERE review_id = '%s'" %(newDate, newRating, newContent, id)
        cur = db.execute_query(db_connection = db_connection, query = query)
        return redirect("/reviews")

    return render_template("edit.html", edit = nowEditing)

@app.route('/reviews', methods = ["POST", "GET"])
def reviewsPage():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        gameQuery = "SELECT * FROM Games"
        gameCursor = db.execute_query(db_connection=db_connection, query = gameQuery)
        Games = gameCursor.fetchall()

        reviewerQuery = "SELECT * FROM Reviewers"
        reviewerCursor = db.execute_query(db_connection=db_connection, query = reviewerQuery)
        Reviewers = reviewerCursor.fetchall()

        genreQuery = "SELECT * FROM Genres"
        genreCursor = db.execute_query(db_connection=db_connection, query = genreQuery)
        Genres = genreCursor.fetchall()

        reviewQuery = """SELECT review_id, game_name, reviewer_name, review_date, rating, review_content
                        FROM Reviews
                        JOIN Games on Games.game_id = Reviews.game_id
                        JOIN Reviewers on Reviewers.reviewer_id = Reviews.reviewer_id;"""
        reviewCursor = db.execute_query(db_connection=db_connection, query = reviewQuery)
        Reviews = reviewCursor.fetchall()
        return render_template("reviews.html", reviews = Reviews, games = Games, reviewers = Reviewers, genres = Genres)

    if request.method == "POST":
        if request.form.get("add_review"):
            game_id = request.form["gameID"]
            reviewer_id = request.form["reviewerID"]
            contents = request.form["review_content"]
            date = request.form["review_date"]
            rating = request.form["rating"]

            query = """INSERT INTO Reviews (game_id, reviewer_id, review_date, rating, review_content)
                        VALUES ('%s','%s','%s','%s','%s')""" %(game_id, reviewer_id, date, rating, contents)
            cur = db.execute_query(db_connection = db_connection, query = query)
            return redirect("/reviews")
        
        if request.form.get("apply_filter"):
            genre_id = request.form["genre"]
            gameQuery = "SELECT * FROM Games"
            gameCursor = db.execute_query(db_connection=db_connection, query = gameQuery)
            Games = gameCursor.fetchall()

            reviewerQuery = "SELECT * FROM Reviewers"
            reviewerCursor = db.execute_query(db_connection=db_connection, query = reviewerQuery)
            Reviewers = reviewerCursor.fetchall()

            genreQuery = "SELECT * FROM Genres"
            genreCursor = db.execute_query(db_connection=db_connection, query = genreQuery)
            Genres = genreCursor.fetchall()

            reviewQuery = """SELECT review_id, game_name, reviewer_name, review_date, rating, review_content
                            FROM Reviews
                            JOIN Games on Games.game_id = Reviews.game_id
                            JOIN Reviewers on Reviewers.reviewer_id = Reviews.reviewer_id
                            INNER JOIN GameGenres ON Reviews.game_id = GameGenres.game_id
                            INNER JOIN Genres ON GameGenres.genre_id = Genres.genre_id
                            WHERE GameGenres.genre_id = '%s';""" %(genre_id)
            reviewCursor = db.execute_query(db_connection=db_connection, query = reviewQuery)
            Reviews = reviewCursor.fetchall()
            return render_template("reviews.html", reviews = Reviews, games = Games, reviewers = Reviewers, genres = Genres)

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

# Listener
if __name__ == "__main__":
    # Port is second argument here
    port = int(os.environ.get('PORT', 59123)) 
    
    app.run(port=port, debug = True) 
