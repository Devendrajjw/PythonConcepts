# n = int(input())
# singer = list(map(int(input())))
def fav_song(singer):
    md = {}
    for sing in singer:
        if sing not in md:
            md[sing] = 1
        else:
            md[sing] += 1
    srmd = sorted(md.items(), key=lambda md:md[1])
    print(srmd[-1][0])

fav_song([1,2,2,2,3,4,5])
