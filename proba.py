chordList = ["[C", "(Cm", "E)", "(Db)"]

for i in range(len(chordList)):
    if chordList[i].startswith("("):
        chordList[i] = chordList[i][1:]
    if chordList[i].endswith(")"):
        chordList[i] = chordList[i][:-1]

print(chordList)