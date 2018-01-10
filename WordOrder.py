"""
WordOrder.py

1/10/2018

You are given n words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.

Note: Each input line ends with a '\n' character.


Constraints:  
The sum of the lengths of all the words do not exceed 10^6
All the words are composed of lowercase English letters only.


Input Format:
The first line contains the integer, n. 
The next n lines each contain a word.

Output Format:
On the first line, output the number of distinct words from the input. 
On the second line, output the number of occurrences for each distinct word according to their
appearance in the input.


Sample Input:
4
bcdef
abcdefg
bcde
bcdef

Sample Output:
3
2 1 1
"""
from collections import OrderedDict

def word_order(in_words):
    occurrences_per_word = OrderedDict()
    
    for word in in_words:
        if word in occurrences_per_word:
            occurrences_per_word[word] += 1
        else:
            occurrences_per_word[word] = 1
    
    # Output number of unique words
    print(len(occurrences_per_word)) 
    
    # Output occurrences per word
    for key, value in occurrences_per_word.items():
        print(value, end=' ') 
  
if __name__ == "__main__":
    num_words = int(input())
    in_words = []
    
    for _ in range(num_words):
        in_words.append(input())
        
    word_order(in_words)
