# Dominos Optimizer
A utility that finds the optimal first move in Mexican Train Dominos via algorithm.

## What Is Mexican Train Dominos?
Mexican Train Dominos is a type of dominos where each player builds a "train" off of a starting domino with 2 of the same values (a double). To play a domino, it has to have 1 matching value to the domino played before it. The goal of the game is to score the most points by playing as many dominos as possible. 

There are 2 reasons for this:
1. the winner is determined by adding up the values on all the dominos in your train
2. any dominos remaining in your hand get their values added up and subtracted from your final train score

During your first turn, you can play as many dominos as you like to build your initial train. You may only play 1 domino on all subsequent turns. This means the first turn is the most important and complicated turn in the game.

This is where the Domino Optimizer comes in: enter the starting domino and all the dominos in your hand, and it will find every possible train you could create organized by highest to lowest score. It returns the top 3 trains and their scores.

This is done through a recursive algorithm that iterated over each domino and finds all possible branches on that path.

## Getting Started
1. clone the repo
    ```sh
    git clone https://github.com/austincrowell1/expense_processor.git
    ```
2. ensure pipenv is installed
    ```sh
    pip install pipenv
    ```
3. install the pipenv
    ```sh
    pipenv install
    ```

## Running the App
Call program.py from the pipenv to run the app:
```sh
pipenv run python program.py
```

## Roadmap
- [ ] add error handling for user input as a stop gap
- [ ] work towards building a GUI to make the app more user friendly
    - This would allow the starting double and player's hand to be entered by selecting pictures of dominos instead of manually typing in the values.
    - even better but much more complicated: take a photo of the dominos in your hand and the starting domino and have the app pull the values from those
- [ ] make app more strategic by adding logic to deal with doubles
    - Doubles are special in Mexican Train Dominos - they can be played at any time to start a new train. This makes it often times worth it to hold onto them rather than playing them on the first turn.
    - For example if there are 2 trains with near the same score but one uses a double and one doesn't, it's typically better to choose the train that DOESN'T use the double. This provides some strategic flexiblity if you find yourself in a situation where you can't play a domino on any train. You could play the double you saved rather than not earning any points that turn.
    - ideally I'd like to have 2 different results sets: one based on raw score and the other based on the highest possible score playing the least amount of doubles
    - could keep a count of doubles used and sort the output by doubles used then score