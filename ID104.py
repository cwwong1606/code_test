import sys

def simulation(n, P):

    previous = {'1': 1}
    out = 'no arbitrage sequence exists'

    for l in range(1, n + 1):
        exchange = {}
        for k, v in previous.items():
            for i in range(len(P)):
                exchange[f'{k} {i + 1}'] = P[int(k[-1]) - 1][i]*v
        success = {k:v for k,v in exchange.items() if (k[-1] == '1')&(v >= 1.01)}

        if len(success) > 0:
            max_ = 1
            for k1, v1 in success.items():
                if v1 > max_:
                    max_ = v1
                    out = k1
            break
        else:
            previous = exchange
        
    return out

display = []
while True:

    in_ = input()
    if (len(in_) == 0):
        for x in display:
            print(x)
        break
    
    seq = [float(x) for x in in_.strip().split(' ')]
    
    if len(seq) == 1:
        n = int(seq[0])
        t = 0
        P = []
    else:
        P.append(seq[:t] + [1] + seq[t:])
        t += 1         
    
    if len(P) == n:
        out = simulation(n, P)
        display.append(out)
        
sys.exit(0)