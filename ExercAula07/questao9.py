nr_tabuada = int(input('Digite um numero para gerar a tabuada'))
for mult in range(10):
    print('%d x %d x %d' % (nr_tabuada, mult+1, nr_tabuada*(mult+1)))
