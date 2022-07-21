def getKey(obj):                            #this will provide the 1st key of Dict
    keys = list(obj)                        #a (keys present in dict)
    if len(keys) != 1:
        return None
    else:
        return keys[0]                      #a


def getValue(obj, Key):
    if type(obj) is not dict:
        return None
    if (Key in obj.keys()) :                    # obj.keys() is dict_keys(['a']) and Key is input
        #print(Key)                              #a
        #print(obj[Key])                         #{'b': {'c': 'd'}}
        if type(obj[Key]) is dict:
            return getValue(obj[Key], getKey(obj[Key]))     # obj={'b': {'c': 'd'}} and key will be 'b' (from getkey(obj) function)
        else:
            return obj[getKey(obj)]             #to provide final output when only value will remain
    else:
        nextKey = getKey(obj)                   #for the case scenario when Input key is nested (b or c instaed of a)
        return getValue(obj[nextKey], Key)      #obj[a] = {'b': {'c': 'd'}} and Key will be b/c, then it will start from scratch


obj = {'a': {'b': {'c': 'd'}}}
Key = 'a'
outp = getValue(obj, Key)
print(outp)