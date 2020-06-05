X = ['a', 'b', 'c']

for i in X:

    globals()[i] = 1


for i in range(10):

    globals()['sss{}'.format(i)] = 2

