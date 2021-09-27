from flask import Flask

app = Flask(__name__)

@app.route("/<int:code>")
def index(code):

    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)

