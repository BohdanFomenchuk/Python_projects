import requests

all_data = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean")
all_data.raise_for_status()
question_data = all_data.json()["results"]