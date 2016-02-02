__author__ = 'jason'

import string
import itertools
import os
import map_reduce

filenames = ["/text/a.txt","/text/b.txt","/text/c.txt"]

i = {}

print ((os.path.dirname(__file__) + "/text/a.txt"))
f = open ((os.path.dirname(__file__) + "/text/a.txt"))
print (f.read())
f.close()

for filename in filenames:
    filename = (os.path.dirname(__file__) +  filename)
    print (filename)
    f = open(filename)
    i[filename] = f.read()
    print (i[filename])
    f.close()

def mapper(input_key, input_value):
    print ("mapper - ", input_key)
    print ("mapper - ", input_value)
    return [(word, 1) for word in remove_punctuation(input_value.lower()).split()]

# s.maketrans - makes a translation of "" to ""
# s.translate - translate recognized keys to new values
# string.punctuation - all the different punctuation
def remove_punctuation(s):
    #return s.translate(s.maketrans("",""))
    print (string.punctuation)
    new_content = s
    for contents in string.punctuation:
        new_content = new_content.replace(contents, "")
        print (contents)
    return new_content
    #return s.replace(string.punctuation, "")

def reducer(intermediate_key, intermediate_value_list):
    print ("reducer - ", intermediate_key)
    print ("reducer - ", intermediate_value_list)
    return (intermediate_key, sum(intermediate_value_list))


"""
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
"""


print(map_reduce.map_reduce(i, mapper, reducer))