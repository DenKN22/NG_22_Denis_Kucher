listNum = list(map(int, input("Write you Number: ").split(",")))
print(listNum)
Max = max(listNum)
Min = min(listNum)
print("Max element is", Max)
print("Min element is", Min)
listNum.remove(Max)
listNum.remove(Min)
print("You sum",sum(listNum))




