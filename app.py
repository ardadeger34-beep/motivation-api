
from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    {
        "q": "Believe you can and you're halfway there.", 
        "a": "Theodore Roosevelt"
    },
    {
        "q": "Small daily improvements over time lead to stunning results.", 
        "a": "Robin Sharma"
    },
    {
        "q": "never give up", 
        "a": "Nike"
    },
    {
        "q": "You are stronger than you think. One step at a time.", 
        "a": "Unknown"
    },
    {
        "q": "time is money", 
        "a": "arda deger"
    }
]


@app.route('/quote')
def get_quote():
    
    return jsonify([random.choice(quotes)])

if __name__ == '__main__':
    app.run(debug=True)
