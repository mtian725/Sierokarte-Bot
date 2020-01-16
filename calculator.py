import uncap

def calc_arcarum(summon, start, end):
    target = uncap.arcarum_summon[summon]
    if start > end:
        return {} #return an empty hash for now
    elif start == end:
        return {} #return an empty hash for now
    else:
        total = {}
        for x in range(start,end):
            for key, value in uncap.arcarum[target][x].items():
                if key in total:
                    total[key] = total[key] + value
                else:
                    total[key] = value
        return total

def arcarum(summon, start, end):
    total = calc_arcarum(summon,start,end)
    output = ''
    for key,value in total.items():
        output = output + key + ' : ' + str(value) + '\n'

    return output
