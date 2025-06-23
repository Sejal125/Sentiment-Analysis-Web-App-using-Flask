import bz2

with bz2.open("train.ft.txt.bz2", mode="rt", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i < 100:
            print(line.strip())
