# Project 3: Ants Vs. SomeBees

## The Game

A game of Ants Vs. SomeBees consists of a series of turns. In each turn, new bees may enter the ant colony. Then, new ants are placed to defend their colony. Finally, all insects (ants, then bees) take individual actions. Bees either try to move toward the end of the tunnel or sting ants in their way. Ants perform a different action depending on their type, such as collecting more food or throwing leaves at the bees. The game ends either when a bee reaches the end of the tunnel (ants lose), the bees destroy a QueenAnt if it exists (ants lose), or the entire bee fleet has been vanquished (ants win).

## Playing the game

To start a graphical game, run:

```
python3 gui.py
```

After you start the graphical version, the game is (usually) available at http://127.0.0.1:31415/.

The game has several options that you will use throughout the project, which you can view with `python3 gui.py --help`.

```
usage: gui.py [-h] [-d DIFFICULTY] [-w] [--food FOOD]

Play Ants vs. SomeBees

options:
  -h, --help     show this help message and exit
  -d DIFFICULTY  sets difficulty of game (test/easy/normal/hard/extra-hard)
  -w, --water    loads a full layout with water
  --food FOOD    number of food to start with when testing
```

You can refresh the webpage to restart the game, but if you changed your code, you need to terminate `gui.py` and run it again. To terminate `gui.py`, you can hit `Ctrl + C` on the terminal.

You cannot have multiple tabs of this same Ants GUI open simultaneously or they will all error.

## More details

https://github.com/leejianping/cs61A-Spring2024/tree/main/projects/project03
