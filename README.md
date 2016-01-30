# Boggle_solver
Purpose: The purpose of this program is to find all of the words in a boggle game.

Requirements: This program uses python 3.1 or newer (https://www.python.org/downloads/).

General: This program can be run in either the python editor or directly from the file.

Steps: 
  1) print instructions
  2) accept word input
  3) load dictionary, if a word in the dictionary has a letter that is not on the board, then don't load it.
  4) for every word with a q in it, if the next letter is not a u, then get rid of it.
  5) for words with qu remove the u to make processing easier.
  6) perform recursive search
        A) for every word left from the dictionary, start function with the first letter of the word
        B) if the second letter of the word is found adjacent to the first letter then search with the second letter
        C) if the third letter of the word is found adjacent to the second letter then search with the third letter
        .... (continue until 2nd to last letter. if at any time a branch dies, then go back to last call)
        D) if last lett of the word is found adjacent to the 2nd to last letter then return True through all calls
        E) if the first call returns True, then append the word to the correct list
        
  7) print formatted results
