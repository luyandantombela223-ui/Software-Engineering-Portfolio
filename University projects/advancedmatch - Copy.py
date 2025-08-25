# A code to macth word in advanced way
# Luyanda Ntombela
# 01 May 2025


def match(pattern, word):
    if pattern == '' and word == '':
        return True
    if pattern == '*' and word == '':
        return True
    if pattern == '' or (word == '' and pattern != '*'):
        return False

    if pattern[0] == word[0] or pattern[0] == '?':
        return match(pattern[1:], word[1:])
    if pattern[0] == '*':
        return match(pattern[1:], word) or (word != '' and match(pattern, word[1:]))
    return False
