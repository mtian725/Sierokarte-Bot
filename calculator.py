import uncap

def calc_arcarum(summon, start, end):
    target = uncap.arcarum_summon[summon]
    if start > end:
        return {'Greater':-1}
    elif start == end:
        return {'Equal':-1}
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
    if 'Greater' in total:
        return '**Chose a start step that was later than the end step**'
    elif 'Equal' in total:
        return '**Chose a start step that is the same as the end step**'
    else:
        output = ''
        for key,value in total.items():
            output = output + key + ' : ' + str(value) + '\n'

        return output
