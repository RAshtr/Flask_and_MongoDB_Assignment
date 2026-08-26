# Flask and MongoDB Atlas Web Application

This is my assignment project for creating a basic Flask web application connected to MongoDB Atlas, containerized using Docker, and automated using GitHub Actions.

## Repository Link
* GitHub: https://github.com/RAshtr/flask_mongodb_assignment

## Features Built
* Simple Flask web server with form handling.
* Storing form submissions (Name, Email, Message) directly in MongoDB Atlas.
* Managed database connection strings securely using `.env` and `python-dotenv`.
* Dockerized the application using a lightweight Python image.
* Setup a basic CI workflow in GitHub Actions to test syntax and dependencies on push.

## Project Structure
```text
flask_mongodb_assignment/
├── .github/
│   └── workflows/
│       └── ci.yml
├── templates/
│   ├── form.html
│   └── success.html
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── app.py
└── requirements.txt