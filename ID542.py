probs = []
countries = {}
i = 0

while True:
    
    if len(countries) < 16:
        countries[i] = str(input())
    else:
        p = [float(x)/100 for x in input().strip().split()]
        probs.append(p)
    i += 1
    
    if len(probs) == 16:
        
        semi_groups = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
        semi_probs = []
        for g in semi_groups:
            for k in g:
                if k%2 == 0:
                    vs = k + 1
                else:
                    vs = k - 1
                other = [x for x in g if (k != x)&(vs != x)]
                try:
                    p = probs[k][vs]*(probs[other[0]][other[-1]]*probs[k][other[0]] + probs[other[-1]][other[0]]*probs[k][other[-1]])
                    semi_probs.append(p)
                except:
                    print(k ,vs, other, p)
                
        final_probs = []
        final_groups = [[[0,1,2,3],[4,5,6,7]],[[8,9,10,11],[12,13,14,15]]]
        for g in final_groups:
            g0 = g[0]
            g1 = g[1]
            for k in g0:
                p = semi_probs[k]*sum([probs[k][x]*semi_probs[x] for x in g1])
                final_probs.append(p)
            for k in g1:
                p = semi_probs[k]*sum([probs[k][x]*semi_probs[x] for x in g0])
                final_probs.append(p)
                
        win_probs = []
        for g in range(16):
            if g < 8:
                win_probs.append(sum([probs[g][x]*final_probs[x] for x in range(8, 16)])* final_probs[g])
            else:
                win_probs.append(sum([probs[g][x]*final_probs[x] for x in range(8)])* final_probs[g])
        break
                
for k,v in countries.items():
    print("{0:10} p={1:.2f}%".format(str(v), win_probs[k]*100))
        
        