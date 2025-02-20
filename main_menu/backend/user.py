def get_user_profile():
    """Get the active user profile

    :return: A dictionary containing key-value pairs. Example: { "first_name": "Alex", "last_name": "Smith", "age": 25 }
    """
    return {
        "first_name": "Alex",
        "last_name": "Smith",
        "age": 25,
        "country": "Luxembourg"
    }

def update_user_profile(user_profile: dict):
    """Update the user profile

    :param user_profile: A dictionary containing user profile information
    """
    pass

def get_user_stats():
    """Get user statistics

    :return: A dict containing the user statistics
    """
    return {
        "completed_games": 17,
        "score": 124
    }

def update_user_stats(stats: dict):
    """Update the user statistics

    :param stats: The number of completed games
    """
    pass
