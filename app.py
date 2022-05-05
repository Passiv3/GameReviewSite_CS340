from flask import Flask, render_template
import os

# Configuration

app = Flask(__name__, template_folder='templates')

# Routes 

# Temporary hardcoded data for step 2, these will be replaced with calls to a db in the next step
Games = [
{
    "game_id": "1",
    "Developers_developer_id": 1,
    "game_name": "Need for Speed Heat",
    "release_date": "2019-11-08"
},
{
    "game_id": "2",
    "Developers_developer_id": 2,
    "game_name": "Counter Strike: Global Offensive",
    "release_date": "2012-08-21"
},
{
    "game_id": "3",
    "Developers_developer_id": 3,
    "game_name": "Monster Hunter: World",
    "release_date": "2018-08-09"
},
{
    "game_id": "4",
    "Developers_developer_id": 3,
    "game_name": "Devil May Cry V",
    "release_date": "2019-03-08"
},
{
    "game_id": "5",
    "Developers_developer_id": 4,
    "game_name": "Death Stranding",
    "release_date": "2019-11-08"
},
]

Developers = [
{
    "developer_id": "1",
    "developer_name": "Ghost Games"
},
{
    "developer_id": "2",
    "developer_name": "Valve"
},
{
    "developer_id": "3",
    "developer_name": "CAPCOM"
},
{
    "developer_id": "4",
    "developer_name": "Kojima Production"
}
]

Reviews = [
{
    "review_id": "1",
    "Games_games_id": "1",
    "Reviewers_reviewer_id": "1",
    "review_date": "2020-10-14",
    "rating": "6",
    "review_content": "This game is gas"
},
{
    "review_id": "2",
    "Games_games_id": "2",
    "Reviewers_reviewer_id": "1",
    "review_date": "2017-12-11",
    "rating": "7",
    "review_content": "This game is pretty good, but the matchmaking is terrible"
},
{
    "review_id": "3",
    "Games_games_id": "3",
    "Reviewers_reviewer_id": "1",
    "review_date": "2019-08-19",
    "rating": "9",
    "review_content": "The music and gameplay is awesome, classic Monster Hunter gameplay"
},
{
    "review_id": "4",
    "Games_games_id": "3",
    "Reviewers_reviewer_id": "1",
    "review_date": "2019-10-25",
    "rating": "8",
    "review_content": "Excellent entry of Monster Hunter"
},
{
    "review_id": "5",
    "Games_games_id": "1",
    "Reviewers_reviewer_id": "1",
    "review_date": "2019-10-25",
    "rating": "8",
    "review_content": "Smokin Sexy Style! The action for the long awaited sequel was worth the wait!"
},
{
    "review_id": "6",
    "Games_games_id": "5",
    "Reviewers_reviewer_id": "2",
    "review_date": "2017-12-11",
    "rating": "7",
    "review_content": "Very interesting game by Hideo Kojima"
},

]

Reviewers =[
{
    "reviewer_id": "1",
    "reviewer_name": "Gamecritic",
    "number_of_review": 2
},
{
    "reviewer_id": "2",
    "reviewer_name": "IGN",
    "number_of_review": 2
},
{
    "reviewer_id": "3",
    "reviewer_name": "Gamespot",
    "number_of_review": 2
}
]

GameGenres = [
{
    "Games_game_id" : "1",
    "Genres_genre_id" : "1"
}
]

Genres = [
{
    "genre_id": "1",
    "game_genre": "Racing"
},
{
    "genre_id": "2",
    "game_genre": "FPS"
},
{
    "genre_id": "3",
    "game_genre": "Shooter"
},
{
    "genre_id": "4",
    "game_genre": "Adventure"
},
{
    "genre_id": "5",
    "game_genre": "Hack-And-Slash"
},
{
    "genre_id": "6",
    "game_genre": "Action"
},
]

GamesGenre = [
{
    "Games_game_id": "1",
    "Genres_genres_id": "1"
}
]

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/games')
def gamePage():
    return render_template("games.html", games = Games, developers = Developers)

@app.route('/developers')
def developerPage():
    return render_template("developers.html", developers = Developers)

@app.route('/genres')
def genrePage():
    return render_template("genres.html", genres = Genres)

@app.route('/reviewers')
def reviewerPage():
    return render_template("reviewers.html", reviewers = Reviewers)

@app.route('/reviews')
def reviewsPage():
    return render_template("reviews.html", reviews = Reviews, games = Games, reviewers = Reviewers)

@app.route('/gameGenres')
def gameGenres():
    return render_template("gameGenres.html", gameGenres = GamesGenre, games = Games, genres = Genres)

@app.route('/about')
def about():
    return render_template("about.html")
# Listener


if __name__ == "__main__":
    # Port is second argument here
    port = int(os.environ.get('PORT', 59129)) 
    
    app.run(port=port, debug = True) 
