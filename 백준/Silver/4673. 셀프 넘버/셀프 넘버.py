natural = set(range(10001))
not_self = {sum(map(int, str(i)))+i for i in range(10000)}
print(*sorted(natural - not_self), sep='\n')