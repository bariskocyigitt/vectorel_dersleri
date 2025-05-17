for a in range(11):
    if a%2==0 : continue
    for b in range(11):
        print(f"{a} x {b}= {a*b}")
    print()
    if a>5 : break  
    