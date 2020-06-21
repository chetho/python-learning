# Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT

input_list = map(int,input().split())
l = list(input_list)
n,m = l[0],l[1]
c = '.|.'
welcome = 'WELCOME'
d = '-'
for i in range(1,n+1):    
    if (i % 2 == 1) and i != n:
        print((c*i).center(m,d))
    if (i == n ):
        print((welcome).center(m,d))
for i in range(n,0,-1):
    if (i % 2 == 1) and i != n:
        print((c*i).center(m,d))