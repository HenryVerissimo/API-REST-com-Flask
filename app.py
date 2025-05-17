from app import app, db

@app.route("/")
def index():
    return "Hello World!"


if __name__ == "__main__":

    app.run(debug=True)