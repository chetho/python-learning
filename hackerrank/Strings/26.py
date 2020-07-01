def minion_game(string):
    string = string.upper()
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += (len(string)-i)
            print('k',kevin_score)
        else:
            stuart_score += (len(string)-i)
            print('s',stuart_score)
    if kevin_score > stuart_score:
        print('Kevin',kevin_score)
    elif kevin_score < stuart_score:
        print('Stuart',stuart_score)
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)