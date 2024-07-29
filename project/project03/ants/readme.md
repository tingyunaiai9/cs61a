# Project 3: Ants Vs. SomeBees

![Ants vs. Somebees](https://www.learncs.site/assets/images/splash-ada102e8bbe59adbdb5cf5ae24c7ab49.png)

> The bees are coming!
> Create a better soldier
> With inherit-ants.

## The Game [​](https://www.learncs.site/docs/curriculum-resource/cs61a/project/ants#the-game "Direct link to The Game")

A game of Ants Vs. SomeBees consists of a series of turns. In each turn, new bees may enter the ant colony. Then, new ants are placed to defend their colony. Finally, all insects (ants, then bees) take individual actions. Bees either try to move toward the end of the tunnel or sting ants in their way. Ants perform a different action depending on their type, such as collecting more food or throwing leaves at the bees. The game ends either when a bee reaches the end of the tunnel (ants lose), the bees destroy a QueenAnt if it exists (ants lose), or the entire bee fleet has been vanquished (ants win).

![](https://www.learncs.site/assets/images/screenshot-76f2da622efa6459983ab452c37ac28b.gif)

### Core concepts[​](https://www.learncs.site/docs/curriculum-resource/cs61a/project/ants#core-concepts "Direct link to Core concepts")

**The Colony**. This is where the game takes place. The colony consists of several `Place`s that are chained together to form tunnels through which the bees travel. The colony also has some quantity of food which can be expended in order to place an ant in a tunnel.

**Places**. A place links to another place to form a tunnel. The player can put a single ant into each place. However, there can be many bees in a single place.

**The Hive**. This is the place where bees originate. Bees exit the beehive to enter the ant colony.

**Ants**. The player places an ant into the colony by selecting from the available ant types at the top of the screen. Each type of ant takes a different action and requires a different amount of colony food to place. The two most basic ant types are the `HarvesterAnt`, which adds one food to the colony during each turn, and the `ThrowerAnt`, which throws a leaf at a bee each turn. You will be implementing many more!

**Bees**. Each turn, a bee either advances to the next place in the tunnel if no ant is in its way, or it stings the ant in its way. Bees win when at least one bee reaches the end of a tunnel. In addition to the orange bees, there are yellow wasps that do double damage and a green boss bee that is quite difficult to vanquish.

### Core classes[​](https://www.learncs.site/docs/curriculum-resource/cs61a/project/ants#core-classes "Direct link to Core classes")

The concepts described above each have a corresponding class that encapsulates the logic for that concept. Here is a summary of the main classes involved in this game:

*   **`GameState`**: Represents the colony and some state information about the game, including how much food is available, how much time has elapsed, where the `AntHomeBase` is, and all the `Place`s in the game.
*   **`Place`**: Represents a single place that holds insects. At most one `Ant` can be in a single place, but there can be many `Bee`s in a single place. `Place` objects have an `exit` to the left and an `entrance` to the right, which are also places. Bees travel through a tunnel by moving to a `Place`'s `exit`.
*   **`Hive`**: Represents the place where `Bee`s start out (on the right of the tunnel).
*   **`AntHomeBase`**: Represents the place `Ant`s are defending (on the left of the tunnel). If `Bee`s get here, they win :(
*   **`Insect`**: A base class for `Ant` and `Bee`. Each insect has a `health` attribute representing its remaining health and a `place` attribute representing the `Place` where it is currently located. Each turn, every active `Insect` in the game performs its `action`.
*   **`Ant`**: Represents ants. Each `Ant` subclass has special attributes or a special `action` that distinguish it from other `Ant` types. For example, a `HarvesterAnt` gets food for the colony and a `ThrowerAnt` attacks `Bee`s. Each ant type also has a `food_cost` attribute that indicates how much it costs to deploy one unit of that type of ant.
*   **`Bee`**: Represents bees. Each turn, a bee either moves to the `exit` of its current `Place` if the `Place` is not `blocked` by an ant, or stings the ant occupying its same `Place`.

### Game Layout[​](https://www.learncs.site/docs/curriculum-resource/cs61a/project/ants#game-layout "Direct link to Game Layout")

Below is a visualization of a GameState.

![](https://www.learncs.site/assets/images/colony-drawing-f3a5a5b1d92423e41462e8316b5ec05c.png)

To help visualize how all the classes fit together, [here](https://www.learncs.site/assets/files/ants_diagram-2c04eda6fa437f165e3fbc8dbc5f3739.pdf) is a diagram of all of the classes and their inheritance relationships.

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
