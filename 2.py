#问题1
fi = open("test.txt", "r", encoding="utf-8")
txt = fi.read()
d = {}
exclude = "，。！？、（）【】<>《》=：+-*—“”…"
for word in txt:
    if word in exclude:
        continue
    else:
        d[word] = d.get(word,0)+1
fi.close()
ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
print(ls)
print("{}:{}".format(ls[0][0], ls[2][1]))
