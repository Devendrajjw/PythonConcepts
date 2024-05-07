from collections import OrderedDict
if __name__ == '__main__':
    data = [22, 11, 33, 11, 22, 99, 00, 12]
    sr = sorted(data, reverse=False)
    print(sr)
    # st = set(sr)
    # srs = st
    # print(sorted(srs))
    print(sorted(set(sr)))
