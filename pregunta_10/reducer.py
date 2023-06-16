#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from dataclasses import replace
import operator
from collections import defaultdict
import sys

if __name__ == '__main__':

    Dict = defaultdict(list)

    for line in sys.stdin:

        key, val = line.replace('\n', '').strip().split('\t')
        val = val.split(',')

        for letra in val:
            Dict[letra].append(key)

    sortedDict = sorted(Dict.items(), key = operator.itemgetter(0))

    for clv, vlr in sortedDict:
        result = sorted(vlr, key = int)
        vlr =','.join(map(str, result))

     
        sys.stdout.write("{}\t{}\n".format(clv, vlr))
