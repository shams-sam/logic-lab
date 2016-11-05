def  sweetness(arr):
    init = {}
    final = {}
    result = 0
    for i in xrange(len(arr)):
        if init.get(arr[i], None) == None:
            init[arr[i]] = i
            final[arr[i]] = i
        else:
            final[arr[i]] = i    
    foreach elem in final.keys():
        result += (final[elem] - init[elem])
    return result

print sweetness([2,2])
