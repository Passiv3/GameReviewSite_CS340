from flask import Flask, render_template
import os

# Configuration

app = Flask(__name__)

# Routes 



@app.route('/')
def root():
    return render_template("index.html")

@app.route('/games')
def gamePage():
    return render_template("games.html")

@app.route('/developers')
def developerPage():
    return render_template("developers.html")

@app.route('/genres')
def genrePage():
    return render_template("genres.html")

@app.route('/reviewers')
def reviewerPage():
    return render_template("reviewers.html")

@app.route('/reviews')
def reviewsPage():
    return render_template("reviews.html")

# Listener


if __name__ == "__main__":
    # Port is second argument here
    port = int(os.environ.get('PORT', 59123)) 
    
    app.run(port=port, debug = True) 

Games =
[
{
    "game_id": "1",
    "Developers_developer_id": 1,
    "game_name": "Need for Speed Heat",
    "release_date": "2019-11-08"
}
]

Developers = 
[
{
    "developer_id": "1"
    "developer_name": "Ghost Games"
}
]

Reviews = 
[
{
    "review_id": "1"
    "Games_games_id": "1"
    "Reviewers_reviewer_id": "1"
    "review_date": "rating"
}
]

Reviewers =
[
{
    "reviewer_id": "1"
    "reviewer_name": "Gamecritic"
    "number_of_review": 2
}
]

GameGenres = 
[
{
    "Games_game_id" = "1"
    "Genres_genre_id" = "1"
}
]    
Genres = 
[
{
    "genre_id": "1"
    "game_genre": "Racing"
}
]
