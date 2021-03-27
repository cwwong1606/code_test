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
    
    in_= stdin.readline()
    in_ = [int(x) for x in in_.strip().split()]
    
    if len(in_) == "":
        for x in collect:
            stdout.write("TERM {} IS {}/{}\n".format(in_, r, c))
        break

    r, c = analyze(in_)