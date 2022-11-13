WordList= str(input("Write you word: "))
dictionary = {}
print("Count of elements", len(WordList))
for cycle in WordList:
    dictionary[cycle] = WordList.count(cycle) 
    print(cycle,"-",WordList.count(cycle))
print(dictionary)
sortDict = dict(sorted(dictionary.items()))
print("sorted count of elements", sortDict)



