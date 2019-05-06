# My Markov Chain
## Setup requirements
* Python 3 in virtual environment using pipenv
* Random
## Running the program:
  In order to run the markov chain you must first clean the text by running clean.py on the sample text. Right now the cleaning
  code is very specific to the book recommendations. Then you can call main.py which will generate a sample book recommendation
  and save it to gen.txt. If you want to change any files simply change the python open() methods to contain the file of your
  choice.
## clean.py
  This script is only meant to be run once and has already been run on this repo. It goes through and removes the author and
  recommender's names.
## main.py
  This script generates text according to the markov chain. The markov chain consists of a dictionary where each key is a word
  and each value is an array of words that can follow. By using random.choice() one can find the next word in the sequence.
