from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return {"message": "Hello, Platform!"}

if __name__ == "__main__":
    # In production, a WSGI server like Gunicorn would run this
    app.run(host="0.0.0.0", port=8080)
