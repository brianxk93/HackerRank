"""
MergeTheTools.py

1/9/2018

HackerRank Question:

Consider the following:

1. A string, s, of length n where s = c_0c_1...c_n-1.
2. An integer, k, where k is a factor of n.

We can split s into n/k subsegments where each subsegment, t_i, consists of a
contiguous block of k characters in s. Then, use each t_i to create string u_i such that:

1. The characters in u_i are a subsequence of the characters in t_i.
2. Any repeat occurrence of a character is removed from the string such that each
character in u_i occurs exactly once. In other words, if the character at some index j
in t_i occurs at a previous index <j in t_i, then do not include the character in string u_i.

Given s and k, print n/k lines where each line i denotes string u_i.


Input Format:
The first line contains a single string denoting s. 
The second line contains an integer, k, denoting the length of each subsegment.

Constraints:
1. 1 <= n <= 10^4, where n is the length of s
2. 1 <= k <= n
3. It is guaranteed that n is a multiple of k.

Output Format:
Print n/k lines where each line i contains string u_i.

Sample Input:
AABCAAADA
3

Sample Output:
AB
CA
AD
"""

def create_subsegments(in_str, substr_len):

    current_index = 0
    end_index = substr_len
    subsegments = []

    while current_index < len(in_str):
        subsegments.append(in_str[current_index:end_index])
        current_index += substr_len
        end_index += substr_len

    return subsegments


def merge_the_tools(string, k):
    subsegments = create_subsegments(string, k)

    # subsegments with duplicates chars removed
    trimmed_subsegments = []
    
    for segment in subsegments:
        trimmed_segment = ""
        for char in segment:
            if char not in trimmed_segment:
                trimmed_segment += char
        trimmed_subsegments.append(trimmed_segment)
    
    print(*trimmed_subsegments, sep='\n')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
