from flask import Flask, render_template
import os

# Configuration

app = Flask(__name__)

# Routes 



@app.route('/')
def root():
    return render_template("index.html")

# Listener


if __name__ == "__main__":
    # Port is second argument here
    port = int(os.environ.get('PORT', 59123)) 
    
    app.run(port=port, debug = True) 