from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    results = {
        "most_positive": "I love this product, it's amazing!",
        "most_negative": "This is terrible, I hate it.",
        "segments": [
            {"window": 1, "score": 5},
            {"window": 2, "score": -2},
            {"window": 3, "score": 1}
        ]
    }
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

