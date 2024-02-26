from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def index():
    return "flask is running"
