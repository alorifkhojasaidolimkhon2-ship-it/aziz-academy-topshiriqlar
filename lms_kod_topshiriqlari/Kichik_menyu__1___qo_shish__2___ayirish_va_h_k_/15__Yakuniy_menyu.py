while 1:
    s=input()
    if s=='0':
        print('Exit')
        break
    a,b=map(int,s.split())
    c=int(input())
    print([a+b,a-b,a*b,a/b,a//b,a%b][c-1])