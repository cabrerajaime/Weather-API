from flask import Flask, render_template

app = Flask("website")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def temperature(station, date):
    temp = 23
    return {"station": station,
            "date": date,
            "temperature": temp}


app.run(debug=True)
