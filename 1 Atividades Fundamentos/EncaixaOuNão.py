N = int(input())

while N > 0:
    A, B = input().split()

    '''
    TODO: Check if B encaixa in A and print "encaixa" or "nao encaixa" for each pair.
    '''
    if A.endswith(B):
        print("encaixa")
    else:
        print("nao encaixa")

    N -= 1
