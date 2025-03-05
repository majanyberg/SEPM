# Backend

This is the repository for the backend module


# API

This is the interface module. All backend functionality is called upon through this module.

## User Management
```python
# Retrieves all user information for the specified user.
get_user(username: str) -> dict

# Creates a new user entry in the database.
create_user(username: str, real_name: str = None, age: int = 0, 
                country: str = None, user_type: str = None, 
                total_time: int = 0, words_learned: int = 0) -> None

# Deletes a user from the database.
delete_user(username: str) -> None
```
To use these functions, import sessionmanager.
This is used in order to avoid global variables.
```python
# Logs in a user and tracks session start time.
session_manager.login(username: str) -> str

# Logs out the current user and updates total time spent.
session_manager.logout() -> None

# Returns the currently logged-in user.
session_manager.get_current_user() -> str
```
```python
# Updates a specific entry in the current logged-in user's database record.
update_cur_user(column: str, value) -> None

# Retrieves statistics of the currently logged-in user.
get_cur_user_stats() -> dict

# Increases the words learned stat for the logged-in user.
increase_words_learned(value: int) -> None

# Retrieves the words learned stat of the logged-in user.
get_words_learned() -> int

# Updates the game state for the currently logged-in user in the database.
store_game_state(json_string: str) -> None

# Retrieves the game state from the database for the currently logged-in user.
get_game_state() -> dict
```
