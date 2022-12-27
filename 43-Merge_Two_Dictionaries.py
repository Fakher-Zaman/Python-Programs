# Solution # 1(Using bar `|` operator)
dic1 = {"fakher": 90, "hammad": 80}
dic2 = {"hammad": 85, "shaban": 80}
print(dic1 | dic2)

# Solution # 1(Using kwargs `**` operator)
print({**dic1, **dic2})

# Solution # 1(Using copy() and update( method))
dic3 = dic2.copy()
dic3.update(dic1)
print(dic3)