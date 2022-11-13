WordList= str(input("Write you word: "))
dictionary = {}
print("Count of elements", len(WordList))
for i in WordList:
    dictionary[i] = WordList.count(i) 
    print(i,"-",WordList.count(i))
print(dictionary)
sortDict = dict(sorted(dictionary.items()))
print("sorted count of elements", sortDict)



