#https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true

from collections import Counter

if __name__ == '__main__':
    s = input()

    # 1. Count occurrences of each character
    counts = Counter(s)
    
    # 2. Sort the counts
    # first priority: -x[1] (Frequency, descending)
    # second priority: x[0] (Character, ascending/alphabetical - in case of freq. ties)
    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    # 3. Print the top 3
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")
