from resources import uncap

def calc_arcarum(summon, start, end):
    if start > end:
        return {'Greater':-1}
    elif start == end:
        return {'Equal':-1}
    else:
        total = {}
        for x in range(start,end):
            for key, value in uncap.arcarum[summon][x].items():
                if key in total:
                    total[key] = total[key] + value
                else:
                    total[key] = value
        return total

def arcarum(summon, start, end, toggle):
    target = uncap.arcarum_summon[summon]
    output = ''
    if toggle == 0:
        for x in range(start,end):
            output = output+'__'+uncap.steps[x+1]+'__\n'
            for key,value in uncap.arcarum[target][x].items():
                output = output + key + ' : ' + '×' +  str(value) + '\n'

            output = output+'\n'

        return output
    else:
        total = calc_arcarum(target,start,end)
        if 'Greater' in total:
            return '**Chose a start step that was later than the end step**'
        elif 'Equal' in total:
            return '**Chose a start step that is the same as the end step**'
        else:
            for key,value in total.items():
                output = output + key + ' : ' + '×' + str(value) + '\n'

            return output
