# sWAP cASE
def swap_case(s):
    z = ''
    for c in s:
        if 97 <= ord(c) <= 122:
            z += chr(ord(c)-32)
        elif 65 <= ord(c) <= 90:
            z += chr(ord(c)+32)
        else:
            z += c
    return z

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)