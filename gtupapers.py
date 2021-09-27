from flask import Flask, jsonify
import json

from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Please enter subject code after slash"

@app.route("/<int:code>")
def papers(code):
    papers = {
        "w20": f"https://www.gtu.ac.in/uploads/W2020/BE/{code}.pdf",
        "w19": f"https://www.gtu.ac.in/uploads/W2019/BE/{code}.pdf",
        "s21": f"https://www.gtu.ac.in/uploads/S2021/BE/{code}.pdf",
        "s20": f"https://www.gtu.ac.in/uploads/S2020/BE/{code}.pdf"
    }
    return jsonify(papers)

if __name__ == '__main__':
    app.run(debug=True)