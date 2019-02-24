if __name__ == "__main__":
    s = set([2, 3, 4, 1, 2, 3, 7])
    d = dict({"a" : 1, "b" : 2, 2 : 3, 5 : 7})
    l = list([2, 3, 4, 1, 2])
    print(set([1, 2, 3]).issubset(s))
    print((d[2], d["a"]))
    print(set([8, 1, 2, 3]).difference(s))
    print(l.count(2))