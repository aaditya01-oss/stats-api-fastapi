Stats API (FastAPI)

Simple FastAPI service that calculates mean, variance, and standard deviation for a list of numbers.

Run locally
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn
uvicorn main:app --reload
API Usage
POST /calculate/

Example request:

{"numbers": [10, 20, 30, 40]}
Example response:

{"mean": 25.0, "variance": 125.0, "standard_deviation": 11.1803398875}
