**Logic Architecture**
*Usage Guide*

**1.** ***Initializing a game***

In order to initialize the game, the *UI* object must instantiate the *LOGIC*. This is done by simply calling the class. Once an instance exists, a player can be created by calling the *init_player* function. The function takes three variables:
*1. Health-Points, 2. Number of hints, 3. Category*
In order to stay consistent, the category is picked via an enum-class: *Category*.
```
logic = Logic() # the logic object
logic.init_player(5,5, Category.FOOD) # 5 HP, 5 Hints, Category = Food
```
**2. *Getters***

The logic layer has multiple functions for retrieving useful data.
```
logic.get_hp() #returns the players current HP
logic.get_hints_left() # returns how many hints the player has left
logic.get_hint() # returns a random hint
```
There are also functions for checking if the game should end.
```
logic.player_is_alive() # True if player is alive, False if not
logic.player_won() # True if player has found all correct words, False if not
```

**3.** ***Making a move***

When a player makes a move, the process of validating this move is straight-forward.
The function *new_move* takes the swedish word along with the english word. The Logic object will take care of updating the players health-points. The workflow we propose for this action is to: *1. make a move, 2. update the visuals via get functions and check if the player is still alive.*
```
logic.new_move('äpple', 'pear')
logic.get_hp()
logic.player_is_alive()
```

**4. *Validation feedback on character selection***

We have introduced a validation function that processes coordinate inputs $(x, y)$. When a user taps a coordinate that belongs to a word, the function returns $1$. If the subsequent tap is adjacent and still part of the same word, it continues returning $1$. When the user completes the word by selecting its final character, the function returns $2$. If the tap is not on a connected character, tracking is discontinued and the function returns $0$.
The function can be used as an action to a button press 
```
logic.validate(5,7) # validates x=5, y=7
```
