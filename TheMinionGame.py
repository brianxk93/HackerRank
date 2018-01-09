"""
TheMinionGame.py

1/9/2018

HackerRank Question:

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Scoring:
A player gets +1 point for each occurrence of the substring in the string S.

Input Format:
A single line of input containing the string S. 
Note: The string S will contain only uppercase letters: [A - Z].

Constraints:
0 < len(S) <= 10^6

Output Format:
The name of the winner and their score separated by a space.
If the game is a draw, print Draw.
"""

def isConsonant(letter):
    if letter not in ['A','E','I','O','U',]:
        return True
    else:
        return False
    
def minion_game(string):
    # Create local copies
    stuart_string = string
    kevin_string = string
    
    # Initialize scores
    stuart = 0
    kevin = 0
    
    # Stuart's score - consonants
    for index,char in enumerate(stuart_string):
        if isConsonant(char):
            stuart += len(stuart_string) - index
    
    # Kevin's score - vowels
    for index,char in enumerate(kevin_string):
        if not isConsonant(char):
            kevin += len(kevin_string) - index
    
    if stuart > kevin:
        print("Stuart " + str(stuart))
    elif kevin > stuart:
        print("Kevin " + str(kevin))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
