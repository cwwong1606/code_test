def analyze(in_):
    last = 0
    for count, i in enumerate(range(1, 20000)):
        last += i
        if last >= in_:
            break
    last -= i
    total = count + 2

    diff = in_ - last
    row = total - diff
    col = diff
    
    return row, col

collect = []
while True:
    in_ = input()
    
    if len(in_) == 0:
        for x in collect:
            print(x)
        break
    
    in_ = int(in_)
    r, c = analyze(in_)
    collect.append(f'TERM {in_} IS {r}/{c}')