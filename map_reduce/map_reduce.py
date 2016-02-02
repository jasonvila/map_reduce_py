__author__ = 'jason'

import itertools


# i.items() - copy of dictionary
# intermediate.extend() - extends the list
def map_reduce(i, mapper, reducer):
    intermediate = []
    for (key,value) in i.items():
        intermediate.extend(mapper(key,value))
        print(intermediate)

    # itertools - iterator tools - group the sorted list to lambda x:x[0]
    groups = {}
    for key, group in itertools.groupby(sorted(intermediate), lambda x: x[0]):
        groups[key] = list([y for x, y in group])

    return [reducer(intermediate_key, groups[intermediate_key]) for intermediate_key in groups]