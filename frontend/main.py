from frontend.Application import Application
from backend.main import saveLevel

def launch_paperpelle_game():
    saveLevel(1, 1, 1, 1)
    app = Application()
    app.run()

if __name__ == "main":
    launch_paperpelle_game()

launch_paperpelle_game()