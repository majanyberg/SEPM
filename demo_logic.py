from puzzle_logic.apis.logic import Logic
from puzzle_logic.model.category import Category
import time


def demo_gameplay():
    print("\n===== Demonstrating Gameplay =====")

    # Initialize the game
    print("\n🎮 Player selects FOOD category:")
    input("")

    logic = Logic()
    logic.init_player(3, 3, Category.FOOD)
    time.sleep(1)

    # Game starts with the following grid
    input("")
    print("\n🎮 Game starts with the following grid (includes words from FOOD category):\n")

    grid = logic.get_grid()

    #print(f'\nGrid = {logic.get_grid()}')
    for i in range(len(grid)):
        print(grid[i])

    # Player stats
    print("\n🎮 Player initial stats:")
    print(f'HP = {logic.get_hp()}')
    print(f'Hints left = {logic.get_hints_left()}')

    # Wrong move
    print("\n🎮 Player makes a wrong move:")
    input("")
    logic.new_move('äpple', 'pear')
    print(f"❌ HP after wrong move: {logic.get_hp()}")

    # Request hints
    print("\n💡 Player requests hints:")
    for _ in range(4):
        input("")

        print(f"Hint: {logic.get_hint()}")
        print(f"Hints left: {logic.get_hints_left()}")

    # Correct move
    print("\n✅ Player makes a correct move:")
    input("")
    logic.new_move('päron', 'pear')
    print(f"HP after the move: {logic.get_hp()}")

    # Losing the game
    input("")
    print("\n☠️ Simulating Game Over:")

    print(f'\n🎮 Player makes a second wrong move:')
    input("")
    logic.new_move('stol', 'table')
    print(f"❌ HP after second wrong move: {logic.get_hp()}")

    print(f'\n🎮 Player makes a third wrong move:')
    input("")
    logic.new_move('stol', 'table')
    print(f"❌ HP after third wrong move: {logic.get_hp()}")

    print(f"\nGame Over: {not logic.player_is_alive()}")


if __name__ == "__main__":
    demo_gameplay()
