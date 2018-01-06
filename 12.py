import sys
import enchant 

total = 0
percentage = 0
progress = 0
d = enchant.Dict("nl_NL")

def is_valid(vars) :
    return (vars[9] + vars[10]) <= 10
    #for i in range(0,len(n)) :
    #    left = vars[i]
    #    right = vars[i+1]
    #    under = vars[i+len(n)+1]
    #    if(left+right+under != n[i]) :
    #        return False
    #return True

def to_char(n) :
    return str(unichr(96+n))


def pretty_print(vars) :
    characters = ''
    for v in vars :
        characters = characters + to_char(v)
    return characters

def pretty_print_complex(vars) :
    a = ''
    b = ''
    for i in range(len(vars)) :
        if i % 2 == 0 :
            a = a + to_char(vars[i])
        else :
            b = b + to_char(vars[i])
    return a + b

def check_word(string, min, max) :
    result = set()
    for i in range(min,max) :
        w = string[0:i]
        if d.check(w) :
            if len(string)-i >= min :
                temp_result = check_word(string[i:],min,max)
                for tr in temp_result :
                    result.add(string[0:i] + ' ' +tr)
            else :
                result.add(string[0:i] + ' ' +string[i:])
    return result

def permutations(vars, n, i) :
    global progress
    for c in range(1,27) :
        progress = progress + 1
        print str((progress / float(total)) * 100) + '%'
        vars[i] = c
        if is_valid(vars,n) :
            print pretty_print(vars)
        if(i < len(vars)-1) :
            permutations(vars, n, i+1)

def find_parts(sum,n) :
    if n == 1 :
        return [[sum]]
    results = []
    for i in range(1,27) :
        if (sum - i <= (n-1)*26) and (sum - i >= (n-1)) :
            temp_results = find_parts(sum-i,n-1)
            for tr in temp_results :
                results.append([i]+tr)
    return results

def find(n) :
    global total, percentage
    vars = [1] * (len(n)*2+1)
    total = 26 ** len(vars)
    percentage = total / 10000000
    permutations(vars,n,0)


def to_int_array(n) :
    ints = [0] * len(n)
    for i in range(len(n)) :
        ints[i] = int(n[i])
    return ints

def link(current, all_groups, n) :
    if not (n in all_groups) :
        if is_valid(current) :
            s = pretty_print_complex(current)
            results = check_word(s,2,6)
            if len(results) > 0 :
                for r in results :
                    print r
    else :
        starts = all_groups[n]
        possible = []
        if n == 0 :
            for start in starts:
                possible = possible + starts[start]
        else :
            start = current[-1]
            if start in starts :
                possible = starts[current[-1]]
            else :
                return
        for p in possible :
            link(current[0:-1] + p, all_groups, n+1)

def find_groups(n) :
    all_groups = {}
    for i in range(len(n)) :
        parts = find_parts(n[i],3)
        print len(parts)
        start = {}
        for part in parts :
            if part[0] in start :
                start[part[0]].append(part)
            else :
                start[part[0]] = [part] 
        all_groups[i]= start
    #print all_groups[1]
    link([],all_groups,0)


if __name__ == "__main__" :
    n = sys.argv[1:]
    n = to_int_array(n)
    find_groups(n)
