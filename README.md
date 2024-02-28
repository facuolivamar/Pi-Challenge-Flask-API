# Challenge Python - Interview

This repository contains the Flask API for the "Challenge Python - Interview".

- [Challenge Python .docx](https://github.com/facuolivamar/Pi-Challenge-Flask-API/blob/main/docs/Challenge_Python_-_Interview_(1).docx)

## Running the API with Docker

To start running the Flask API with Docker, follow these steps:

1. Run the command: `docker build -t challenge-python-flask-api .`
2. Run the command: `docker run -dp 5000:5000 challenge-python-flask-api` (running in the background)

## Running the API with Python

Alternatively, if you prefer to run the API with Python, proceed as follows:

1. Activate the Pipenv shell with: `pipenv shell`
2. Install the required dependencies using: `pip install -r requirements.txt`
3. Navigate to the app directory
4. Optionally, initialize the database with: `flask db init`
5. Optionally, perform migrations with: `flask db migrate`
6. Optionally, upgrade the database with: `flask db upgrade`
7. Start the Flask server with: `flask run`
8. If you wish to execute tests, navigate to the tests directory and run: `pytest`

## API Documentation

You can access the API documentation by visiting [http://127.0.0.1:5005/swagger-ui](http://127.0.0.1:5005/swagger-ui) in your browser.

## API Testing with Postman

For API testing, you can utilize the provided Postman collection "[Challenge Python - Interview](https://www.postman.com/payload-geologist-60335199/workspace/challenge-python-interview/overview)". This collection covers all procedures outlined in the Character folder description.
