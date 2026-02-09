from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Gemini TeamSync</h1><p>The Unified Team Hub is Active!</p>"

if __name__ == "__main__":
    app.run()
