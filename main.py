from flask import Flask, render_template, request
import requests
from _datetime import datetime

app = Flask(__name__)
response_data = requests.get(url="https://api.npoint.io/4838401e9cf90d7797de").json()
today = datetime.today()


@app.route('/')
def get_all_posts():
    return render_template("index.html", data=response_data, date=today)


@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in response_data:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == '__main__':
    app.run(debug=True)

