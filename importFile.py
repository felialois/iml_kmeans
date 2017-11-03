from scipy.io import arff
import numpy as np


def read_file(fl):
    data, meta = arff.loadarff(fl)
    # print(meta)
    meta.types()
    # print(meta.names())

    data2 = np.zeros(shape=(len(data), len(data[0])))

    for i in range(0, len(meta.names())):
        if meta.types()[i] == 'numeric':
            for j in range(0, len(data)):
                data2[j][i] = data[j][i]
        else:
            values = meta[meta.names()[i]][1]
            for j in range(0, len(data)):
                if data[j][i] == '?':
                    data2[j][i] = -1
                else:
                    data2[j][i] = values.index(data[j][i])
    return data2
    #print data2
