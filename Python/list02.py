r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))

print(r.count(3))

if 100 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = "My name is Iram"
to_split = s.split(' ')
print(to_split)
x = ' '.join(to_split)
print(x)

print(help(list))
