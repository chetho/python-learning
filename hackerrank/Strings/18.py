# Find a string

def count_substring(string, sub_string):
    a = 0
    for i in range(0,len(string)):
        if string.find(sub_string,i) == i:
            a += 1
    return a

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)