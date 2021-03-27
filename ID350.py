def counting(Z, I, M, L):
    memory = [L]

    while True:
        tmp = (memory[-1]*Z + I) % M

        if tmp not in memory:
             memory.append(tmp)
        else:
            break

    return len(memory)

collect = []
t = 0
while True:
    in_ = input()
    Z, I, M, L = [int(x) for x in in_.strip().split(' ')]
    t += 1
    
    if (Z == 0)&(I == 0)&(M == 0)&(L == 0):
        for x in collect:
            print(x)
        break

    cycle = counting(Z, I, M, L)
    collect.append(f'Case {t}: {cycle}')