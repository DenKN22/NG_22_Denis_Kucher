string = str(input("Write you word: "))
dictionary = {}
print("Count of elements", len(string))
for i in string:
    dictionary[i] = string.count(i) 
    print(i,"-",string.count(i))
print(dictionary)
sortedDict = dict(sorted(dictionary.items()))
print("sorted count of elements", sortedDict)



