user_profiles = []

def get_user_profile():
    """Get the active user profile

    :return: A dictionary containing key-value pairs. Example: { "username": alexsmith, "first_name": "Alex", "last_name": "Smith", "age": 25 }
    """
    return {
        "username": "alexsmith",
        "first_name": "Alex",
        "last_name": "Smith",
        "age": 25,
        "country": "Luxembourg"
    }

def add_user_profile(user_profile_data):
    """Lägg till en användarprofil till listan user_profiles"""
    global user_profiles  # Ensure we modify the global list
    user_profiles.append(user_profile_data)
    print(f"Added user profile: {user_profile_data}")  
    print(f"Current user profiles: {user_profiles}")  

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
