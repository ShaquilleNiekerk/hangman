# Hangman

* Begin by choosing a difficulty, this will determine the word length and 
  complexity.
* You will be shown the length of a randomly selected word as well as one letter
  of that word.
* You will have four(4) chances to guess the word.

## To run
* `python3 hangman.py`
* Follow the input prompts to play the game.

## To test
* To run all the unittests: `python3 -m unittest tests/test_main.py`
* To run a specific step's unittest, e.g step *1*: 
  `python3 -m unittest tests.test_main.MyTestCase.test_step1`