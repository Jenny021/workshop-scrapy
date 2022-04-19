def anagrams(word, l):
    if isinstance(l, list) == False:
        return False
    L = []
    for i in l:
        if sorted(word) == sorted(i):
            L.append(i)
    return L


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))