def commonCh(d1, d2):
    s1 = set(d1)
    s2 = set(d2)
    s3 = s1 & s2
    print(list(s3))

commonCh('dev', 'red')
