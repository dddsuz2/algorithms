"""
Given a string, find the length of the longest substring
without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""

def longest_non_repeat(string):
    """
    Find the length of the longest substring
    without repeating characters.
    """
    if string is None:
        return 0
    dict = {}
    max_length = 0
    j = 0
    for i in range(len(string)):
        if string[i] in dict:
            j = max(dict[string[i]], j)
        dict[string[i]] = i + 1
        max_length = max(max_length, i - j + 1)
    return max_length

def longest_non_repeat_v2(s):
    """
    s[j]がwindow内に存在した場合、同じ位置が現れた最新の位置を参照し、
    iをその一つ先に更新する
    """
    window = dict()
    max_size = 0
    i, j, n = 0, 0, len(s)
    while i < n and j < n:
        if s[j] in window:
            i = max(i, window[s[j]] + 1)
        window[s[j]] = j
        max_size = max(max_size, j-i+1)
        j += 1
    return max_size

def longest_non_repeat_v1(s):
    """
    sliding windowを使う
    計算量はO(n)
    """
    window = set()
    max_size = 0
    i, j, n = 0, 0, len(s)
    while i < n and j < n:
        if s[j] not in window:
            window.add(s[j])
            max_size = max(len(window), max_size)
            j += 1
        else:
            window.discard(s[i])
            i += 1
    return max_size


