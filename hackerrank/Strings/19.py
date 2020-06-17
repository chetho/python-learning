# String Validators

if __name__ == '__main__':
    s = input()
    alnu = False
    al = False
    nu = False
    il = False
    iu = False
    for i in s:
        if i.isalpha():
            al = True
        elif i.isdigit():
            nu = True
        if i.islower():
            il = True
        elif i.isupper():
            iu = True
        if al and nu:
            alnu = True
        else:
            alnu = False
    print(alnu)
    print(al)
    print(nu)
    print(il)
    print(iu)