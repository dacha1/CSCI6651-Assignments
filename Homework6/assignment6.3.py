import shelve
d = shelve.open(quotes)
d[key] = data
data = d[key]
del d[key]
flag = d.has_key(key)
klist = d.keys()
d['xx'] = range(4)
d['xx'].append(5)
temp = d['xx']
temp.append(5)
d['xx'] = temp
d.close()


