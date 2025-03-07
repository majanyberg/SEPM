# main.py
from puzzle_logic.apis.logic import Logic
from puzzle_logic.model.category import Category


def main():
    # Create game logic instance
    logic = Logic()
    print(f'Game started')
    logic.init_player(3, 3, Category.FOOD)
    print(f'player grid = {logic.get_grid()}')
    print(f'player hp = {logic.get_hp()}')
    print(f'player hints left = {logic.get_hints_left()}')
    
    print(f'*makes wrong move*')
    logic.new_move('äpple', 'pear')
    print(f'player hp after faulty move = {logic.get_hp()}')
    print(f'Request hints')
    print(f'get hint returns = {logic.get_hint()}')
    print(f'Player hints left = {logic.get_hints_left()}')
    print(f'get hint returns = {logic.get_hint()}')
    print(f'Player hints left = {logic.get_hints_left()}')
    print(f'get hint returns = {logic.get_hint()}')
    print(f'Player hints left = {logic.get_hints_left()}')
    print(f'get hint returns = {logic.get_hint()}')
    print('----------------------------------------')
    print(f'*makes correct move*')
    print(f'player hp = {logic.get_hp()}')
    print(f"move:{logic.new_move('paron', 'pear')}")
    print(f'player hp = {logic.get_hp()}')
    print(f'player is alive:{logic.player_is_alive()}')
    """
    print('----------------------------------------')
    print('cannot make same move twice!!')
    print(f'*makes correct move again*')
    print(f'player hp = {logic.get_hp()}')
    print(f'move:{logic.new_move('päron', 'pear')}')
    print(f'player hp = {logic.get_hp()}')
    print(f'player is alive:{logic.player_is_alive()}')
    print('----------------------------------------')
    """
    print(f'*Makes the second wrong move*')
    logic.new_move('Stol', 'Table')
    print(f'player hp after faulty move = {logic.get_hp()}')
    print(f'player alive: {logic.player_is_alive()}')
    print(f'*Makes the third wrong move*')
    logic.new_move('Stol', 'Table')
    print(f'player hp after faulty move = {logic.get_hp()}')
    print(f'player won={logic.player_won()}')
    print(f'player is alive:{logic.player_is_alive()}')
    print('----------------------------------------')
    print('checking coords')
    """"
    print(f'5, 7 = {logic.validate(5,7)}')
    print(f'10, 8 = {logic.validate(10,8)}')
    print(f'12, 15 = {logic.validate(12,15)}')
    """
    print(f'13, 4 = {logic.validate(5,7)}')
    print(f'10, 8 = {logic.validate(10,8)}')
    print(f'12, 15 = {logic.validate(12,15)}')
    while True:
        x = input("x")
        y = input("y")
        print(logic.validate(int(x),int(y)))

if __name__ == "__main__":
    main()
