import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")
# Add tlsAllowInvalidCertificates to bypass Windows OpenSSL handshake mismatch
client = MongoClient(MONGO_URI, tlsAllowInvalidCertificates=True)
db = client.get_database("student_assignment_db")
collection = db.user_submissions

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    user_name = request.form.get("name")
    user_email = request.form.get("email")
    user_message = request.form.get("message")

    submission_data = {
        "name": user_name,
        "email": user_email,
        "message": user_message
    }
    collection.insert_one(submission_data)

    return render_template("success.html", name=user_name)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)