def calculate(l):
    if isinstance(l, list):
        res = 0
        for i in l:
            if isinstance(i, str):
                try:
                    res += int(i)
                except ValueError:
                    res += 0
        return res
    return False

print(calculate(['4', '3', '-2']))
print(calculate(453))
print(calculate(['nothing', 3, '8', 2, '1']))
print(calculate('54'))