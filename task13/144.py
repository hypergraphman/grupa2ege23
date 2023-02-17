g = {
    'A': 'BC',
    'B': 'CDK',
    'C': 'E',
    'D': 'CF',
    'E': 'DH',
    'F': 'E',
    'G': 'IF',
    'H': 'IFG',
    'I': 'ADE',
    'K': 'DF',
}
paths = set()


def find_paths(s, p):
    if len(p) > 1 and len(set(p)) < len(p):
        if p[0] == p[-1]:
            paths.add(p)
        else:
            return None
    for v in g[s]:
        find_paths(v, p + v)


find_paths('E', 'E')
print(paths)
print(len(paths))
