from flask import Flask, render_template, request

app = Flask(__name__)

@app.context_processor
def inject_request():
    return dict(request=request)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/events")
def events():
    return render_template("events.html")

if __name__ == "__main__":
    app.run(debug=True)