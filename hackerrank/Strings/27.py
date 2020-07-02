# Merge the Tools!

def merge_the_tools(string, k):
    # your code goes here
    x = list(string)
    y = k
    z = []
    final_list = []
    duplicate_list = []
    for i in range(len(x)):
        if i == 0 and len(x[i:y]) == k and x[i]:
            z.append(x[i:y])
        elif i % k == 0:
            y +=k
            z.append(x[i:y])
        elif len(x[i:y]) == k:
            z.append(x[i:y])
    for row in z:
        t_l = []
        for r in row:
            if r in t_l:
                duplicate_list.append(r)
            else:
                t_l.append(r)
        final_list.append(t_l)
    for row in final_list:
        print(''.join(row))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)