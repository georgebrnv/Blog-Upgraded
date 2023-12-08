from flask import Flask, render_template
import requests
from _datetime import datetime

app = Flask(__name__)
response_data = requests.get(url="https://api.npoint.io/4838401e9cf90d7797de").json()
today = datetime.today()


@app.route('/')
def get_all_posts():
    return render_template("index.html", data=response_data, date=today)


@app.route('/templates/about.html')
def about():
    return render_template("about.html")


@app.route('/templates/contact.html')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in response_data:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)

