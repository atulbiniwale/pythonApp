from flask import Flask, render_template

app = Flask(__name__, static_url_path="", static_folder="static")


@app.route("/") #create page on this first url
def homePage():
  return render_template("homepage.html")


app.run(host="0.0.0.0")