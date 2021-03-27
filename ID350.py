def counting(Z, I, M, L):
    memory = [L]
    last = L
    start = L

    while True:
        last = (last*Z + I) % M

        if start != last:
             memory.append(last)
        else:
            break

    return len(memory)

collect = []
t = 0
while True:
    
    in_ = input()
    seq = [int(x) for x in in_.strip().split(' ')]
    Z, I, M, L = seq[0], seq[1], seq[2], seq[3]
    t += 1
    
    if sum(seq) == 0:
        for x in collect:
            print(x)
        break

    cycle = counting(Z, I, M, L)
    collect.append(f'Case {t}: {cycle}')    