def generate_label(charge):
    ap = [('b' + str(x+1), 'y' + str(x+1)) for x in range(charge)]
    return sorted([x for y in ap for x in y])
