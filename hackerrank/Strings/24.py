# Alphabet Rangoli

def print_rangoli(size):
    d = '-'
    l = []
    for x in range(size):
        l.append(chr(97+x))
    wl = '-'.join(l)
    width = len(wl) * 2 - 1
    if size == 1:
        print('a')
    else:
        for i in range(len(wl),0,-1):
            if (i % 2 == 0):
                print((wl[:i:-1]+wl[i:]).center(width,'-'))
            if( i == 1):
                print((wl[:i:-1]+'-a'+wl[i:]).center(width,'-'))
        for i in range(1,len(wl)+1):
            if (i % 2 == 0):
                print((wl[:i:-1]+wl[i:]).center(width,'-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)