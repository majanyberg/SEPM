from integration_backend import storage

word_fetch_limit = 20
time_fetch_limit = 96
difficulties = ['EASY', 'MEDIUM', 'HARD']
categories = ['food', 'furniture', 'clothing', 'mixed']

def get_words(category: str, difficulty: str, count=5) -> list:
    difficulty = difficulty.upper()

    if difficulty not in difficulties:
        print("Error: Invalid difficulty level.")
        return
    
    if category not in categories:
        print("Error: Invalid category.")
        return

    if count < 1:
        print("Error: Invalid count.")
        return

    if count > word_fetch_limit:
        print(f"Warning: Requested {count} words, but the limit is {word_fetch_limit}. Returning maximum amount.")
        count = word_fetch_limit
    words = storage.get_words(category, difficulty, count)
    return words

def get_times(difficulty: str, count=5) -> list:
    difficulty = difficulty.upper()

    if difficulty not in difficulties:
        print("Error: Invalid difficulty level.")
        return

    if count < 1:
        print("Error: Invalid count.")
        return

    if count > time_fetch_limit:
        print(f"Warning: Requested {count} times, but the limit is {time_fetch_limit}. Returning maximum amount.")
        count = time_fetch_limit
    times = storage.get_times(difficulty, count)
    return times


def update_score(username: str, score: int) -> None:
    try: 
        user_profile = storage.get_user_profile(username)
    except Exception as e:
        print(f"User profile not found. Error: {e}")
        return

    try:
        user_profile["score"] += score
    except Exception as e:
        print(f"User profile missing required fields. Error: {e}")
        return
    
    storage.update_user_profile(username, user_profile)