def GenerateCombinations(array, tuple_length, prev_array=[], used_array = []):
    if len(prev_array) == tuple_length:
        return [prev_array]
    combs = []
    for i, val in enumerate(array):
        if(prev_array):
            print(val, "and", prev_array, "and", used_array)
        if(not prev_array):
            combs += GenerateCombinations(array[i+1:], tuple_length, [val])
        elif(val[0] == prev_array[-1][-1]):
          prev_array_extended = prev_array.copy()
          prev_array_extended.append(val)
          used_array_extended = used_array.copy()
          used_array_extended.append(val)
          combs += GenerateCombinations(array[i+1:], tuple_length, prev_array_extended, used_array_extended)
        elif(val[-1] == prev_array[0][0]):
            prev_array_extended = prev_array.copy()
            prev_array_extended.insert(0,val)
            used_array_extended = used_array.copy()
            used_array_extended.append(val)
            combs += GenerateCombinations(array[i+1:], tuple_length, prev_array_extended, used_array_extended)
            combs += GenerateCombinations(used_array, tuple_length, prev_array_extended, [])
    return combs

x = GenerateCombinations(['ab','bc','bd','cb'],3)
print(x)

#ab -> bc -> cb -> bd should be valid