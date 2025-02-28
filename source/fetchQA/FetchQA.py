import requests
import random
import json

BACKEND_URL = ""  # TODO: fill in correct URL


def load_questions_temp(file_path='questions.json'):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def fetch_qa_temp(lvl):
    questions = load_questions_temp()
    if lvl in questions and questions[lvl]:
        return random.choice(questions[lvl])
    else:
        return {'No questions available'}


def fetch_questions_from_backend(level):
    """
    Fetches all questions for a specific level from the backend.
    """
    try:
        response = requests.get(f'{BACKEND_URL} level={level}', timeout=5)  # TODO: is the level chosen here?
        if response.status_code == 200:  # TODO: check actual value with backend team
            data = response.json()
            return data.get('questions', [])
    except requests.RequestException as e:
        print(f'An error occurred while fetching questions: {e}')
        return []


def generate_random_question(level):
    """
    Randomly selects a question for the specific level.
    """
    questions = fetch_questions_from_backend(level)
    if questions:
        return random.choice(questions)
    else:
        return {'No questions available'}
