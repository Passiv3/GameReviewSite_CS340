from flask import Flask, render_template
import os

# Configuration

app = Flask(__name__)

# Routes 



@app.route('/')
def root():
    return render_template("games.j2", people = people_from_app_py)

# Listener

people_from_app_py =[
{
    "name": "Thomas",
    "age": 33,
    "location": "New Mexico",
    "favorite_color": "Blue"
},
{
    "name": "Gregory",
    "age": 41,
    "location": "Texas",
    "favorite_color": "Red"
},
{
    "name": "Vincent",
    "age": 27,
    "location": "Ohio",
    "favorite_color": "Green"
},
{
    "name": "Alexander",
    "age": 29,
    "location": "Florida",
    "favorite_color": "Orange"
}]

if __name__ == "__main__":
    # Port is second argument here
    port = int(os.environ.get('PORT', 59123)) 
    
    app.run(port=port, debug = True) 